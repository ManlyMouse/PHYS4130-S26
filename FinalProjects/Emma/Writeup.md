---
meta:
    author: Emma Krebs
    topic: 3D Atmospheric Fluid Simulation using an Eulerian Octree to Model Heat Diffusion
    course: TN Tech PHYS4130
    term: Spring 2026
---

# 3D Atmospheric Fluid Simulation using an Eulerian Octree to Model Heat Diffusion

## Introduction of Atmospheric Modeling and Data Management

-Introduce topic, why we should care/physics of atmospheric modeling, and why different storage of data is important in computational problems. 

## Eulerian Octrees

## Summary of Code

The code is divided into three main files: OctreeFunctions.py, StormFunctions.py, and Main.py. OctreeFunctions contains all the function definitions for the management of the octree and the class object for the spatial nodes. StormFunctions contains two heat equations from different iterations of this project. The first is not a closed system and has fluctuating heat, meaning the initial results were not a conserved system for heat diffusion. The second heat function is the improved iteration that, although not perfect, does maintain a more accurate conserved system then the first. The Main.py imports the previous files, initiates a hot spot somewhere in space, and updates the octree. Additionally, it creates the graphs seen later for measuring octree growth and total heat. 

### OctreeFunctions



### StormFunctions

### Main

## Resulting Animations and Graphs

## Conclusion

-Areas to improve code
-Restate important points of result
-State importance of data management 

## Languages, Libraries, Lessons Learned



## Timekeeping

As of 4/23/26: 38 hours

## Soucres

### Websites

https://en.wikipedia.org/wiki/Octree (Wiki for Octree)
https://www.osti.gov/servlets/purl/1008123#:~:text=Computational%20simulation%20must%20often%20be,the%20mesh%20generation%20code%2C%20CUBIT. (Computational Information for Eulerian Octree)
https://gmd.copernicus.org/articles/17/6401/2024/ (Adapative Mesh Octree)

### Books

An Introduction to Clouds by Lohmann Luond Mahrt



