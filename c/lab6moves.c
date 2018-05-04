#include "moves.h"

bool inBounds(int boardSize, int row, int col) {
	/*
	Checks if (row, col) is within game board limits
	*/
	if ((row > boardSize - 1) || (col > boardSize - 1)) 
		return false;
	if ((row < 0) || (col < 0)) 
		return false;
	return true;
}

int scoreInDirection(int boardSize, int row, int col, int deltaRow, int deltaCol, char player, char **gameBoard) {
	/*
	Determines score in the direction given by (deltaRow, deltaCol), returns 0 if move is not legal in direction
	*/
	int score = 1;
	
	char otherPlayer;
	if (player == 'W') otherPlayer = 'B';
	if (player == 'B') otherPlayer = 'W';
	
	if (!inBounds(boardSize, row + deltaRow, col + deltaCol))
		return 0;
	if (gameBoard[row + deltaRow][col + deltaCol] != otherPlayer)
		return 0;
		
	int checkRow = row;
	int checkCol = col;
	
	while (1) {
		if (!inBounds(boardSize, checkRow + 2*deltaRow, checkCol + 2*deltaCol))
			return 0;
		if (gameBoard[checkRow + 2*deltaRow][checkCol + 2*deltaCol] == player) {
			return score;
		} else if (gameBoard[checkRow + 2*deltaRow][checkCol + 2*deltaCol] == 'U')
			return 0;
		else {
			checkRow += deltaRow;
			checkCol += deltaCol;
			score += 1;
		}
	}
}

void getMoves(int boardSize, char player, char **gameBoard, int **playerMoves) {
	/*
	Updates allowed moves array
	*/
	for (int row = 0; row < boardSize; row++) {
		for (int col = 0; col < boardSize; col++) {
			playerMoves[row][col] = 0;
			if (gameBoard[row][col] == 'U') {
				if (scoreInDirection(boardSize, row, col, -1, -1, player, gameBoard)) { playerMoves[row][col] = 1; continue;}
				if (scoreInDirection(boardSize, row, col, -1, 0, player, gameBoard))  { playerMoves[row][col] = 1; continue;}
				if (scoreInDirection(boardSize, row, col, -1, 1, player, gameBoard))  { playerMoves[row][col] = 1; continue;}
				if (scoreInDirection(boardSize, row, col, 0, -1, player, gameBoard))  { playerMoves[row][col] = 1; continue;}
				if (scoreInDirection(boardSize, row, col, 0, 1, player, gameBoard))   { playerMoves[row][col] = 1; continue;}
				if (scoreInDirection(boardSize, row, col, 1, -1, player, gameBoard))  { playerMoves[row][col] = 1; continue;}
				if (scoreInDirection(boardSize, row, col, 1, 0, player, gameBoard))   { playerMoves[row][col] = 1; continue;}
				if (scoreInDirection(boardSize, row, col, 1, 1, player, gameBoard))   { playerMoves[row][col] = 1; continue;}
			}
		}
	}
}

bool moveValid(int boardSize, char player, char *moveString, int **playerMoves) {
	/*
	Checks if moveString is a valid move
	*/
	int row = moveString[1] - 'a';
	int col = moveString[2] - 'a';
	if (!inBounds(boardSize, row, col))
		return false;
	if (playerMoves[row][col])
		return true;
	return false;
}

void moveInDirection(int boardSize, int row, int col, int deltaRow, int deltaCol, char player, char **gameBoard) {
	/*
	Updates game board by moving in the direction given by (deltaRow, deltaCol)
	*/
	int checkRow = row;
	int checkCol = col;
	while (1) {
		if (!inBounds(boardSize, checkRow + 2*deltaRow, checkCol + 2*deltaCol))
			return;
		if (gameBoard[checkRow + 2*deltaRow][checkCol + 2*deltaCol] == player) {
			updateGameBoard('a' + checkRow + deltaRow, 'a' + checkCol + deltaCol, player, gameBoard);
			return;
		} else {
			updateGameBoard('a' + checkRow + deltaRow, 'a' + checkCol + deltaCol, player, gameBoard);
			checkRow += deltaRow;
			checkCol += deltaCol;
		}
	}
}

void move(int boardSize, char player, char *moveString, char **gameBoard) {
	/*
	Updates game board by the move given by moveString
	*/
	updateGameBoard(moveString[1], moveString[2], player, gameBoard);

	int row = moveString[1] - 'a';
	int col = moveString[2] - 'a';

	if (scoreInDirection(boardSize, row, col, -1, -1, player, gameBoard)) moveInDirection(boardSize, row, col, -1, -1, player, gameBoard);
	if (scoreInDirection(boardSize, row, col, -1, 0, player, gameBoard))  moveInDirection(boardSize, row, col, -1, 0, player, gameBoard);
	if (scoreInDirection(boardSize, row, col, -1, 1, player, gameBoard))  moveInDirection(boardSize, row, col, -1, 1, player, gameBoard);
	if (scoreInDirection(boardSize, row, col, 0, -1, player, gameBoard))  moveInDirection(boardSize, row, col, 0, -1, player, gameBoard);
	if (scoreInDirection(boardSize, row, col, 0, 1, player, gameBoard))   moveInDirection(boardSize, row, col, 0, 1, player, gameBoard);
	if (scoreInDirection(boardSize, row, col, 1, -1, player, gameBoard))  moveInDirection(boardSize, row, col, 1, -1, player, gameBoard);
	if (scoreInDirection(boardSize, row, col, 1, 0, player, gameBoard))   moveInDirection(boardSize, row, col, 1, 0, player, gameBoard);
	if (scoreInDirection(boardSize, row, col, 1, 1, player, gameBoard))   moveInDirection(boardSize, row, col, 1, 1, player, gameBoard);
}
