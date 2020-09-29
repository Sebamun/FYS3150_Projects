all: compile execute

compile:	
	c++ -O3 -o Tridiag.x main.cpp jacobi.cpp -larmadillo -llapack -lblas

execute:
	./Tridiag.x Output Output_2 Output_3