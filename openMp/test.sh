#!/usr/bin/bash

for numThread in 5 15 25; do
  export OMP_NUM_THREADS=$numThread
  name="matrixMultOMP_${numThread}.log"
  for t in {1..10};
  do
    for matrixSize in 300 600 900 1200 1500 1800 2100 2400 2700 3000;
        do
           ./cmake-build-openmp/openMp $matrixSize >> thirdLoop/$name
        done
  done

done

#name="matrixMult.log"
#for t in {1};
#  do
#    for matrixSize in 1000 2000;
#        do
#           ./cmake-build-openmp/openMp $matrixSize >> $name
#        done
#  done
