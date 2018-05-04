#ifndef GAMEBOARD_H
#define GAMEBOARD_H
#include <stdio.h>
#include <stdlib.h>

void printGameBoard(int boardSize, char **gameBoard);
void updateGameBoard(char row, char col, char player, char **gameBoard);
int getCount(int boardSize, char player, char **gameBoard);

#endif
