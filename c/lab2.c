#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include "colorcodes.h"
#include "printresistance.h"

int main() {
	char firstBand, secondBand, multiplier, tolerance;

	//allow user to input resistor colors as characters
	printf("Please enter the 1st band: \n");
	scanf("%c%*c", &firstBand);
	printf("Please enter the 2nd band: \n");
	scanf("%c%*c", &secondBand);
	printf("Please enter the multiplier band: \n");
	scanf("%c%*c", &multiplier);
	printf("Please enter the tolerance band: \n");
	scanf("%c", &tolerance);
	
	printResistance(firstBand, secondBand, multiplier, tolerance);

	return 0;
}
