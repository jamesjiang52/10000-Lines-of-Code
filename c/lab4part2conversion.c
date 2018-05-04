#include "conversion.h"

int convertBase(int numberToConvert, int oldBase, int newBase) {
	/*
	Converts the base of numberToConvert from oldBase to newBase
	*/
	int outputNumber = 0;
	int place = 0;
	while (numberToConvert) {
		outputNumber += pow(oldBase, place)*(numberToConvert % newBase);
		numberToConvert /= newBase;
		place += 1;
	}
	return(outputNumber);
}
