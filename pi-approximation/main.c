#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "dartboardAlgo/dartboard.h"
#include "needle/needle.h"


int main(int argc, char *argv[]) {

    int tosses = strtol(argv[2], NULL, 10);

    if (argc == 3){
        if (strcmp(argv[1],"montecarlo") == 0) {
//            printf("tosses:measure:error:time\n");
            monte_carlo(&tosses, NULL);
        }
        else if(strcmp(argv[1],"needle") == 0){
//            printf("tosses:measure:error:time");
            needle(&tosses);
        }
        else if(strcmp(argv[1],"montecarloP") == 0){
//            monte_carlo_parallel(&tosses);
//            printf("tosses:pi_approximation:error:time\n");
            monte_carlo_threads(&tosses);
        }
        else if(strcmp(argv[1],"needleP") == 0){
//            printf("tosses:measure:error:time");
            needle_threads(&tosses);
        }
    }
    else{
        printf("Not enough args");
    }
    return 0;

}
