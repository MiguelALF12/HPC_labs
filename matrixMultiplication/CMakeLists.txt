cmake_minimum_required(VERSION 3.25)
project(matrixMultiplication C)

set(CMAKE_C_STANDARD 99)

add_executable(matrixMultiplication main.c functions/matrixMultiplication.c)
