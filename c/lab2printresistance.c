#include "printresistance.h"

void printResistance(char firstBand, char secondBand, char multiplier, char tolerance) {
	/*
	Determines and prints resistor information, including tolerance
	*/
	//determine resistance and tolerance
	double resistorValue = colorCodeValue(firstBand)*pow(10, colorCodeValue(multiplier) + 1) + colorCodeValue(secondBand)*pow(10, colorCodeValue(multiplier));
	double resistorTolerance = colorCodeTolerance(tolerance);
	
	//determine names of input colors
	char *firstBandColor = colorCodeName(firstBand);
	char *secondBandColor = colorCodeName(secondBand);
	char *multiplierColor = colorCodeName(multiplier);
	char *toleranceColor = colorCodeName(tolerance);

	printf("Resistor bands: %s %s %s %s\n", firstBandColor, secondBandColor, multiplierColor, toleranceColor);
    
	//adjust and print output according to order of magnitude
	if (resistorValue < 1000.0) {
		printf("Resistance: %.2lf Ohms +/- %.2lf%%\n", resistorValue, resistorTolerance);
	} else if (resistorValue < 1000000.0) {
		double outputValue = resistorValue/1000.0;
		printf("Resistance: %.2lf KOhms +/- %.2lf%%\n", outputValue, resistorTolerance);
	} else {   
		double outputValue = resistorValue/1000000.0;
		printf("Resistance: %.2lf MOhms +/- %.2lf%%\n", outputValue, resistorTolerance);
	}
}
