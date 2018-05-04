#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "conversion.h"

int main() {
	char base;
	int inputNumber;
	
	//allow user to input desired conversion and number to convert
	printf("Enter B for conversion of Binary to Decimal, OR\nEnter D for conversion of Decimal to Binary: ");
	scanf("%c", &base);
	
	printf("Enter your number: ");
	
	//check if input character is invalid
	if ((base != 'B') && (base != 'D')) {
		printf("Invalid input; Goodbye\n");
		return 0;
	}
	
	scanf("%d", &inputNumber);
	
	//carry out and print conversion
	if (base == 'B') {
		printf("%d in binary = %d in decimal\n", inputNumber, convertBase(inputNumber, 2, 10));
	} else {
		printf("%d in decimal = %d in binary\n", inputNumber, convertBase(inputNumber, 10, 2));
	}
	
	return 0;
}
