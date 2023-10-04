//
// Created by Miguel Angel Lopez Fernandez on 27/09/23.
//

#include "dartboard.h"

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <pthread.h>
#define MAX_THREADS 5 //number of threads

//typedef struct {
//    long n;
//    long hits;
//    double thread_time;
//} ThreadData;

typedef struct {
    int thread_id;
    int tosses;
    int hits;
    double thread_time;

} ThreadDataV2;

int monte_carlo(int *tosses, void* arg) {
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

    // %p to print void* pointer
    if(arg == NULL){
        double pi_approx = 4.0 * hits / *tosses;
        // Significa que estamos ejecutando el secuencial
        printf("%d:%.6lf:%.6lf:%.6lf\n", *tosses, pi_approx, fabs(M_PI - pi_approx) * 100 / M_PI, time_taken);
    }else{
        // Significa que estamos ejecutando el paralelo, con hilos
        ThreadDataV2 * data = (ThreadDataV2*) arg;
//        printf("Received threadid in monteCarloFunc: %d\n", data->thread_id);
        data->hits = hits;
        data->thread_time = time_taken;
//        printf("%d:%.6lf\n", data->thread_id, time_taken);
    }
    return 0;
}


// V1: Parallel
/*
void* monte_carlo_parallel_threads(void* arg) {
    ThreadData* data = (ThreadData*) arg;
    long n = data->n;
    long hits = 0;

    const double factor = 1.0 / RAND_MAX;

    srand((int)time(NULL));

    clock_t thread_start_time = clock();

    for (long k = 0; k < n; ++k) {
        double x = rand() * factor;
        double y = rand() * factor;
        if (x * x + y * y < 1.0) {
            ++hits;
        }
    }

    clock_t thread_end_time = clock();
    double thread_time_taken = ((double)(thread_end_time - thread_start_time)) / CLOCKS_PER_SEC; // Tiempo del hilo en segundos

    data->hits = hits;
    data->thread_time = thread_time_taken;

    pthread_exit(NULL);
}

int monte_carlo_parallel(int *tosses) {

    pthread_t* threads = malloc(MAX_THREADS * sizeof(pthread_t));
    ThreadData* thread_data = malloc(MAX_THREADS * sizeof(ThreadData));

    clock_t t;
    t = clock();

    for (int i = 0; i < MAX_THREADS; ++i) {
        thread_data[i].n = *tosses / MAX_THREADS;
        pthread_create(&threads[i], NULL, monte_carlo_parallel_threads, &thread_data[i]);
    }

    for (int i = 0; i < MAX_THREADS; ++i) {
        pthread_join(threads[i], NULL);
    }

    int total_hits = 0;
    double total_thread_time = 0.0;

    for (int i = 0; i < MAX_THREADS; ++i) {
        total_hits += thread_data[i].hits;
        total_thread_time += thread_data[i].thread_time;
    }

    double pi_approx = 4.0 * total_hits / *tosses;
    t = clock() - t;
    double time_taken = ((double)t) / CLOCKS_PER_SEC; // Tiempo total de ejecución en segundos

    printf("Approximation of pi after %d tosses: %.6lf (error = %.6lf%%). Total execution time: %.6lf seconds\n", *tosses, pi_approx, fabs(M_PI - pi_approx) * 100 / M_PI, time_taken);

    for (int i = 0; i < MAX_THREADS; ++i) {
        printf("Thread %d execution time: %.6lf seconds\n", i, thread_data[i].thread_time);
    }

    free(threads);
    free(thread_data);

    return 0;
}
 */


// V2: Parallel
void* monte_carlo_thread(void* arg) {
    ThreadDataV2 * data = (ThreadDataV2 *)arg;
    int tosses = data->tosses;
    monte_carlo(&tosses,arg);
    pthread_exit(NULL);
}


int monte_carlo_threads(int *tosses) {

    pthread_t threads[MAX_THREADS];
    ThreadDataV2 thread_data[MAX_THREADS];

    for (int i = 0; i < MAX_THREADS; ++i) {
        thread_data[i].thread_id = i;
        thread_data[i].tosses = *tosses / MAX_THREADS;
        thread_data[i].hits = 0;
        thread_data[i].thread_time=0.0;
        pthread_create(&threads[i], NULL, monte_carlo_thread, &thread_data[i]);
    }

    for (int i = 0; i < MAX_THREADS; ++i) {
        pthread_join(threads[i], NULL);
    }

    int total_hits = 0;
    double total_thread_time = 0.0;

    for (int i = 0; i < MAX_THREADS; ++i) {
        total_hits += thread_data[i].hits;
        total_thread_time += thread_data[i].thread_time;
    }

    double pi_approx = (4.0 * total_hits) / (*tosses);

    double avg_time = total_thread_time/(double) MAX_THREADS;
    printf("%d:%.6lf:%.6lf:%.6lf\n", *tosses, pi_approx, fabs(M_PI - pi_approx) * 100 / M_PI, avg_time);

    return 0;
}
