#include "colorcodes.h"

int colorCodeValue(char color) {
	/*
	Takes a character corresponding to a color as input and returns its value
	*/
	char colorLowerCase = tolower(color);
	switch(colorLowerCase) {
		case 'k': return 0;
		case 'b': return 1;
		case 'r': return 2;
		case 'o': return 3; 
		case 'e': return 4;
		case 'g': return 5;
		case 'u': return 6;
		case 'v': return 7;
		case 'y': return 8;
		case 'w': return 9;
		case 'l': return -1;
		case 's': return -2;
	}
}

double colorCodeTolerance(char color) {
	/*
	Takes a character corresponding to a color as input and returns its tolerance percent
	*/
	char colorLowerCase = tolower(color);
	switch(colorLowerCase) {
		case 'b': return 1.0;
		case 'r': return 2.0;
		case 'g': return 0.5;
		case 'u': return 0.25;
		case 'v': return 0.10;
		case 'y': return 0.05;
		case 'l': return 5.0;
		case 's': return 10.0;
	}
}

char *colorCodeName(char color) {
	/*
	Takes a character corresponding to a color as input and returns its color name
	*/
	char colorLowerCase = tolower(color);
	switch(colorLowerCase) {
		case 'k': return "Black";
		case 'b': return "Brown";
		case 'r': return "Red";
		case 'o': return "Orange";
		case 'e': return "Yellow";
		case 'g': return "Green";
		case 'u': return "Blue";
		case 'v': return "Violet";
		case 'y': return "Grey";
		case 'w': return "White";
		case 'l': return "Gold";
		case 's': return "Silver";
	}
}
