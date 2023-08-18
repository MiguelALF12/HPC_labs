#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#include "functions/matrixMultiplication.h"

int main(int argc, char *argv[]){
    int size = atoi(argv[1]); // argv[] = ["./code", "10", "verbose"]
    int verbose = 0;

    if (argc == 3 && strcmp(argv[2], "verbose") == 0) {
        verbose = 1;
    }

    multiplyMatrixesV2(&size, &verbose);

    return 0;
}

