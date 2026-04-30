---
meta:
    author: Emma Krebs
    topic: 3D Atmospheric Fluid Simulation using an Eulerian Octree to Model Supercell Formation
    course: TN Tech PHYS4130
    term: Spring 2026
---

# 3D Atmospheric Fluid Simulation using an Eulerian Octree to Model Supercell Formation

-Introduce topic, why we should care/physics of atmospheric modeling, and why different storage of data is important in computational problems. 


## Theory of Storm Formation

### Storms and Longevity 

-Talk about storms and what factors go into their formation and longevity ie why longer storms happen
-What are the main parameters we should worry about (temperature, pressure, vorticity, and velocity)

[Image of storm longevity from book source]

### Vorticity 
-Huge section with PDEs, poisson's solution, and more. Mostly math section

## Summary of Code
-Really basic overview of code, like what you did with diffusion. Lead into data

### Data Storage 

-Talk about Eulerian Octree -- why did you choose Eulerian over lagrangian. Why did you decide to do an octree (neighbor lookup/quicker access to important information)
-Information about your node and cell classes. 

### Important Function Definitions (Updaters)

### Main.py

## Results

### Produced Animation

[Animations for a couple different storm formations]

### Numerical Comparison

Important results:

-maximum vorticity magnitude
-updraft velocity peak
-spatial storm radius over time

-storm intensity growth rate
-structural stability
-simulated longevity

## Conclusion

-Areas to improve code
-Restate important points of result
-State importance of data management 

### 

## Languages, Libraries, Lessons Learned

The main language was python and I used the libraries numpy, matplotlib, and os. I developed my skills with using objects and classes in python and creating images and animations for aggregations. In particular, I learned how to use the os to more effectively store the .gifs and .pngs. I also learned how to do octrees, but they unfortunately did not end up working for this particular program (but they might be useful for my project over the summer!). On that note, ignore the Code_Graveyard. It is filled with ghosts of past aggregate lives. 

## Timekeeping

As of 4/23/26: 36 hours

## Soucres

### Websites

https://en.wikipedia.org/wiki/Octree (Wiki for Octree)
https://www.osti.gov/servlets/purl/1008123#:~:text=Computational%20simulation%20must%20often%20be,the%20mesh%20generation%20code%2C%20CUBIT. (Computational Information for Eulerian Octree)
https://gmd.copernicus.org/articles/17/6401/2024/ (Adapative Mesh Octree)

### Books

An Introduction to Clouds by Lohmann Luond Mahrt



