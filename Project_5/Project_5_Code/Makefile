all: compile1 compile2 compile_test

compile1:	
	c++ -O3 -o run.x main.cpp Diffusion_solver.cpp -larmadillo -llapack -lblas
compile2:	
	c++ -O3 -o run2.x main_d.cpp Diffusion_solver.cpp -larmadillo -llapack -lblas

compile_test:
	g++ -o unit_test.exe -Wall Tridiag_test.cpp Diffusion_solver.cpp 