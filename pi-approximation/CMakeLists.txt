cmake_minimum_required(VERSION 3.25)
project(pi_approximation C)

set(CMAKE_C_STANDARD 17)

add_executable(pi_approximation main.c dartboardAlgo/dartboard.c dartboardAlgo/dartboard.h needle/needle.c needle/needle.h)
