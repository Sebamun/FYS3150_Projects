all: compilec compiled compile2d compileg compile_test

compilec:
	c++ -O3 -o run_c.x main_c.cpp Diffusion_solver.cpp -larmadillo -llapack -lblas

compiled:
	c++ -O3 -o run_d.x main_d.cpp Diffusion_solver.cpp -larmadillo -llapack -lblas

compile2d:
	c++ -O3 -o run2d.x main2d.cpp Diffusion_solver.cpp -larmadillo -llapack -lblas

compileg:
	c++ -O3 -o run_g.x main_g.cpp Diffusion_solver.cpp -larmadillo -llapack -lblas

compile_test:
	g++ -o unit_test.exe -Wall Tridiag_test.cpp Diffusion_solver.cpp
