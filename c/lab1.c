#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "stats.h"

int main() {
	//set number of numbers that user inputs
	const int NUMBER_VALUES = 3;
	double inputNumbers[NUMBER_VALUES];

	//allow user to input numbers
	printf("Enter three numbers: "); //must change number according to NUMBER_VALUES
	for (int i = 0; i < NUMBER_VALUES; i++) {
		scanf("%lf", &inputNumbers[i]);
	}
    
	double mean_ = mean(inputNumbers, NUMBER_VALUES);
	double stdDev_ = stdDev(inputNumbers, NUMBER_VALUES);
	
	printf("The mean is %.2lf and the standard deviation is %.2lf\n", mean_, stdDev_);
    
	return 0;
}
