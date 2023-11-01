//
// Created by root on 10/30/23.
//
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <omp.h>
#include "needles.h"

typedef struct {
    double x;
    double angle;
    double length;
} Needle;

typedef struct {
    double l; // Distance between the lines
} Floor;


//double randomNumber(double *max){
//    double min = 0.0;
//    double range = (*max - min);
//    double div = RAND_MAX / range;
//    return min + (rand() / div);
//}

/*
 * returns a Needle uniformly distributed in the state space.
 * */
Needle toss_needle(double needle_length, Floor floor){
    double maxLimitForAngle = 1.0;
//    double x = randomNumber(&floor.l) * floor.l;
//    double angle = randomNumber(&maxLimitForAngle) * PI;
    double x = ((double)rand() / RAND_MAX) * floor.l;
    double angle = ((double)rand() / RAND_MAX) * M_PI;
    Needle newNeedle = {x, angle, needle_length};
    return (newNeedle);
}

/*
 * takes a Needle and a Floor as arguments and returns true iff the needle intersects with a line on the floor.
 * */
double cross_line(Needle needle, Floor floor){
    double x_right_tip = needle.x + (needle.length / 2) * sin(needle.angle);
    double x_left_tip = needle.x - (needle.length / 2) * sin(needle.angle);
    return x_right_tip > floor.l || x_left_tip < 0.0;
}

double estimate_prob_needle_crosses_line_secuencial(int nb_tosses, Floor floor, double needle_lenght){
    int nb_crosses = 0;
    Needle needle;
    for(int t = 1; t < nb_tosses; t++){
        needle = toss_needle(needle_lenght, floor);
//        printf("New needle tossed: %f %f\n", needle.x, needle.angle);
        if(cross_line(needle, floor)){
            nb_crosses++;
        }
    }
//    printf("\n\n Number of crosses: %d\n", nb_crosses);
    return (double) nb_crosses / nb_tosses;
}

double estimate_prob_needle_crosses_line_omp(int nb_tosses, Floor floor, double needle_lenght){
    int nb_crosses = 0;
    Needle needle;
    #pragma omp parallel for
    for(int t = 1; t < nb_tosses; t++){
        needle = toss_needle(needle_lenght, floor);
//        printf("New needle tossed: %f %f\n", needle.x, needle.angle);
        if(cross_line(needle, floor)){
            nb_crosses++;
        }
    }
//    printf("\n\n Number of crosses: %d\n", nb_crosses);
    return (double) nb_crosses / nb_tosses;
}


void needle_secuencial(int *nb_tosses) {
    double L = 1.0;// Length of the needle
    Floor floor;
    floor.l = 2.0;  // Distance between the lines

    // Seed the random number generator with the current time
    srand(time(NULL));
    clock_t t;
    t = clock();
    // Estimate the probability that the needle crosses a line
    double probability = estimate_prob_needle_crosses_line_secuencial(*nb_tosses, floor, L);
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds

    // Print the result
    printf("%d:%lf:%6lf:%f\n", *nb_tosses,1/probability, fabs(M_PI - 1/probability) * 100 / M_PI, time_taken);
}


void needle_omp(int *nb_tosses) {
    double start;
    double end;
    double L = 1.0;// Length of the needle
    Floor floor;
    floor.l = 2.0;  // Distance between the lines

    // Seed the random number generator with the current time
    start = omp_get_wtime();
    // Estimate the probability that the needle crosses a line
    double probability = estimate_prob_needle_crosses_line_omp(*nb_tosses, floor, L);
    end = omp_get_wtime();

    printf("%d:%lf:%6lf:%f\n", *nb_tosses,1/probability, fabs(M_PI - 1/probability) * 100 / M_PI, end - start);
}
