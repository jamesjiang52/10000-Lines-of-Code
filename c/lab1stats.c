#include "stats.h"

double mean(double *numbers, int size) {
	/*
	Returns the mean of an array of numbers
	*/
	double sum = 0.0;
	for (int i = 0; i < size; i++) {
		sum += numbers[i];
	}
	return sum/size;
}

double stdDev(double *numbers, int size) {
	/*
	Returns the standard deviation of an array of numbers
	*/
	double sumDeviation = 0.0;
	double mean_ = mean(numbers, size);
	for (int i = 0; i < size; i++) {
		sumDeviation += pow(numbers[i] - mean_, 2);
	}
	double stdDev = sqrt(sumDeviation/(size - 1));
	return stdDev;
}
