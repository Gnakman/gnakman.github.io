import numpy as np
import os

# ── Test section (fixed exit) ─────────────────────────────────────────────────
R2 = 0.125  # outlet half-size [m]  (0.25 × 0.25 m test section)

# ── CR table: (CR, inlet W=H [m], nozzle length [m]) ─────────────────────────
# Derived from sizing study; see design/index.md
CR_DATA = [
    (6.0,  0.612, 0.691),
    (6.5,  0.637, 0.719),
    (7.0,  0.661, 0.746),
    (7.5,  0.685, 0.772),
    (8.0,  0.707, 0.798),
    (8.5,  0.729, 0.822),
    (9.0,  0.750, 0.846),
]

# ── Mesh resolution ───────────────────────────────────────────────────────────
Nx = 50
Ny = 20
Nz = 20

# ── Output root ───────────────────────────────────────────────────────────────
OUTPUT_ROOT = r"\\wsl.localhost\Ubuntu\home\gnakman\OpenFOAM\gnakman-13\run\WindTunnel\Duct_Design\Curved\3D"

# ── Bell-Mehta 5th-order polynomial ──────────────────────────────────────────
# y(xi) = dR*(6*xi^5 - 15*xi^4 + 10*xi^3) + R1,  xi = x/L
# BCs: y(0)=R1, y(1)=R2, y'(0)=y'(1)=0, y''(0)=y''(1)=0
def make_half_size(R1, R2, L):
    dR = R2 - R1
    def half_size(x):
        xi = x / L
        return dR * (6*xi**5 - 15*xi**4 + 10*xi**3) + R1
    return half_size

# ── Spline points for one streamwise corner edge ──────────────────────────────
N_SPLINE = 50

def spline_pts(hs, L, y_sign, z_sign):
    x_sp = np.linspace(0, L, N_SPLINE + 2)[1:-1]
    r_sp = hs(x_sp)
    lines = [f"        ({x:.6f} {y_sign*r:.6f} {z_sign*r:.6f})"
             for x, r in zip(x_sp, r_sp)]
    return "\n".join(lines)

# ── Generate one blockMeshDict per CR ─────────────────────────────────────────
for cr, WH, L in CR_DATA:
    R1 = WH / 2
    dR = R2 - R1
    hs = make_half_size(R1, R2, L)

    #   Square cross-section vertices
    #   Inlet face (x=0), viewed from -x:
    #        z-min          z-max
    #   y+:   3 ──────────── 7
    #         │              │
    #   y-:   0 ──────────── 4
    #   Outlet: 1(y-,z-) 2(y+,z-) 6(y+,z+) 5(y-,z+)
    v = [
        (0.0,  -R1, -R1),  # 0  inlet  y-min z-min
        (L,    -R2, -R2),  # 1  outlet y-min z-min
        (L,     R2, -R2),  # 2  outlet y-max z-min
        (0.0,   R1, -R1),  # 3  inlet  y-max z-min
        (0.0,  -R1,  R1),  # 4  inlet  y-min z-max
        (L,    -R2,  R2),  # 5  outlet y-min z-max
        (L,     R2,  R2),  # 6  outlet y-max z-max
        (0.0,   R1,  R1),  # 7  inlet  y-max z-max
    ]

    def fv(i, _v=v):
        return f"({_v[i][0]:.6f} {_v[i][1]:.6f} {_v[i][2]:.6f})"

    cr_tag = f"CR{cr:.1f}".replace(".", "p")
    case_dir = os.path.join(OUTPUT_ROOT, cr_tag)
    os.makedirs(case_dir, exist_ok=True)
    out_path = os.path.join(case_dir, "blockMeshDict")

    bmd = f"""\
/*--------------------------------*- C++ -*----------------------------------*\\
| =========                 |                                                 |
| \\\\      /  F ield         | OpenFOAM                                        |
|  \\\\    /   O peration     |                                                 |
|   \\\\  /    A nd           |                                                 |
|    \\\\/     M anipulation  |                                                 |
\\*---------------------------------------------------------------------------*/
FoamFile
{{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      blockMeshDict;
}}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// Contraction ratio : CR = {cr}
// Inlet             : {2*R1:.3f} x {2*R1:.3f} m
// Outlet            : {2*R2:.3f} x {2*R2:.3f} m
// Length            : {L:.3f} m
// Profile           : Bell-Mehta 5th-order polynomial
//   y(xi) = dR*(6*xi^5 - 15*xi^4 + 10*xi^3) + R1
//   dR={dR:.6f} m   R1={R1:.6f} m   R2={R2:.6f} m

scale 1;

vertices
(
    {fv(0)}  // 0  inlet  y-min z-min
    {fv(1)}  // 1  outlet y-min z-min
    {fv(2)}  // 2  outlet y-max z-min
    {fv(3)}  // 3  inlet  y-max z-min
    {fv(4)}  // 4  inlet  y-min z-max
    {fv(5)}  // 5  outlet y-min z-max
    {fv(6)}  // 6  outlet y-max z-max
    {fv(7)}  // 7  inlet  y-max z-max
);

blocks
(
    hex (0 1 2 3 4 5 6 7) ({Nx} {Ny} {Nz}) simpleGrading (1 1 1)
);

edges
(
    // 4 streamwise corner edges — each traces (x, ±r(x), ±r(x))
    spline 0 1   // y-min z-min
    (
{spline_pts(hs, L, -1, -1)}
    )
    spline 3 2   // y-max z-min
    (
{spline_pts(hs, L, +1, -1)}
    )
    spline 7 6   // y-max z-max
    (
{spline_pts(hs, L, +1, +1)}
    )
    spline 4 5   // y-min z-max
    (
{spline_pts(hs, L, -1, +1)}
    )
);

boundary
(
    inlet
    {{
        type patch;
        faces ( (0 4 7 3) );
    }}
    outlet
    {{
        type patch;
        faces ( (1 2 6 5) );
    }}
    topWall
    {{
        type wall;
        faces ( (3 7 6 2) );
    }}
    bottomWall
    {{
        type wall;
        faces ( (0 1 5 4) );
    }}
    leftWall
    {{
        type wall;
        faces ( (0 3 2 1) );
    }}
    rightWall
    {{
        type wall;
        faces ( (4 5 6 7) );
    }}
);

// ************************************************************************* //
"""

    with open(out_path, "w") as f:
        f.write(bmd)

    print(f"Written [{cr_tag}]: {out_path}")
    print(f"  Inlet {2*R1:.3f}x{2*R1:.3f} m  Outlet {2*R2:.3f}x{2*R2:.3f} m  L {L:.3f} m  dR {dR:.4f} m")
    print(f"  Mesh: {Nx}x{Ny}x{Nz} = {Nx*Ny*Nz:,} cells")
