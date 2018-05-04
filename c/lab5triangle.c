#include "triangle.h"

void printSpaces(int numSpaces) {
	/*
	Prints numSpaces amount of spaces
	*/
	while (numSpaces-->0)
		printf(" ");
}

int *triangle(int row, int numRows) {
	/*
	Recursively prints rows of Pascal's triangle with numRows rows and returns an array of the numbers in the row-th row
	*/
	//recursion base case, print one 1 at top of triangle
	if (!row) {
		printSpaces(3*numRows);
		printf("1\n");
		int rowNums[1] = {1};
		return rowNums;
	}
	
	int *rowNums = malloc((row + 1)*sizeof(int)); //array to store numbers in current row
	
	//determine and print previous row
	int *previousRow = triangle(row - 1, numRows);
	rowNums[0] = 1;
	rowNums[row] = 1;
	
	//calculate numbers in current row
	for (int i = 1; i < row; i++) {
		rowNums[i] = previousRow[i - 1] + previousRow[i];
	}
	
	//print each number in the row
	for (int i = 0; i <= row; i++) {
		int number = rowNums[i];
		
		//print spaces for offsetting the row
		if (!i)
			printSpaces(3*(numRows - row));
		
		printf("%-6d", number);
	}
	printf("\n");
	
	return rowNums;
}
