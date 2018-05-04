#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "coinamounts.h"

int main() {
	int inputAmount;
	
	//continue asking for input until input is invalid
	while (1) {
		//allow user to input coin amount
		printf("Please give an amount in cents less than 100: ");
		scanf("%d", &inputAmount);
		
		//stop if input is invalid
		if (inputAmount > 99 || inputAmount < 1) {
			printf("Goodbye.\n");
			return 0;
		}
		
		coinAmounts(inputAmount);
	}
}
