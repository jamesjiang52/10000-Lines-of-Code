#include <stdio.h>
#include <stdlib.h>
#include "operate.h"

int main() {
	double firstNumber, secondNumber;
	char operation;
	
	//allow user to input two numbers and desired operation
	printf("Enter first number: ");
	scanf("%lf", &firstNumber);
	printf("Enter second number: ");
	scanf("%lf%*c", &secondNumber);
	printf("Enter calculation command (one of a, s, m, or d): ");
	scanf("%c", &operation);
	
	operate(operation, firstNumber, secondNumber);
	
	return 0;
}
