#include "coinamounts.h"

void coinAmounts(int inputAmount) {
	/*
	Prints the coins needed to make inputAmount with the least number of coins
	*/
	int coins[4] = {25, 10, 5, 1};
	char *coinNamesSingular[4] = {"quarter", "dime", "nickel", "cent"};
	char *coinNamesPlural[4] = {"quarters", "dimes", "nickels", "cents"};
	int seenFirstCoin = 0;
	
	int currentAmount = inputAmount;
	printf("%d cents: ", inputAmount);
	
	//iterate through all coin types from greatest to smallest value
	for (int coinIndex = 0; coinIndex < 4; coinIndex++) {
		//check if remaining value is larger than coin value
		if (currentAmount/coins[coinIndex]) { 
			if (seenFirstCoin) //determine whether or not to print comma
				printf(", ");

			seenFirstCoin = 1;
			
			//print number of times coin amount can be subtracted from remaining amount
			printf("%d ", currentAmount/coins[coinIndex]);
			
			//determine whether to print singular or plural version of coin name
			printf("%s", (currentAmount/coins[coinIndex] == 1) ? coinNamesSingular[coinIndex] : coinNamesPlural[coinIndex]);
			
			//calculate remaining amount
			currentAmount %= coins[coinIndex];
		}
	}
	
	printf(".\n");
}
