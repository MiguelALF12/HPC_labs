//#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "functions/matrixMultiplication.h"

int main(int argc, char *argv[]){
    const int size = strtol(argv[1], NULL, 10);
    int verbose = 0;

    if (argc == 3 && strcmp(argv[2], "verbose") == 0) {
        verbose = 1;
    }

    multiplyMatrixesV3(&size, &verbose);

    return 0;
}

