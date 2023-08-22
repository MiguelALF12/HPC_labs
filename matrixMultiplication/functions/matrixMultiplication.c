//
// Created by Miguel Angel Lopez Fernandez on 11/08/23.
//

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "matrixMultiplication.h"


// Using pointers
int randomNumber(){
    int upper = 100, lower = 1;
    int num = (rand() % (upper - lower + 1)) + lower;
    return num;
}

//void fillMatrix(int* matrixPointer, int *size){
//    int(*matrix)[*size] = matrixPointer;
//    int i, j;
//    for (i = 0; i < *size; i++) {
//        for (j = 0; j < *size; j++) {
//            matrix[i][j] = randomNumber();
//        }
//    }
//}

//void printMatrix(int* matrixPointer, int *size, int *verbose, char matrixName ){
//    int (*matrix)[*size] = matrixPointer;
//    int i, j;
//    if(*verbose){
//        printf("The matrix %c is: \n", matrixName);
//        for (i = 0; i < *size; i++) {
//            for (j = 0; j < *size; j++) {
//                printf("%d\t", matrix[i][j]);
//            }
//            printf("\n");
//        }
//    }
//}



//void multiplyMatrixesV2(int *size, int *verbose){
//    int i, j, k;
//
//    srand(time(0));
//    clock_t t;
//    t = clock();
//
//    //random number generation
//    int a[*size][*size], b[*size][*size], axb[*size][*size];
//    fillMatrix(&a, size);
//    printMatrix(&a, size, verbose, 'a');
//    fillMatrix(&b, size);
//    printMatrix(&b, size, verbose, 'b');
//
//    for (i = 0; i < *size; i++) {
//        for (j = 0; j < *size; j++) {
//            axb[i][j] = 0;
//            for (k = 0; k < *size; k++) {
//                axb[i][j] += a[i][k] * b[k][j];
//            }
//        }
//    }
//
//    t = clock() - t;
//    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
//    printMatrix(&axb, size, verbose, 'c');
//    printf("(%d) The multiplication took %f seconds to execute \n", *size,time_taken);
//}


//Not Pointers
void multiplyMatrixesV3(const int *size,const int *verbose){
//    srand(time(0));
    clock_t t;
    t = clock();

    //Dynamic memory allocation
//    int a[*size][*size], b[*size][*size], c[*size][*size], n, i, j, k;
    int n, i, j, k;
    int(*a)[*size][*size] = malloc(sizeof *a);
    int(*b)[*size][*size] = malloc(sizeof *b);
    int(*c)[*size][*size] = malloc(sizeof *c);
    printf("size: %d", *size );


    // Fill the matrix with random numbers
    for (i = 0; i < *size; i++) {
        for (j = 0; j < *size; j++) {
            (*a)[i][j] = randomNumber();
            (*b)[i][j] = randomNumber();
        }
    }
    // Multiply th matrixes
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            (*c)[i][j] = 0;
            for (k = 0; k < n; k++) {
                (*c)[i][j] += (*a)[i][k] * (*b)[k][j];
            }
        }
    }
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds

    // Showing information if verbose
    if(*verbose){
        printf("The matrix a is: \n");
        for (i = 0; i < *size; i++) {
            for (j = 0; j < *size; j++) {
                printf("%d\t", (*a)[i][j]);
            }
            printf("\n");
        }
        printf("The matrix b is: \n");
        for (i = 0; i < *size; i++) {
            for (j = 0; j < *size; j++) {
                printf("%d\t", (*b)[i][j]);
            }
            printf("\n");
        }
        printf("The matrix c is: \n");
        for (i = 0; i < *size; i++) {
            for (j = 0; j < *size; j++) {
                printf("%d\t", (*c)[i][j]);
            }
            printf("\n");
        }
    }

    printf("(%d) The multiplication took %f seconds to execute \n", *size,time_taken);
    free(a);
    free(b);
    free(c);
}

