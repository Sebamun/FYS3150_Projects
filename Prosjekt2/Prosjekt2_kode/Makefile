all: compile execute1 execute2

compile:	
	c++ -O3 -o Tridiag.x main.cpp jacobi.cpp -larmadillo -llapack -lblas

execute1:
	python3 run.py 0

execute2:
	python3 run.py 1

