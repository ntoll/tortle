clean:
	rm -rf __pycache__
	rm -rf turtle.py
	rm -rf examples/square/turtle.py
	rm -rf examples/square/svg.py

turtle: clean
	python make_turtle.py

serve: turtle
	cp turtle.py examples/square/turtle.py
	cp svg.py examples/square/svg.py
	python -m http.server
