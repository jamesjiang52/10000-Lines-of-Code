#ifndef AI_H
#define AI_H
#include <stdlib.h>
#include <math.h>
#include <limits.h>
#include "gameboard.h"
#include "moves.h"

int numberPiecesScore(int boardSize, char computer, char player, char **gameBoard);
int numberMovesScore(int boardSize, char computer, char player, int **computerMoves, int **playerMoves);
int frontierSquaresScore(int boardSize, char computer, char player, char **gameBoard);
int cornerStabilityScore(int boardSize, char computer, char player, char **gameBoard);
int XSquareStabilityScore(int boardSize, char computer, char player, char **gameBoard);
int CSquareStabilityScore(int boardSize, char computer, char player, char **gameBoard);
int winScore(int boardSize, char computer, char player, int **computerMoves, int **playerMoves, char **gameBoard);
double totalScore(int boardSize, char computer, char player, int **computerMoves, int **playerMoves, char **gameBoard);
double minimax(int currentDepth, int maxDepth, double alpha, double beta, int boardSize, char computer, char player, int **computerMoves, int **playerMoves, char **gameBoard, bool computerTurn, char *bestMove, double *bestScore);

#endif
