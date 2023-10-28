#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <omp.h>
#include <ctype.h>
#include "matrixMultiplication/matrixMultiplication.h"

int main(int argc, char *argv[]){
    const int size = strtol(argv[1], NULL, 10);
    int verbose = 0;

    if (argc == 3 && strcmp(argv[3], "verbose") == 0) {
        verbose = 1;
    }
//    multiplyMatrixesSecuencial(&size, &verbose);
    multiplyMatrixesOmp(&size, &verbose);
//    review_omp_threads();

    return 0;
}