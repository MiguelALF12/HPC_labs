#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <omp.h>
#include <ctype.h>
#include "matrixMultiplication/matrixMultiplication.h"
#include "pi_approx/dartboard/dartboard.h"
#include "pi_approx/needles/needles.h"

int exe_matrixes_mult(int argc, char *argv[]){
    const int size = strtol(argv[1], NULL, 10);
    int verbose = 0;

    if (argc == 3 && strcmp(argv[3], "verbose") == 0) {
        verbose = 1;
    }
    multiplyMatrixesSecuencial(&size, &verbose);
//    multiplyMatrixesOmp(&size, &verbose);
//    review_omp_threads();

    return 0;
}

int exe_api_approx(int argc, char *argv[]){

    if (argc == 3){
        int tosses = strtol(argv[2], NULL, 10);

        if (strcmp(argv[1],"dartboard") == 0) {
//            printf("tosses:measure:error:time\n");
            monte_carlo_secuencial(&tosses);
        }
        else if(strcmp(argv[1],"needle") == 0){
//            printf("tosses:measure:error:time");
            needle_secuencial(&tosses);
        }
        else if(strcmp(argv[1],"dartboardP") == 0){
//            monte_carlo_parallel(&tosses);
//            printf("tosses:pi_approximation:error:time\n");
            monte_carlo_omp(&tosses);
        }
        else if(strcmp(argv[1],"needleP") == 0){
//            printf("tosses:measure:error:time");
            needle_omp(&tosses);
        }
    }
    else{
        printf("Not enough args");
    }
    return 0;
    return 0;
}

int main(int argc, char *argv[]){
//    exe_matrixes_mult(argc, argv);
    exe_api_approx(argc, argv);
    return 0;
}