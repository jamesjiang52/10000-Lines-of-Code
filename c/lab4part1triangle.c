#include "triangle.h"

void printSpaces(int numSpaces) {
	/*
	Prints numSpaces amount of spaces
	*/
	while (numSpaces-->0)
		printf(" ");
}

void printTriangle(int row, int totalRows) {
	/*
	Recursively prints rows of the triangle with totalRows rows
	*/
	//recursion base case, print top of triangle
	if (row == 1) {
		printSpaces(totalRows - row);
		printf("^\n");
		return;
	}
	
	//last row of triangle
	if (row == totalRows) {
		printTriangle(row - 1, totalRows); //print triangle above last row
		for (int i = 0; i < 2*totalRows - 1; i++)
			printf("^");
		printf("\n");
		return;
	}
	
	//rows between first and last rows
	printTriangle(row - 1, totalRows); //print triangle above current row
	printSpaces(totalRows - row);
	printf("^");
	printSpaces(2*row - 3);
	printf("^\n");
}
