---
title: "Requirements, Specs and Preliminary Thoughts"
date: 2026-05-09
author: ["Nam Kyun Kang"]
description: "Wind tunnel design specs and constraints"
summary: "Specs and design constraints for building an open loop wind tunnel"
showToc: false
weight: 1
---

## Preliminary Thoughts

Wind tunnel is one of those things that I have used in the past and familiar with, but actual construction of one is a bit daunting. One of the work stream that I did was creating a virtual wind tunnel for correlation work. I have experience with a closed-loop open jet wind tunnel for automotive applications. Boundary layer management system, moving ground as well as nozzle/collector geometry is quite important for these tunnels and the results changes quite a bit if one of them is altered in anyway. Wind tunnel is a facinating tools at our disposal and I would be a very happy man if I can just test different things in the tunnel to see what happens. I don't think I will have enough money to commission a tunnel any time soon, but I think I can create a "good enough" wind tunnel for my own personal projects.

There are many kinks that must be worked out. As an aerodynamics engineer I am quite comfortable with creating the overall design of the tunnel by using CFD, but the actual fabrication of the tunnel is a daunting task. I've also used pressure scanners many times before, but I've never created one from scratch and I will have to create one from scratch considering how expensive it is to buy on off the shelf. I am lucky enough to have been to a wind tunnel to know what is required for the application I have in mind. 

The size of the tunnel as well will be determined by choosing the geometry of the test articles. The project should be done in this order:

1. Determine maximum width, height and length of the test article
2. Test section geometry based on #1
3. Maximum speed of the tunnel
4. Contraction ratio of the nozzle
5. diffuser geometry according to available axial fan
6. What will be measured?
    + air speed
    + surface pressure
    + force
7. DAQ schematic and hardware
8. Fan controller 
9. How will the tunnel be contructed?
10. How to tackle noise and vibration of the fan?

I am sure more will come up as the project moves forward, but for now this is what I have to go off with. 

## Constraints:
### Test Section
The immediate contraint is space, if I had a ton of realstate. I want the tunnel to fit in a garage so it should not exceed the length of 3 m. The test section will be 30 cm by 30 cm which means a 1:12 scale model can be tested inside. The blockage ratio will be about 17% which is acceptable for me. The test section length should be about 0.5 - 3 times the hydraulic diameter of the test section according to Barlow due to the wake. I will just create the length to be 2 times the diameter, which comes out to 60 cm. 
### Nozzle
The contraction ratio should be between 6-10 and the length of the nozzle has to be approximately the same as the hydraulic diamter of the nozzle inlet according to Metha. I will conduct some CFD study to figure out the most realistic size for me. Flow uniformity and pressure drop will be monitored. There is also a fifth order polynomial that I can use to determine the shape of the nozzle. 
### Diffuser
Diffuser is there to recover some pressure to reduce resistance. The goal is to keep the flow attached, some simualtion I did in the past showed that anything above 6 degrees was quite bad. I will do some more simulation to figure it out. Nozzle length has to be sorted out first for me to be able to design the diffuser. 
###











