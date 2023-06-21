clean:
	rm -rf __pycache__
	rm -rf turtle.py
	rm -rf examples/square/turtle.py
	rm -rf examples/square/svg.py
	rm -rf examples/squiggle/turtle.py
	rm -rf examples/squiggle/svg.py

turtle: clean
	python make_turtle.py

serve: turtle
	cp turtle.py examples/square/turtle.py
	cp svg.py examples/square/svg.py
	cp turtle.py examples/squiggle/turtle.py
	cp svg.py examples/squiggle/svg.py
	python -m http.server
