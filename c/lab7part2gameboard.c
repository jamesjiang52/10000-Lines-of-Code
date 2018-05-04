#include "gameboard.h"

void printGameBoard(int boardSize, char **gameBoard) {
	/*
	Prints current game board
	*/
	printf("  ");
	for (int i = 0; i < boardSize; i++) {
		printf("%c", 'a' + i);
	}
	printf("\n");
	
	for (int row = 0; row < boardSize; row++) {
		printf("%c ", 'a' + row);
		for (int col = 0; col < boardSize; col++) {
			printf("%c", gameBoard[row][col]);
		}
		printf("\n");
	}
}

void updateGameBoard(char row, char col, char player, char **gameBoard) {
	/*
	Updates game board in position (row, col) with player character
	*/
	gameBoard[row - 'a'][col - 'a'] = player;
}

int getCount(int boardSize, char player, char **gameBoard) {
	/*
	Counts the number of occurences of player in gameBoard
	*/
	int count = 0;
	
	for (int row = 0; row < boardSize; row++) {
		for (int col = 0; col < boardSize; col++) {
			if (gameBoard[row][col] == player)
				count += 1;
		}
	}
	return(count);
}
