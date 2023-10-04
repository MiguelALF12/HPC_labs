#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <pthread.h>

#define PI 3.14159265358979323846
#define MAX_THREADS 5 //number of threads

typedef struct {
    double x;
    double angle;
    double length;
} Needle;

typedef struct {
    double l; // Distance between the lines
} Floor;

typedef struct {
    int thread_id;
    int nb_tosses;
    Floor floor;
    double needle_length;
    double probability;
    double thread_time;
} ThreadData;


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
    /*
     *  x = rand() * floor.ℓ
     *  θ = rand() * π
     *  return Needle(x, θ, L)
     */
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
    /*
     * x_right_tip = needle.x + needle.L / 2 * sin(needle.θ)
     * x_left_tip  = needle.x - needle.L / 2 * sin(needle.θ)
     * return x_right_tip > floor.ℓ || x_left_tip < 0.0*/
    double x_right_tip = needle.x + (needle.length / 2) * sin(needle.angle);
    double x_left_tip = needle.x - (needle.length / 2) * sin(needle.angle);
    return x_right_tip > floor.l || x_left_tip < 0.0;
}

double estimate_prob_needle_crosses_line(int nb_tosses, Floor floor, double needle_lenght){
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

void needle(int *nb_tosses) {
    double L = 1.0;// Length of the needle
    Floor floor;
    floor.l = 2.0;  // Distance between the lines

    // Seed the random number generator with the current time
    srand(time(NULL));
    clock_t t;
    t = clock();
    // Estimate the probability that the needle crosses a line
    double probability = estimate_prob_needle_crosses_line(*nb_tosses, floor, L);
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds

    // Print the result
    printf("%d:%lf:%6lf:%f\n", *nb_tosses,1/probability, fabs(M_PI - 1/probability) * 100 / M_PI, time_taken);
}

void* needle_thread(void* arg) {
    ThreadData* data = (ThreadData*)arg;

    srand(time(NULL));
    clock_t t;
    t = clock();

    // Estimate the probability that the needle crosses a line
//    printf("received thread: %d %d %f %f\n",data->thread_id, data->nb_tosses, data->floor.l, data->needle_length);
    double probability = estimate_prob_needle_crosses_line(data->nb_tosses, data->floor, data->needle_length);
    data->probability = probability;

    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds

    // Print the result
//    printf("%d:%f:%6lf\n", data->thread_id, probability, time_taken);
    data->thread_time = time_taken;
    pthread_exit(NULL);
}

int needle_threads(int *tosses) {

    pthread_t threads[MAX_THREADS];
    ThreadData thread_data[MAX_THREADS];

    for (int i = 0; i < MAX_THREADS; i++) {
        thread_data[i].thread_id = i;
        thread_data[i].nb_tosses = *tosses / MAX_THREADS;
        thread_data[i].floor.l = 2.0;
        thread_data[i].needle_length = 1.0;
//        printf("Given thread: %d %d %f %f\n",thread_data[i].thread_id ,thread_data[i].nb_tosses, thread_data[i].floor.l, thread_data[i].needle_length);
        pthread_create(&threads[i], NULL, needle_thread, &thread_data[i]);
    }

    for (int i = 0; i < MAX_THREADS; i++) {
        pthread_join(threads[i], NULL);
//        printf("Thread %d: Estimated probability = %f\n", i, thread_data[i].probability);
    }
    double total_probability = 0;
    double total_thread_time = 0.0;
    double total_pi_approx_bythread = 0.0;
    for (int i = 0; i < MAX_THREADS; ++i) {
        total_probability += thread_data[i].probability;
        total_thread_time += thread_data[i].thread_time;
        total_pi_approx_bythread += (2/thread_data[i].probability)*(thread_data[i].needle_length/thread_data[i].floor.l);
    }
    double avg_probability = total_probability/(double) MAX_THREADS;
    double avg_time = total_thread_time/(double) MAX_THREADS;
    double avg_pi_approx = total_pi_approx_bythread/(double) MAX_THREADS;
    printf("%d:%.6lf:%6lf:%.6lf\n", *tosses, 1/avg_probability, fabs(M_PI - 1/avg_probability) * 100 / M_PI,avg_time);
    return 0;
}


