#!/usr/bin/env bash

for t in {1..10};
do
  for matrixSize in 10 100 200 400 600 800 1000 2000;
      do
#         ./cmake-build-debug/matrixMultiplication  $matrixSize verbose >> matrixOutputVerboseV2.log
         ./cmake-build-debug/matrixMultiplication $matrixSize >> matrixOutputNotVerboseV2.log
      done
done