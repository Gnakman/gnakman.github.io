---
title: "Wind Tunnel CFD"
date: 2026-06-09
author: ["Nam Kyun Kang"]
description: "Wind Tunnel CFD and characteristics"
summary: "CFD analysis of Nozzle, Test Section, and Diffuser combination "
showToc: false
math: true
weight: 4
cover:
    image: "Pressure_Tunnel.png"
    alt: "Surface Pressure"
    relative: true
---

## Wind tunnel Physics

It is quite important to understand the characteristics of the wind tunnel in order to properly understand the result obtained from it. Knowing the flow field inside of the tunnel will also let me position sensors and test rigs in appropriate locations. For now I just employed RANS simulation using k-e turbulence model. Two variables that I looked into are streamwise velocity profiles and axial pressure distribution. 

The velocity profiles will let me understand how boundary layer grown from the tunnel may affect the result and also shed some light on how high the ground plane must be installed. Axial pressure gradient is also important since it will have direct impact on any force measured inside of the tunnel. 

I am only aware of the corrections they do for automotive tunnels which are oftentimes an open-jet tunnel. My tunnel will be a closed-jet tunnel so the blockage will have a greater influence on the model since the dynamic pressure will change more as air accelerates if the blockage is big enough. I will have to read up on how aerospace wind tunnels are operated since my knowledge is a bit limited. 

### Pressure Distribution

![](Cp_streamwise.png)
![](Cp_test_section.png)
![](dCp_dx_test_section.png)
![](Ux_profiles.png)
























