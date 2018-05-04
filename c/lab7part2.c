#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <limits.h>
#include "gameboard.h"
#include "moves.h"
#include "ai.h"

int main() {
	int boardSize = 0;
	char computer, player;
	bool playerHasFirstMove;
	
	//initial setup of game
	printf("Enter the board dimension: ");
	scanf("%d%*c", &boardSize);
	printf("Computer plays (B/W) : ");
	scanf("%c%*c", &computer);
	
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
	
	//assign player and computer to chars
	int **playerMoves;
	int **computerMoves;
	if (computer == 'W') {
		player = 'B';
		playerHasFirstMove = true;
		computerMoves = WMoves;
		playerMoves = BMoves;
	}
	if (computer == 'B') {
		player = 'W';
		playerHasFirstMove = false;
		computerMoves = BMoves;
		playerMoves = WMoves;
	}

	getMoves(boardSize, computer, gameBoard, computerMoves);
	getMoves(boardSize, player, gameBoard, playerMoves);
	
	char inputMove[2];
	
	//keep looping until game ends
	while (1) {
		//update player allowed moves
		getMoves(boardSize, player, gameBoard, playerMoves);
		
		//skip in first iteration of loop if player doesn't have first move
		if (playerHasFirstMove) {
			if (hasMoves(boardSize, playerMoves)) {
				//user inputs a move
				printf("Enter move for colour %c (RowCol): ", player);
				scanf("%s", inputMove);

				//check if move is valid
				if (moveValid(boardSize, player, inputMove, playerMoves)) {
					move(boardSize, player, inputMove, gameBoard);
					printGameBoard(boardSize, gameBoard);
				} else {
					printf("Invalid move.\n%c player wins.\n", computer);
					return 0;
				}
			} else if (hasMoves(boardSize, computerMoves)) { //player has no valid move, but computer has valid move
				printf("%c player has no valid move.\n", player);
			} else //neither player has a valid move, so break the loop and end the game
				break;
		}
		
		playerHasFirstMove = true;
		
		//update allowed moves
		getMoves(boardSize, player, gameBoard, playerMoves);
		getMoves(boardSize, computer, gameBoard, computerMoves);
		
		if (hasMoves(boardSize, computerMoves)) {
			//determine and execute best computer move
			char computerBestMove[2] = "aa";
			double computerBestScore = INT_MIN;
			
			minimax(6, 6, INT_MIN, INT_MAX, boardSize, computer, player, computerMoves, playerMoves, gameBoard, true, computerBestMove, &computerBestScore);
			printf("Computer places %c at %s.\n", computer, computerBestMove);
			move(boardSize, computer, computerBestMove, gameBoard);
			printGameBoard(boardSize, gameBoard);
		} else if (hasMoves(boardSize, playerMoves)) { //computer has no valid move, but player has valid move
			printf("%c player has no valid move.\n", computer);
		} else //neither player has a valid move, so break the loop and end the game
			break;
	}
	
	//count pieces and determine winner
	if (getCount(boardSize, player, gameBoard) > getCount(boardSize, computer, gameBoard))
		printf("%c player wins.\n", player);
	else if (getCount(boardSize, player, gameBoard) < getCount(boardSize, computer, gameBoard))
		printf("%c player wins.\n", computer);
	else
		printf("Draw!");
	
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
