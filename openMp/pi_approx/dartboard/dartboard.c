//
// Created by root on 10/30/23.
//
#include "dartboard.h"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <omp.h>

int monte_carlo_secuencial(int *tosses) {
    int k, hits = 0;
    const double factor = 1.0 / RAND_MAX;

    srand((int)time(NULL));
    clock_t t;
    t = clock();
    for (k = hits = 0; k < *tosses; ++k) {
        double x = rand() * factor;
        double y = rand() * factor;
        if (x * x + y * y < 1.0) {
            ++hits;
        }
    }
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds

    double pi_approx = 4.0 * hits / *tosses;
    // Significa que estamos ejecutando el secuencial
    printf("%d:%.6lf:%.6lf:%.6lf\n", *tosses, pi_approx, fabs(M_PI - pi_approx) * 100 / M_PI, time_taken);

    return 0;
}

int monte_carlo_omp(int *tosses) {
    int k, hits = 0;
    const double factor = 1.0 / RAND_MAX;
    double start;
    double end;

    start = omp_get_wtime();
    #pragma omp parallel for
    for (k = hits = 0; k < *tosses; ++k) {
        double x = rand() * factor;
        double y = rand() * factor;
        if (x * x + y * y < 1.0) {
            ++hits;
        }
    }

    double pi_approx = 4.0 * hits / *tosses;
    end = omp_get_wtime();

    printf("%d:%.6lf:%.6lf:%.6lf\n", *tosses, pi_approx, fabs(M_PI - pi_approx) * 100 / M_PI, end - start);

    return 0;
}


