from xworker import XWorker

for i in range(10):
    sync = XWorker("squiggle.py", config="turtle.toml", type="micropython")
