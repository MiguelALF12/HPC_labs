//
// Created by Miguel Angel Lopez Fernandez on 13/10/23.
//

#ifndef OPENMP_MATRIXMULTIPLICATION_H
#define OPENMP_MATRIXMULTIPLICATION_H

void multiplyMatrixesSecuencial(const int *size,const int *verbose);
void multiplyMatrixesOmp(const int *size,const int *verbose);
int review_omp_threads (void);
#endif //OPENMP_MATRIXMULTIPLICATION_H
