---
title: "Nozzle"
date: 2026-06-09
author: ["Nam Kyun Kang"]
description: "Nozzle wind tunnel experiment"
summary: "Nozzle wind tunnel experiment"
showToc: true
wight : 2
---

# Overview
The design trade off studies have been completed using OpenFOAM. Pressure drop along the nozzle, boundary layer thickness, and flow uniformity were used to evaluate each designs. Most important consideration is space, the overall length of the tunnel has to be between 2-3 m. Since the test section will be 0.6 m long that means there are 1.4 - 2.4 m of space for both nozzle and diffuser combined. 
The following shows the parameters that has to be determined:
+ Contraction ratio, 6-9
+ Curvature
+ Length; length will be about the size of the inlet of the nozzle
## Preliminary CFD Studies
Before the design studies are conducted, I have to determine the numerical model as well as the mesh suitable for the simulation. Because the geometry is rather simple, I will be using blockMesh and validate my simulation setup using an experimental data. This [paper](https://www.sciencedirect.com/science/article/abs/pii/S0167610500000805) by Fang et.al titled "Experimental and analytical evaluation of flow in a square-to-square wind tunnel contraction" provides exactly what I need to make sure my setup is physical. 
![](Fan_Nozzle.png)
Experimental setup: 
+ Contraction ratio of 9
+ Inlet: 2.4 x 2.4 m
+ Outlet: 0.8 x 0.8 m
+ $V_{outlet}$ = 15 m/s
+ $Re$ = 764,000 
+ Surface pressure is measured along the mid plane of each surfaces

The Reynolds number is about 4 times greater, but the flow should behave relatively the same. 

### Numerical Setup
Structured hexahedral mesh is used for this nozzle simulation. OpenFOAM has its own structured mesh generator called blockMesh and it is quite useful when dealing with simple geometries. You can also add curvature via spline command as displayed below. The spline is connecting the vertices 0 and 1 together with prescribed coordinates.  


```cpp
edges(
    spline 0 1
    (
        (x1 y1 z1)
        (x2 y2 z2)
        (x3 y3 z3)
     )
)
```
There is only one block for the nozzle and you can make your block using hex. It helps when you draw out the geometry beforehand with all the vertices labeled. This will help you follow the right-hand rule and I connect the vertices looking down from the z-plane. So the mesh has 200 elements along x direction and 300 in y. I just divided the mesh in two different zones and added half of the elements in each zones. The spacing is 1/500. I think the distance between the cells are determined using the geometric series. 

```cpp
blocks(
    hex (0 1 2 3 4 5 6 7) // 
    (200 300 1)
    simpleGrading( 1 
                    ((5 3 500) (5 3 0.002))   
                    1 )
)
```
<!--
{{<vtk file="/vtk/duct.vtp" wireframe="true" colorBy="U" title="Mesh" >}}*/
-->
![](Mesh.png)
The number of elements in the mesh shown above is 60,000 and it is just here to illustrate the type of mesh that can be generated using blockMesh. I've used ICEMCFD before to make structured mesh and it is quite similar apart from the lack of graphical interface.

I originally wanted to use 2D simulation to save time, but it turns out that is not the right choice. I guess the curvature of the nozzle creates a strong secondary flow inside and creates a flow field that cannot be quite explained using only two coordinates. 
![](comparison.png)

I will conclude that the current setup is adequate for the nozzle design and the same setup will be used later for the diffuser as well. 




