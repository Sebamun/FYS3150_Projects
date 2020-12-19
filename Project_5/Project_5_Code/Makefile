all: compile1 compile2 compile_test

compile1:	
	c++ -O3 -o run_c.x main_c.cpp Diffusion_solver.cpp -larmadillo -llapack -lblas
compile2:	
	c++ -O3 -o run_d.x main_d.cpp Diffusion_solver.cpp -larmadillo -llapack -lblas

compile_test:
	g++ -o unit_test.exe -Wall Tridiag_test.cpp Diffusion_solver.cpp 