#include <stdio.h>
#include <stdlib.h>
#include "triangle.h"

int main() {
	int numberRows;
	
	//allow user to input number of rows of triangle
	printf("Enter the number of rows in the triangle: ");
	scanf("%d", &numberRows);
	
	//print triangle
	if (numberRows > 0)
		printTriangle(numberRows, numberRows);
	return 0;
}
