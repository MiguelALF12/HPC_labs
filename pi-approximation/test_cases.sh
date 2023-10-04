#!/usr/bin/env bash

name=""

if [ $1 == "montecarlo" ]; then
  name="montecarlo_measures_secuencial.log"
elif [ $1 == "needle" ]; then
  name="needle_measures_secuencial.log"
elif [ $1 == "montecarloP" ]; then
  name="montecarlo_measures_parallel.log"
elif [ $1 == "needleP" ]; then
  name="needle_measures_parallel.log"
fi

for t in {1..10};
do
  for tosses in 10000 100000 1000000 10000000 100000000 1000000000;
      do
         ./cmake-build-debug/pi_approximation "$1" $tosses >> "$name"
      done
done
