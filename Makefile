clean:
	rm -rf __pycache__
	rm -rf turtle.py
	rm -rf examples/square/turtle.py
	rm -rf examples/square/svg.py
	rm -rf examples/squiggle/turtle.py
	rm -rf examples/squiggle/svg.py
	rm -rf build/*

turtle: clean
	python src/make_turtle.py

serve: turtle
	python -m http.server
