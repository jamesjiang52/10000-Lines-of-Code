#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "gameboard.h"
#include "moves.h"

int main() {
	int boardSize = 0;
	
	printf("Enter the board dimension: ");
	scanf("%d", &boardSize);
	
	//allocate memory for game board
	char **gameBoard;
	gameBoard = (char**) malloc(boardSize*sizeof(char*));
	for (int row = 0; row < boardSize; row++) {
		gameBoard[row] = (char*) malloc(boardSize*sizeof(char));
	}
	
	//allocate memory for allowed moves
	int **WMoves;
	WMoves = (int**) malloc(boardSize*sizeof(int*));
	for (int row = 0; row < boardSize; row++) {
		WMoves[row] = (int*) malloc(boardSize*sizeof(int));
	}
	
	int **BMoves;
	BMoves = (int**) malloc(boardSize*sizeof(int*));
	for (int row = 0; row < boardSize; row++) {
		BMoves[row] = (int*) malloc(boardSize*sizeof(int));
	}
	
	//initialize game board and allowed moves
	for (int row = 0; row < boardSize; row++) {
		for (int col = 0; col < boardSize; col++) {
			gameBoard[row][col] = 'U';
			WMoves[row][col] = 0;
			BMoves[row][col] = 0;
		}
	}
	
	gameBoard[boardSize/2 - 1][boardSize/2 - 1] = 'W';
	gameBoard[boardSize/2][boardSize/2] = 'W';
	gameBoard[boardSize/2 - 1][boardSize/2] = 'B';
	gameBoard[boardSize/2][boardSize/2 - 1] = 'B';
	
	printGameBoard(boardSize, gameBoard);
	
	printf("Enter board configuration:\n");
	char inputSequence[3] = "Uaa";
	
	//read in and apply input until !!! is seen
	do {
		updateGameBoard(inputSequence[1], inputSequence[2], inputSequence[0], gameBoard);
		scanf("%s%*c", inputSequence);
	} while (strcmp(inputSequence, "!!!"));
	
	printGameBoard(boardSize, gameBoard);
	
	getMoves(boardSize, 'W', gameBoard, WMoves);
	getMoves(boardSize, 'B', gameBoard, BMoves);

	//print allowed moves for White and Black
	printf("Available moves for W: \n");
	for (int row = 0; row < boardSize; row++) {
		for (int col = 0; col < boardSize; col++) {
			if (WMoves[row][col])
				printf("%c%c\n", 'a' + row, 'a' + col);
		}
	}
	
	printf("Available moves for B: \n");
	for (int row = 0; row < boardSize; row++) {
		for (int col = 0; col < boardSize; col++) {
			if (BMoves[row][col])
				printf("%c%c\n", 'a' + row, 'a' + col);
		}
	}
	
	//user inputs a move
	char inputMove[3];
	printf("Enter a move:\n");
	scanf("%s%*c", inputMove);
	
	int **playerMoves;
	if (inputMove[0] == 'W') playerMoves = WMoves;
	if (inputMove[0] == 'B') playerMoves = BMoves;
	
	//check if input is valid
	if (!moveValid(boardSize, inputMove[0], inputMove, playerMoves))
		printf("Invalid move.\n");
	else {
		printf("Valid move.\n");
		//update game board based on move
		move(boardSize, inputMove[0], inputMove, gameBoard);
	}
	printGameBoard(boardSize, gameBoard);
	
	//free allocated memory
	for (int row = 0; row < boardSize; row++) {
		free(gameBoard[row]);
		free(WMoves[row]);
		free(BMoves[row]);
	}
	
	free(gameBoard);
	free(WMoves);
	free(BMoves);
	
	return 0;
}
