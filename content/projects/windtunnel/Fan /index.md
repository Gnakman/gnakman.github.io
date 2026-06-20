---
title: "Fan"
date: 2026-06-20
author: ["Nam Kyun Kang"]
description: "Fan Selection"
summary: "Calculating overall pressure drop inside of the tunnel for fan selection"
showToc: false
math: true
weight: 5
---

## Fans 
Two primary types of fan typically used are axial fan and centrifugal fan. They both move air, but centrifugal fans are more suitable for this project since it is designed to move high volume of air with greater resistance. Axial fans are commonly used to cool objects inside of an electronic or a car whereas centrifugal fans are oftentimes installed inside of a building to move air through a duct. Below is a figure summarizing the two obtained from [here](https://www.fansco.com/news/what-is-the-difference-between-centrifugal-and-axial-fan/).

![](Fan_type.png)

### Fan Performance Curve
Each fan can be characterized using a fan performance curve which tells you how much air it can move given its RPM and static pressure. 


There are many kinks that must be worked out. As an aerodynamics engineer I am quite comfortable with creating the overall design of the tunnel by using CFD, but the actual fabrication of the tunnel is a daunting task. I've also used pressure scanners many times before, but I've never created one from scratch and I will have to create one from scratch considering how expensive it is to buy off the shelf. I am lucky enough to have been to a wind tunnel to know what is required for the application I have in mind. 



![](schematic.png)

|Part #|Name|Description|Spec|
|---|---|---|---|
|1| Honey Comb |Reduce turbulence and increases flow uniformity|TBD|
|2| Nozzle |Accelerates flow and conditions flow|6-10 contraction|
|3| Test Section |Test object and instrumentation|25x25x56 cm|
|4| Diffuser|Enables pressure recovery|TBD|
|5| Fan|Draws flow into the tunnel|~2000 cfm or 10 m/s|
## General Rule of Thumb
A design guide for a wind tunnel can be found in chapter 3 of this [book]("https://web.pdx.edu/~d4eb/chrome/J._B._Barlow,_W._H._Rae,_Jr,_A._Pope_Low_Speed_Wind_Tunnel_Testing.pdf") by J.Barlow, W.Rae, Jr, and A.Pope
### Test Section
* Length of the section has to be at least 2 times the hydraulic diameter,  
$D_{h} = 2(A_{cross}/\pi)^{0.5}$. 
*  $w\times h\times  l = 0.25\times 0.25\times 0.56 m$

Other parameter based its geometry on the test section and preliminary sizing study showed 0.25 m is a good length if I want to limit the total length of the tunnel to be less than 3 m.
### Nozzle
* Contraction ratio, $CR_{Nozzle}$ must be between 6-9
* Length of the nozzle is $\approx D_{h}$ of the nozzle
<div style="width: fit-content; margin: auto; text-align: center">

| $CR_{Nozzle}$| $W$ & $H$ (m)|$L$ (m)|
|---|---|---|
|6| 0.612 |0.691|
|6.5| 0.637 |0.719|
|7| 0.661  |0.746|
|7.5| 0.685|0.772|
|8| 0.707|0.798|
|8.5| 0.729 |0.822|
|9| 0.750  |0.846|

</div>
The curvature of the nozzle can be derived from a Bell-Metha 5th order polynomial equation:  
$$
y = a_{1}\xi^{5}+a_{2}\xi^{4}+a_{3}\xi^{3}+a_{4}\xi^{2}+a_{5}\xi+C
$$
where $\xi=x/L_{nozzle}$

### Diffuser
Diffuser is there to recover some pressure to reduce resistance. The goal is to keep the flow attached, some simulation I did in the past showed that anything above 6 degrees was quite bad. I will do some more simulation to figure it out. Nozzle length has to be sorted out first for me to be able to design the diffuser. 
### Maximum Speed
A radiator fan will be used to draw the air into the nozzle from the diffuser. The range will be between 10-20 m/s, which means that the fan should move 0.9 - 1.8 cubic meter of air per second or around 2000-4000 cfm. Realistically, the maximum speed of the tunnel will be 10 m/s unless I can design an add-on that contracts the flow even more. The Reynolds number based on the hydraulic diameter of the test section is $1.9\times(10^{5})$. 










