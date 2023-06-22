clean:
	rm -rf __pycache__
	rm -rf turtle.py
	rm -rf src/__pycache__/*
	rm -rf build/*

turtle: clean
	python src/make_turtle.py

serve: turtle
	python -m http.server
