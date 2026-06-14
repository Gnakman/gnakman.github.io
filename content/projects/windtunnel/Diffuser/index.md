---
title: "Diffuser"
date: 2026-06-09
author: ["Nam Kyun Kang"]
description: "General Overview"
summary: "Specs and design constraints for building an open loop wind tunnel"
showToc: false
math: true
weight: 3
---

## Diffuser Geometry

Diffuser helps with pressure recovery as the flow expands and the velocity of the fluid slows down. Greater pressure recovery will reduce the amount of power for the fan to displace air. It is not as important as the nozzle, but it is nevertheless an important part of a wind tunnel that must be designed with care. 

The expansion ration of the diffuser should be between 2-3 and the angle must be between 2-3.5. I summarized the dimension of the diffuser below and included a bit more aggressive angle since that would reduce the length. The outlet dimension has been calculated first:

|Ratio|w & h (m)|
|---|---|
|2| 0.353 |
|2.5| 0.395 |
|3| 0.433 |

From the outlet geometry, the length of the diffuser can now be calculated. There are total of 15 cases that has been identified and further CFD analysis was run. 

|Angle|Ratio 2|Ratio 2.5|Ratio 3|
|---|---|---|---|
|2.5| 1.188 m | 1.667 m|2.010 m|
|3.0| 0.990 m | 1.389 m|1.750 m|
|3.5| 0.849 m | 1.191 m|1.501 m|
|4.0| 0.743 m|1.043 m|1.314 m|
|5.0| 0.595 m|0.835 m|1.052 m|















