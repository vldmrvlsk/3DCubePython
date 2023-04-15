from vpython import *
ourbox = box(color=vector(0, 0.33, 1),
             opacity = 0.7,
             shininess = 0.5,
             emissive = False)
dx = 0.01
while True:
    rate(1/dx)
    ourbox.rotate(angle=1*dx, axis=vector(0,1,0))