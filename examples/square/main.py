# Regular turtle code from here...
from turtle import *

def square(length=100):
    for i in range(4):
        forward(length)
        right(90)
square()
done()


# PyScript boilerplate here...
from js import document
output = document.createElement("div")
output.innerHTML = svg()
document.body.appendChild(output)
