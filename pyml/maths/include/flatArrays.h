//
// Created by Gil Ferreira Hoben on 10/11/17.
//
#include <Python.h>


#ifndef PYML_DEV_FLATARRAYS_H
#define PYML_DEV_FLATARRAYS_H

#ifdef __cplusplus
extern "C" {
#endif

class flatArray {
private:
    int rows;
    int cols;
    int size;
    double *array;

public:
    flatArray() {
        array = nullptr;
        rows = 0;
        cols = 0;
        size = 0;
    };
    ~flatArray() {
        delete [] array;
        array = nullptr;
    };

    void readFromPythonList(PyObject *pyList);
    void startEmptyArray(int rows_, int cols_);

    int getRows();
    int getCols();
    void setRows(int r);
    void setCols(int c);
    int getSize();

    double* getArray();

    double getElement(int row, int col);
    void setElement(double value, int row, int col);

    double getNElement(int n);
    void setNElement(double value, int n);

    double* getRow(int i);
    double* getCol(int j);
    void setRow(double *row, int i);

    flatArray* transpose();
    double sum();
    flatArray *dot(flatArray *other);
    flatArray *subtract(flatArray *other);
    flatArray *power(int p);
    flatArray *divide(double m);
};

#ifdef __cplusplus
}
#endif

#endif //PYML_DEV_FLATARRAYS_H
