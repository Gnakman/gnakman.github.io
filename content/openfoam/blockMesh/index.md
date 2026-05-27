---
title: "blockMesh"
date: 2025-05-26
description: "A line-by-line guide to blockMeshDict — the structured mesh generator in OpenFOAM."
summary: "Learn how to build structured hexahedral meshes for OpenFOAM using blockMesh, explained from the FoamFile header all the way to boundary patches."
showToc: true
TocOpen: true
disableAnchoredHeadings: false
---
{{< vtk file="/vtk/test.vtp" colorBy="p" title="My simulation" >}}


## What is blockMesh?

`blockMesh` is OpenFOAM's built-in structured mesh generator. Instead of importing a mesh
from an external tool, you describe the geometry and topology of your mesh directly inside
a plain-text dictionary file called `blockMeshDict`, located at:

```
<case>/system/blockMeshDict
```

`blockMesh` reads this file and writes the resulting mesh into `<case>/constant/polyMesh/`.
The mesh is made up of **hexahedral blocks** — each block has eight vertices, twelve edges,
and six faces. You can join multiple blocks together to represent more complex shapes.

---

## A minimal blockMeshDict

Below is a complete `blockMeshDict` for a simple rectangular domain
(a box of 1 m × 0.1 m × 0.1 m with 20 cells in x, 1 in y, 1 in z).
Every section is explained line by line.

```cpp
/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2312                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      blockMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

scale   1;

vertices
(
    (0   0   0  )   // 0 — back-bottom-left
    (1   0   0  )   // 1 — back-bottom-right
    (1   0.1 0  )   // 2 — back-top-right
    (0   0.1 0  )   // 3 — back-top-left
    (0   0   0.1)   // 4 — front-bottom-left
    (1   0   0.1)   // 5 — front-bottom-right
    (1   0.1 0.1)   // 6 — front-top-right
    (0   0.1 0.1)   // 7 — front-top-left
);

blocks
(
    hex (0 1 2 3 4 5 6 7)   // vertex connectivity
        (20 1 1)             // cell count: (x y z)
        simpleGrading (1 1 1) // uniform grading
);

edges
(
    // No curved edges — leave empty for straight edges
);

boundary
(
    inlet
    {
        type patch;
        faces
        (
            (0 4 7 3)   // left face (x = 0)
        );
    }

    outlet
    {
        type patch;
        faces
        (
            (1 2 6 5)   // right face (x = 1)
        );
    }

    topAndBottom
    {
        type wall;
        faces
        (
            (0 1 5 4)   // bottom face (y = 0)
            (3 7 6 2)   // top face    (y = 0.1)
        );
    }

    frontAndBack
    {
        type empty;     // 2-D: suppress solution in z-direction
        faces
        (
            (0 3 2 1)   // back  face (z = 0)
            (4 5 6 7)   // front face (z = 0.1)
        );
    }
);

// ************************************************************************* //
```

---

## Line-by-line explanation

### File header

```cpp
/*--------------------------------*- C++ -*----------------------------------*\
...
\*---------------------------------------------------------------------------*/
```

This is a block comment (`/* ... */`). OpenFOAM files always start with this
banner — it is cosmetic and is ignored by the parser. The `-*- C++ -*-` tag
tells editors like Emacs to apply C++ highlighting.

---

### FoamFile

```cpp
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      blockMeshDict;
}
```

Every OpenFOAM dictionary begins with a `FoamFile` sub-dictionary.
OpenFOAM reads this to identify the file before parsing the rest.

| Key | Meaning |
|---|---|
| `version` | File-format version. Always `2.0`. |
| `format` | `ascii` (human-readable) or `binary` (faster for large meshes). |
| `class` | The C++ class that will parse this file. `dictionary` is used for all text config files. |
| `object` | The name of the file — must match the actual filename (`blockMeshDict`). |

---

### scale

```cpp
scale   1;
```

A global scaling factor applied to **every** vertex coordinate.
Use `scale 0.001` if your coordinates are in millimetres and you want metres,
or `scale 25.4` to convert inches to millimetres (combined with a unit system).

---

### vertices

```cpp
vertices
(
    (0   0   0  )   // 0 — back-bottom-left
    (1   0   0  )   // 1 — back-bottom-right
    ...
);
```

A list of 3-D coordinates that define the corners of your blocks.
Each vertex is referenced later by its **zero-based index** (the first vertex
listed is vertex 0, the second is vertex 1, and so on).

> **Tip:** Add a comment on each line with the index and a human-readable label.
> Debugging is much harder without them.

---

### blocks

```cpp
blocks
(
    hex (0 1 2 3 4 5 6 7)
        (20 1 1)
        simpleGrading (1 1 1)
);
```

This is where you define the topology — how the vertices connect into hexahedral
(six-face) blocks.

| Part | Meaning |
|---|---|
| `hex` | Block shape: hexahedron. This is the only supported type in most OpenFOAM versions. |
| `(0 1 2 3 4 5 6 7)` | The eight vertex indices of this block, listed in the right-hand-rule order (see diagram below). |
| `(20 1 1)` | Number of cells in the **x**, **y**, **z** directions of this block. |
| `simpleGrading (1 1 1)` | Cell size ratio between the last and first cell in each direction. `1` = uniform spacing. Use `> 1` to cluster cells towards the end of an edge. |

**Vertex ordering inside a block:**

```
    7 ---- 6
   /|     /|
  4 ---- 5 |
  | 3 ---| 2
  |/     |/
  0 ---- 1
```

Vertices 0–3 form the "back" face (lower z), vertices 4–7 form the "front" face
(higher z). The ordering must follow the **right-hand rule** so that
face normals point outward — getting this wrong produces negative-volume cells.

---

### edges

```cpp
edges
(
);
```

Optional curved edges. If left empty (as here), all edges are straight lines
between vertices. You can use `arc`, `spline`, or `polyLine` entries here to
create cylindrical or arbitrary-curve geometries.

---

### boundary

```cpp
boundary
(
    inlet
    {
        type patch;
        faces
        (
            (0 4 7 3)
        );
    }
    ...
);
```

Defines the named patches that appear in `0/` boundary conditions.
Each patch needs:

| Key | Meaning |
|---|---|
| `type patch` | Generic boundary — no special physics. Use for inlets, outlets, symmetry planes, etc. |
| `type wall` | Triggers wall functions in turbulence models. |
| `type empty` | Suppresses solution in that direction — required for 2-D simulations (one cell thick in z). |
| `type symmetryPlane` | Applies a symmetry condition. |
| `faces` | List of four vertex indices (in counter-clockwise order when viewed from outside) that define each face on this patch. |

> **Important:** Every face on the outer boundary of your mesh **must** appear in
> exactly one patch. Missing faces cause `checkMesh` to report open boundaries.
> Duplicate faces cause topology errors.

---

## Running blockMesh

From your case directory:

```bash
blockMesh
```

Then check the mesh quality:

```bash
checkMesh
```

Look for:
- **Max non-orthogonality** < 70° (ideally < 40°)  
- **Max skewness** < 4  
- Zero cells with negative volume

---

## Next steps

- **Grading**: Change `simpleGrading (4 1 1)` to stretch cells towards the outlet — useful for boundary layer resolution.
- **Multiple blocks**: Add more `hex` entries to the `blocks` list and share vertices at their interfaces.
- **Curved edges**: Use `arc` in the `edges` section to mesh cylinders.
