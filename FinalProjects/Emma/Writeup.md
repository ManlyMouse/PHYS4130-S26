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

The code is divided into three main files: OctreeFunctions.py, StormFunctions.py, and Main.py. OctreeFunctions contains all the function definitions for the management of the octree and the class object for the spatial nodes. StormFunctions contains two heat equations from different iterations of this project. The first is not a closed system and has fluctuating heat, meaning the initial results were not a conserved system for heat diffusion. The second heat function is the improved iteration that, although not perfect, does maintain a more accurate conserved system then the first. The Main.py imports the previous files, initiates a hot spot somewhere in space, and updates the octree. Additionally, it creates the graphs seen later for measuring octree growth and total heat. Main.py was ran three times with a maximum octree depth of 3, 4, and 5, meaning they could not subdivide past that depth. 

### OctreeFunctions



### StormFunctions

There are two heat diffusion functions within this file: diffuse and diffuse_conservation. Diffuse is the first iteration of the code 

### Main

## Resulting Animations and Graphs

There are various animations and graphs resulting from this project. We will beging with the first iteration of the project where the heat diffusion was not conserved. We can see the following three animations for n=3, n=4, n=5:



## Conclusion

There are many areas to improve with this code to create a better atmospheric model. Although they were not implemented here, various additional storm functions could be added without much change to Main.py and OctreeFunctions.py to make a much more accurate model. Some of the possible additional charactersitics involved with storms (some of which were previously mentioned in the introduction) are vorticity, wind speed, and pressure. Although these would help achieve the original intent of this project, it was decided to focus on heat diffusion because of three reasons: 1) time constraint, 2) measurability and consistency, and 3) node borders. 

The last two in particular drove this decision. Heat diffusion is a much simpler process to check consistency of because it is simply the flow of heat between boxes, so checking if its conserved as it flows is much easier then wind velocity where you have to check directions on top of the scalar intensity. Additonally, a major issue with this method of octrees is the neighbors. Any particular node may have more neighbors on one edge of its spatial size then another, making storing and accounting for fluxes much more difficult to keep track of. This code would be moreso an approximation of heat diffusion since it either averages neighbors on a side or simply chooses one as a representation. Therefore, strange behaviors can emerge as seen in the previous section heat_conservation function. The diffusion appears to favor growth in the vertical direction (similar problem to the diffusion example!), which may be due to the number of nodes in a region of space. The direction of spread may favor more nodes. 

In summary, 

-Areas to improve code
-Restate important points of result
-Retate importance of data management 

## Languages, Libraries, Lessons Learned

This project let me investigate data structures and the very tip of the iceberg for atmospheric modeling/fluid dynamics. I was able to read some really cool papers of people's attempts on improving these simulations (seen in sources) and how data structures contribute to a good model. In particular, adapative octrees let me practice a type of data organization using object classes which I haven't been able to use since CS 1310. Getting to revisit that was fun. However, the adaptability also increased the difficulty, so although this was a computational physics project it definietely favoured the computation aspect. Most of the timekeeping was dedicated to constructing the octree and bug fixing the node updates and trying to figure out the adaptability. A semi-new library I used was matplotlib's patches, which was mostly there to help me visualize the octree adapting. 

## Timekeeping

As of 5/31/26: 44 hours

## Soucres

### Websites

https://en.wikipedia.org/wiki/Octree (Wiki for Octree)

https://www.osti.gov/servlets/purl/1008123#:~:text=Computational%20simulation%20must%20often%20be,the%20mesh%20generation%20code%2C%20CUBIT. (Computational Information for Eulerian Octree)

https://gmd.copernicus.org/articles/17/6401/2024/ (Adapative Mesh Octree)

### Books

An Introduction to Clouds by Lohmann Luond Mahrt



