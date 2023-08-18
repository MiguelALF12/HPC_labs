//
// Created by Miguel Angel Lopez Fernandez on 11/08/23.
//

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "matrixMultiplication.h"

int randomNumber(){
    int upper = 100, lower = 1;
    int num = (rand() % (upper - lower + 1)) + lower;
    return num;
}

void fillMatrix(int* matrixPointer, int *size){
    int(*matrix)[*size] = matrixPointer;
    int i, j;
    for (i = 0; i < *size; i++) {
        for (j = 0; j < *size; j++) {
            matrix[i][j] = randomNumber();
        }
    }
}

void printMatrix(int* matrixPointer, int *size, int *verbose, char matrixName ){
    int (*matrix)[*size] = matrixPointer;
    int i, j;
    if(*verbose){
        printf("The matrix %c is: \n", matrixName);
        for (i = 0; i < *size; i++) {
            for (j = 0; j < *size; j++) {
                printf("%d\t", matrix[i][j]);
            }
            printf("\n");
        }
    }
}



void multiplyMatrixesV2(int *size, int *verbose){
    int i, j, k;

    srand(time(0));
    clock_t t;
    t = clock();

    //random number generation
    int a[*size][*size], b[*size][*size], axb[*size][*size];
    fillMatrix(&a, size);
    printMatrix(&a, size, verbose, 'a');
    fillMatrix(&b, size);
    printMatrix(&b, size, verbose, 'b');

    for (i = 0; i < *size; i++) {
        for (j = 0; j < *size; j++) {
            axb[i][j] = 0;
            for (k = 0; k < *size; k++) {
                axb[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printMatrix(&axb, size, verbose, 'c');
    printf("(%d) The multiplication took %f seconds to execute \n", *size,time_taken);
}




