cmake_minimum_required(VERSION 3.25)
project(openMp C)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_COMPILER /usr/bin/gcc-13)    # Set this to the path of your GCC C compiler
set(CMAKE_VERBOSE_MAKEFILE ON)
add_executable(openMp main.c matrixMultiplication/matrixMultiplication.c matrixMultiplication/matrixMultiplication.h pi_approx/dartboard/dartboard.c pi_approx/dartboard/dartboard.h pi_approx/needles/needles.c pi_approx/needles/needles.h)

find_package(OpenMP)
if(OpenMP_C_FOUND)
    target_link_libraries(openMp PUBLIC OpenMP::OpenMP_C m)
endif()
