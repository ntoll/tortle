"""
This script generates the turtle module's top level functions from the classes
in the template_turtle core module.

It then emits a final "turtle.py" module containing the combined core and
top level functions to the build directory in the root of this repository.
"""
import os
import shutil
from template_turtle import *


current_dir = os.path.dirname(os.path.realpath(__file__))
build_dir = os.path.realpath(os.path.join(current_dir, "..", "build"))

with open(os.path.join(current_dir, "template_turtle.py")) as template_file:
    template = template_file.read()

import inspect


def getmethparlist(ob):
    """
    Get strings describing the arguments for the given object

    Returns a pair of strings representing function parameter lists
    including parenthesis.  The first string is suitable for use in
    function definition and the second is suitable for use in function
    call.  The "self" parameter is not included.
    """
    defText = callText = ""
    # bit of a hack for methods - turn it into a function
    # but we drop the "self" param.
    # Try and build one for Python defined functions
    args, varargs, varkw = inspect.getargs(ob.__code__)
    items2 = args[1:]
    realArgs = args[1:]
    defaults = ob.__defaults__ or []
    defaults = ["=%r" % (value,) for value in defaults]
    defaults = [""] * (len(realArgs) - len(defaults)) + defaults
    items1 = [arg + dflt for arg, dflt in zip(realArgs, defaults)]
    if varargs is not None:
        items1.append("*" + varargs)
        items2.append("*" + varargs)
    if varkw is not None:
        items1.append("**" + varkw)
        items2.append("**" + varkw)
    defText = ", ".join(items1)
    defText = "(%s)" % defText
    callText = ", ".join(items2)
    callText = "(%s)" % callText
    return defText, callText


_tg_screen_functions = [
    "addshape",
    "animation",
    "bgcolor",
    "bgpic",
    "bye",
    "clearscreen",
    "colormode",
    "delay",
    "exitonclick",
    "getcanvas",
    "getshapes",
    "listen",
    "mode",
    "numinput",
    "onkey",
    "onkeypress",
    "onkeyrelease",
    "onscreenclick",
    "ontimer",
    "register_shape",
    "resetscreen",
    "save",
    "screensize",
    "setup",
    "setworldcoordinates",
    "svg",
    "textinput",
    "title",
    "tracer",
    "turtles",
    "update",
    "window_height",
    "window_width",
]

_tg_turtle_functions = [
    "back",
    "backward",
    "begin_fill",
    "begin_poly",
    "bk",
    "circle",
    "clear",
    "clearstamp",
    "clearstamps",
    "clone",
    "color",
    "degrees",
    "distance",
    "dot",
    "down",
    "end_fill",
    "end_poly",
    "fd",
    "fillcolor",
    "filling",
    "forward",
    "get_poly",
    "getpen",
    "getscreen",
    "get_shapepoly",
    "getturtle",
    "goto",
    "heading",
    "hideturtle",
    "home",
    "ht",
    "isdown",
    "isvisible",
    "left",
    "lt",
    "onclick",
    "ondrag",
    "onrelease",
    "pd",
    "pen",
    "pencolor",
    "pendown",
    "pensize",
    "penup",
    "pos",
    "position",
    "pu",
    "radians",
    "right",
    "reset",
    "resizemode",
    "rt",
    "seth",
    "setheading",
    "setpos",
    "setposition",
    "settiltangle",
    "setundobuffer",
    "setx",
    "sety",
    "shape",
    "shapesize",
    "shapetransform",
    "shearfactor",
    "showturtle",
    "speed",
    "st",
    "stamp",
    "tilt",
    "tiltangle",
    "towards",
    "turtlesize",
    "undo",
    "undobufferentries",
    "up",
    "width",
    "write",
    "xcor",
    "ycor",
]


module_all = (
    _tg_screen_functions
    + _tg_turtle_functions
    + ["done", "mainloop", "restart", "replay_scene", "Turtle", "Screen"]
)

# The following mechanism makes all methods of RawTurtle and Turtle available
# as functions. So we can enhance, change, add, delete methods to these
# classes and do not need to change anything here.

__func_body = """\
def {name}{paramslist}:
    if {obj} is None:
        {obj} = {init}
    return {obj}.{name}{argslist}

"""

# Emit finalised turtle module.
with open(os.path.join(build_dir, "turtle.py"), "w") as turtle_module:
    turtle_module.write(template)
    turtle_module.write("# The following functions are auto-generated.\n\n")

    def _make_global_funcs(functions, cls, obj, init):
        for methodname in functions:
            try:
                method = getattr(cls, methodname)
            except AttributeError:
                print("methodname missing:", methodname)
                continue
            pl1, pl2 = getmethparlist(method)
            defstr = __func_body.format(
                obj=obj,
                init=init,
                name=methodname,
                paramslist=pl1,
                argslist=pl2,
            )
            turtle_module.write(defstr)

    _make_global_funcs(_tg_turtle_functions, Turtle, "Turtle._pen", "Turtle()")

    _make_global_funcs(
        _tg_screen_functions, Screen, "Turtle.screen", "Screen()"
    )
    turtle_module.write(f"\n__all__ = {module_all}\n")

# Emit svg module.
shutil.copyfile(
    os.path.join(current_dir, "svg.py"), os.path.join(build_dir, "svg.py")
)
