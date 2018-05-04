#include "operate.h"

void operate(char operation, double firstNumber, double secondNumber) {
	/*
	Determines desired operation and carries it out
	*/
	switch(operation) {
		//addition
		case 'a':
			printf("Sum of %.2lf and %.2lf is %.2lf\n", firstNumber, secondNumber, firstNumber + secondNumber);
			return;
			
		//subtraction	
		case 's':
			printf("Difference of %.2lf from %.2lf is %.2lf\n", firstNumber, secondNumber, firstNumber - secondNumber);
			return;
		
		//multiplication
		case 'm':
			printf("Product of %.2lf and %.2lf is %.2lf\n", firstNumber, secondNumber, firstNumber*secondNumber);
			return;
		
		//division
		case 'd':
			//check if division by zero
			if (secondNumber) {
				printf("Division of %.2lf by %.2lf is %.2lf\n", firstNumber, secondNumber, firstNumber/secondNumber);
				return;
			}
			printf("Error, trying to divide by zero\n");
			return;
		
		//if operation character isn't a, s, m, or d
		default:
			printf("Error, unknown calculation command given\n");
			return;
	}	
}
