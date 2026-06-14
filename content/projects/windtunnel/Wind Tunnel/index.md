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
    image: ""
    alt: "Surface Pressure"
    relative: true
---

## Diffuser Geometry & CFD Results

Diffuser helps with pressure recovery as the flow expands and the velocity of the fluid slows down. Greater pressure recovery will reduce the amount of power for the fan to displace air. It is not as important as the nozzle, but it is nevertheless an important part of a wind tunnel that must be designed with care. 

The expansion ratio, ER of the diffuser should be between 2-3 and the angle must be between 2-3.5. I summarized the dimension of the diffuser below and included a bit more aggressive angle since that would reduce the length. The outlet dimension has been calculated first:

|ER|w & h (m)|
|---|---|
|2| 0.353 |
|2.5| 0.395 |
|3| 0.433 |

From the outlet geometry, the length of the diffuser can now be calculated. There are total of 15 cases that has been identified and further CFD analysis was run. 

|Angle|ER 2|ER 2.5|ER 3|
|---|---|---|---|
|2.5| 1.188 m | 1.667 m|2.010 m|
|3.0| 0.990 m | 1.389 m|1.750 m|
|3.5| 0.849 m | 1.191 m|1.501 m|
|4.0| 0.743 m|1.043 m|1.314 m|
|5.0| 0.595 m|0.835 m|1.052 m|

Pressure drop is calculated by 0.9L - 0.1L and the result is shown in the figure below. 

![](pressure_drop.png)

The difference between Ratio 2.5 and 3 is minimal except when flow separates which occurs at 5 degrees. I want the diffuser to be as shortest as possible without compromising too much on performance. This leaves me with:

* Angle = 3.5, Expansion Ratio = 2, dP = 28.8 Pa, L = 0.849 m

The difference between best performing diffuser and my chosen case is about 2 Pa, but the length is almost three times greater. The extra pressure recovery is not worth all that space to me. 

Velocity magnitude and kinematic pressure contours are shown below for the chosen geometry.
![](CR2_35_p.png)
Since the outlet is a specified to be atmospheric, the pressure there is 0 for all cases. I call it a pressure outlet which implies that, but maybe some people call it something else. The change in geometry just alters the pressure upstream and pressure gradient along the diffuser. 
![](CR2_35_U_mag.png)
You can see the boundary layer growing much quickly as the flow slows down. I'd want to avoid the that area when I eventually place the fan. The difference of the incoming flow condition along the blade might cause stall or degradation of fan performance. It will also generate more noise. 

















