dist:
	sudo apt install python3-venv python3-pip
	python3 -m pip install build
	python3 -m pip install cython
	python3 -m build

install: dist
	python3 -m pip install .

clean:
	rm -rf dist build src/*.egg-info src/binding/binding.c ~/.local/lib/python3.8/site-packages/shishua/ src/shishua/__pycache__/

.PHONY: clean install
