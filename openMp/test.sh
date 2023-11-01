#!/usr/bin/bash

exe_matrix_mult_parallel() {
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
#    Anexar condición para ejecutar codigo secuencial
}



secuencial_iteration() {
  for t in {1..10};
    do
      for tosses in 10000 100000 1000000 10000000 100000000 1000000000;
          do
             ./cmake-build-openmp/openMp "$1" $tosses >> pi_approx_exe_results/$2
          done
    done
}

parallel_iteration() {
  for numThread in 5 15 25; do
        export OMP_NUM_THREADS=$numThread
        name="$1_ms_parallel_${numThread}.log"
        for t in {1..10};
        do
          for tosses in 10000 100000 1000000 10000000 100000000 1000000000;
              do
                 ./cmake-build-openmp/openMp "$1" $tosses >> pi_approx_exe_results/$name
              done
        done
      done
}

exe_pi_approx() {
  name=""
  if [ $1 == "dartboard" ]; then
    name="dartboard_ms_secuencial.log"
    secuencial_iteration $1 $name
  elif [ $1 == "needle" ]; then
    name="needle_ms_secuencial.log"
    secuencial_iteration $1 $name
  elif [ $1 == "dartboardP" ]; then
#    Not ready
    parallel_iteration $1
  elif [ $1 == "needleP" ]; then
#    Not ready
    parallel_iteration $1
  fi

}



if [ "$1" == "matrix" ]
then
  echo "Executing Matrix ..."
  if [ "$2" == "omp" ]
  then
    echo "... executing OMP ..."
    exe_matrix_mult_parallel
  else
    echo "... executing Secuencial ..."
    exe_matrix_mult
  fi

elif [ "$1" == "needle" ]
then
  echo "Executing Needles ..."
  if [ "$2" == "omp" ]
  then
    echo "... executing OMP ..."
    exe_pi_approx "needleP"
  else
    echo "... executing Secuencial ..."
    exe_pi_approx "needle"
  fi

elif [ "$1" == "dartboard" ]
then
  echo "Executing Dartboard ..."
  if [ "$2" == "omp" ]
  then
    echo "... executing OMP ..."
    exe_pi_approx "dartboardP"
  else
    echo "... executing Secuencial ..."
    exe_pi_approx "dartboard"
  fi

fi


#name="matrixMult.log"
#for t in {1};
#  do
#    for matrixSize in 1000 2000;
#        do
#           ./cmake-build-openmp/openMp $matrixSize >> $name
#        done
#  done
