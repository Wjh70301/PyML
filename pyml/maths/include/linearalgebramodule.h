//
// Created by Gil Ferreira Hoben on 06/11/17.
//
#include <Python.h>

#ifndef SRC_LINEARALGEBRAMODULE_H
#define SRC_LINEARALGEBRAMODULE_H

#ifdef __cplusplus
extern "C" {
#endif

void matrixVectorDotProduct(double** A, double* v, int ASize, int VSize, double* result);
double vectorSum(const double* array, int rows);
void matrixTranspose(double** X, double** result, int rows, int cols);
void vectorPower(double* A, int pPower, int ASize, double* result);
void vectorSubtract(const double* u, const double* v, int size, double* result);
void matrixMatrixProduct(double** A, double** B, int ASize, int BSize, double** result);
void leastSquares(double** X, double* y, double* theta, int n, int m);
void vectorDivide(double* X, int n, int size);

#ifdef __cplusplus
}
#endif

#endif //SRC_LINEARALGEBRAMODULE_H
