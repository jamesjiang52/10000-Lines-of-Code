#include <stdio.h>
#include <stdlib.h>
#include "triangle.h"

int main() {
	//keep looping until input is invalid
	while(1) {
		int numberRows = 0;
		
		//allow user to input number of rows
		printf("Enter the number of rows: ");
		scanf("%d", &numberRows);
		
		if (numberRows < 0) //check if input is invalid
			return 0;
		if (!numberRows) //check if input is larger than 0
			continue;
		
		//print triangle
		triangle(numberRows - 1, numberRows - 1);
	}
}
