#include "ai.h"

char *getBestMove(int boardSize, int **computerMoves) {
	/*
	Returns the (row, col) move of the computer that captures the most opponent pieces
	*/
	static char bestMove[2];
	int maxScore = 0;
	for (int row = 0; row < boardSize; row++) {
		for (int col = 0; col < boardSize; col++) {
			if (computerMoves[row][col] > maxScore) {
				maxScore = computerMoves[row][col];
				bestMove[0] = 'a' + row;
				bestMove[1] = 'a' + col;
			}
		}
	}
	return(bestMove);
}
