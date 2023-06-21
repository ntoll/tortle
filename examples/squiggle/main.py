# Regular turtle code from here...
from turtle import *

color("red")
pensize(3)
speed("fast")

n = 10

for k in range(1, n + 1):
    circle(10 * k, 180)

done()

done()


# PyScript boilerplate here...
from js import document
output = document.createElement("div")
output.innerHTML = svg()
document.body.appendChild(output)
