#ifndef MOVES_H
#define MOVES_H
#include <stdlib.h>
#include <stdbool.h>
#include "gameboard.h"

bool inBounds(int boardSize, int row, int col);
int scoreInDirection(int boardSize, int row, int col, int deltaRow, int deltaCol, char player, char **gameBoard);
void getMoves(int boardSize, char player, char **gameBoard, int **playerMoves);
bool moveValid(int boardSize, char player, char *moveString, int **playerMoves);
void moveInDirection(int boardSize, int row, int col, int deltaRow, int deltaCol, char player, char **gameBoard);
void move(int boardSize, char player, char *moveString, char **gameBoard);

#endif
