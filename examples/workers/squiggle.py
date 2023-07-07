import turtle
import random


for i in range(32):
    turtle.forward(random.randint(1, 200))
    turn = random.randint(0, 180)
    if random.choice([True, False]):
        turtle.right(turn)
    else:
        turtle.left(turn)

turtle.Screen().show_scene()
result = turtle.svg()

from xworker import xworker

document = xworker.window.document
container = document.createElement("div")
document.body.appendChild(container)
container.innerHTML = result
