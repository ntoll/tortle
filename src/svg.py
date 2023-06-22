# Modified version of Brython's SVG module
# Author: Romain Casati
# License: GPL v3 or higher

from js import document


_svg_ns = "http://www.w3.org/2000/svg"
_xlink_ns = "http://www.w3.org/1999/xlink"


def _tag_func(tag):
    def func(*args, **kwargs):
        global COUNTER
        node = document.createElementNS(_svg_ns, tag)
        # this is mandatory to display svg properly
        if tag == "svg":
            node.setAttribute("xmlns", _svg_ns)
        for arg in args:
            if isinstance(arg, (str, int, float)):
                arg = document.createTextNode(str(arg))
            node.appendChild(arg)
        for key, value in kwargs.items():
            key = key.lower()
            if key[0:2] == "on":
                # Event binding passed as argument "onclick", "onfocus"...
                # Better use method bind of DOMNode objects
                node.addEventListener(key[2:], value)
            elif key == "style":
                node.setAttribute(
                    "style", ";".join(f"{k}: {v}" for k, v in value.items())
                )
            elif "href" in key:
                node.setAttributeNS(_xlink_ns, "href", str(value))
            elif value is not False:
                # option.selected=false sets it to true :-)
                node.setAttribute(key.replace("_", "-"), str(value))
        return node

    return func


a = _tag_func("a")
altGlyph = _tag_func("altGlyph")
altGlyphDef = _tag_func("altGlyphDef")
altGlyphItem = _tag_func("altGlyphItem")
animate = _tag_func("animate")
animateColor = _tag_func("animateColor")
animateMotion = _tag_func("animateMotion")
animateTransform = _tag_func("animateTransform")
circle = _tag_func("circle")
clipPath = _tag_func("clipPath")
color_profile = _tag_func("color_profile")
cursor = _tag_func("cursor")
defs = _tag_func("defs")
desc = _tag_func("desc")
ellipse = _tag_func("ellipse")
feBlend = _tag_func("feBlend")
foreignObject = _tag_func("foreignObject")
g = _tag_func("g")
image = _tag_func("image")
line = _tag_func("line")
linearGradient = _tag_func("linearGradient")
marker = _tag_func("marker")
mask = _tag_func("mask")
path = _tag_func("path")
pattern = _tag_func("pattern")
polygon = _tag_func("polygon")
polyline = _tag_func("polyline")
radialGradient = _tag_func("radialGradient")
rect = _tag_func("rect")
set = _tag_func("set")
stop = _tag_func("stop")
svg = _tag_func("svg")
text = _tag_func("text")
tref = _tag_func("tref")
tspan = _tag_func("tspan")
use = _tag_func("use")
