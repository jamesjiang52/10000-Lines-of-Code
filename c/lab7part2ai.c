#include "ai.h"

int numberPiecesScore(int boardSize, char computer, char player, char **gameBoard) {
	/*
	Determines the difference between the number of computer and player pieces divided by the total number of pieces
	*/
	int numberPlayerPieces = 0;
	int numberComputerPieces = 0;
	
	for (int row = 0; row < boardSize; row++) {
		for (int col = 0; col < boardSize; col++) {
			if (gameBoard[row][col] == computer) numberComputerPieces += 1;
			if (gameBoard[row][col] == player)   numberPlayerPieces += 1;
		}
	}
	return(100*(numberComputerPieces - numberPlayerPieces)/(numberComputerPieces + numberPlayerPieces));
}

int numberMovesScore(int boardSize, char computer, char player, int **computerMoves, int **playerMoves) {
	/*
	Determines the difference between the number of computer and player moves divided by the total number of moves
	*/
	int numberPlayerMoves = 0;
	int numberComputerMoves = 0;
	
	for (int row = 0; row < boardSize; row++) {
		for (int col = 0; col < boardSize; col++) {
			if (computerMoves[row][col]) numberComputerMoves += 1;
			if (playerMoves[row][col])   numberPlayerMoves += 1;
		}
	}
	return(100*(numberComputerMoves - numberPlayerMoves)/(numberComputerMoves + numberPlayerMoves + 1)); //add one to avoid division by zero
}

int frontierSquaresScore(int boardSize, char computer, char player, char **gameBoard) {
	/*
	Determines the difference between the number of computer and player frontier squares divided by the total number of frontier squares
	Frontier squares are unoccupied squares immediately adjacent to a player square
	*/
	int numberPlayerFrontierSquares = 0;
	int numberComputerFrontierSquares = 0;
	
	for (int row = 0; row < boardSize; row++) {
		for (int col = 0; col < boardSize; col++) {
			if (gameBoard[row][col] == computer) {
				if (inBounds(boardSize, row - 1, col - 1) && (gameBoard[row - 1][col - 1] == 'U')) numberComputerFrontierSquares += 1;
				if (inBounds(boardSize, row - 1, col) && (gameBoard[row - 1][col] == 'U'))         numberComputerFrontierSquares += 1;
				if (inBounds(boardSize, row - 1, col + 1) && (gameBoard[row - 1][col + 1] == 'U')) numberComputerFrontierSquares += 1;
				if (inBounds(boardSize, row, col - 1) && (gameBoard[row][col - 1] == 'U'))         numberComputerFrontierSquares += 1;
				if (inBounds(boardSize, row, col + 1) && (gameBoard[row][col + 1] == 'U'))         numberComputerFrontierSquares += 1;
				if (inBounds(boardSize, row + 1, col - 1) && (gameBoard[row + 1][col - 1] == 'U')) numberComputerFrontierSquares += 1;
				if (inBounds(boardSize, row + 1, col) && (gameBoard[row + 1][col] == 'U'))         numberComputerFrontierSquares += 1;
				if (inBounds(boardSize, row + 1, col + 1) && (gameBoard[row + 1][col + 1] == 'U')) numberComputerFrontierSquares += 1;
			}
			if (gameBoard[row][col] == player) {
				if (inBounds(boardSize, row - 1, col - 1) && (gameBoard[row - 1][col - 1] == 'U')) numberPlayerFrontierSquares += 1;
				if (inBounds(boardSize, row - 1, col) && (gameBoard[row - 1][col] == 'U'))         numberPlayerFrontierSquares += 1;
				if (inBounds(boardSize, row - 1, col + 1) && (gameBoard[row - 1][col + 1] == 'U')) numberPlayerFrontierSquares += 1;
				if (inBounds(boardSize, row, col - 1) && (gameBoard[row][col - 1] == 'U'))         numberPlayerFrontierSquares += 1;
				if (inBounds(boardSize, row, col + 1) && (gameBoard[row][col + 1] == 'U'))         numberPlayerFrontierSquares += 1;
				if (inBounds(boardSize, row + 1, col - 1) && (gameBoard[row + 1][col - 1] == 'U')) numberPlayerFrontierSquares += 1;
				if (inBounds(boardSize, row + 1, col) && (gameBoard[row + 1][col] == 'U'))         numberPlayerFrontierSquares += 1;
				if (inBounds(boardSize, row + 1, col + 1) && (gameBoard[row + 1][col + 1] == 'U')) numberPlayerFrontierSquares += 1;
			}
		}
	}
	return(100*(numberComputerFrontierSquares - numberPlayerFrontierSquares)/(numberComputerFrontierSquares + numberPlayerFrontierSquares + 1)); //add one to avoid division by zero
}

int cornerStabilityScore(int boardSize, char computer, char player, char **gameBoard) {
	/*
	Determines the difference between the number of computer and player corner squares divided by the total number of corner squares
	*/
	int computerCornerScore = 0;
	int playerCornerScore = 0;
	
	if (gameBoard[0][0] == computer)                         computerCornerScore += 1;
	if (gameBoard[0][boardSize - 1] == computer)             computerCornerScore += 1;
	if (gameBoard[boardSize - 1][0] == computer)             computerCornerScore += 1;
	if (gameBoard[boardSize - 1][boardSize - 1] == computer) computerCornerScore += 1;

	if (gameBoard[0][0] == player)                         playerCornerScore += 1;
	if (gameBoard[0][boardSize - 1] == player)             playerCornerScore += 1;
	if (gameBoard[boardSize - 1][0] == player)             playerCornerScore += 1;
	if (gameBoard[boardSize - 1][boardSize - 1] == player) playerCornerScore += 1;
	
	return(100*(computerCornerScore - playerCornerScore)/(computerCornerScore + playerCornerScore + 1)); //add one to avoid division by zero
}

int XSquareStabilityScore(int boardSize, char computer, char player, char **gameBoard) {
	/*
	Determines the difference between the number of computer and player X-squares divided by the total number of X-squares
	X-squares are the squares immediately diagonally adjacent to the corner squares
	*/
	int computerXSquareScore = 0;
	int playerXSquareScore = 0;
	
	if ((gameBoard[1][1] == computer) && (gameBoard[0][0] == 'U'))                                                 computerXSquareScore += 1;
	if ((gameBoard[1][boardSize - 2] == computer) && (gameBoard[0][boardSize - 1] == 'U'))                         computerXSquareScore += 1;
	if ((gameBoard[boardSize - 2][1] == computer) && (gameBoard[boardSize - 1][0] == 'U'))                         computerXSquareScore += 1;
	if ((gameBoard[boardSize - 2][boardSize - 2] == computer) && (gameBoard[boardSize - 1][boardSize - 1] == 'U')) computerXSquareScore += 1;
	
	if ((gameBoard[1][1] == player) && (gameBoard[0][0] == 'U'))                                                 playerXSquareScore += 1;
	if ((gameBoard[1][boardSize - 2] == player) && (gameBoard[0][boardSize - 1] == 'U'))                         playerXSquareScore += 1;
	if ((gameBoard[boardSize - 2][1] == player) && (gameBoard[boardSize - 1][0] == 'U'))                         playerXSquareScore += 1;
	if ((gameBoard[boardSize - 2][boardSize - 2] == player) && (gameBoard[boardSize - 1][boardSize - 1] == 'U')) playerXSquareScore += 1;
	
	return(100*(computerXSquareScore - playerXSquareScore)/(computerXSquareScore + playerXSquareScore + 1)); //add one to avoid division by zero
}

int CSquareStabilityScore(int boardSize, char computer, char player, char **gameBoard) {
	/*
	Determines the difference between the number of computer and player C-squares divided by the total number of C-squares
	C-squares are the squares on the edges immediately adjacent to the corner squares
	*/
	int computerCSquareScore = 0;
	int playerCSquareScore = 0;
	
	if (gameBoard[0][0] == 'U') {
		if (gameBoard[0][1] == computer)                         computerCSquareScore += 1;
		if (gameBoard[1][0] == computer)                         computerCSquareScore += 1; 
	}
	if (gameBoard[0][boardSize - 1] == 'U') {
		if (gameBoard[0][boardSize - 2] == computer)             computerCSquareScore += 1;
		if (gameBoard[1][boardSize - 1] == computer)             computerCSquareScore += 1;
	}
	if (gameBoard[boardSize - 1][0] == 'U') {
		if (gameBoard[boardSize - 2][0] == computer)             computerCSquareScore += 1;
		if (gameBoard[boardSize - 1][1] == computer)             computerCSquareScore += 1;
	}
	if (gameBoard[boardSize - 1][boardSize - 1] == 'U') {
		if (gameBoard[boardSize - 2][boardSize - 1] == computer) computerCSquareScore += 1;
		if (gameBoard[boardSize - 1][boardSize - 2] == computer) computerCSquareScore += 1;
	}
	
	if (gameBoard[0][0] == 'U') {
		if (gameBoard[0][1] == player)                         computerCSquareScore += 1;
		if (gameBoard[1][0] == player)                         computerCSquareScore += 1; 
	}
	if (gameBoard[0][boardSize - 1] == 'U') {
		if (gameBoard[0][boardSize - 2] == player)             computerCSquareScore += 1;
		if (gameBoard[1][boardSize - 1] == player)             computerCSquareScore += 1;
	}
	if (gameBoard[boardSize - 1][0] == 'U') {
		if (gameBoard[boardSize - 2][0] == player)             computerCSquareScore += 1;
		if (gameBoard[boardSize - 1][1] == player)             computerCSquareScore += 1;
	}
	if (gameBoard[boardSize - 1][boardSize - 1] == 'U') {
		if (gameBoard[boardSize - 2][boardSize - 1] == player) computerCSquareScore += 1;
		if (gameBoard[boardSize - 1][boardSize - 2] == player) computerCSquareScore += 1;
	}
	
	return(100*(computerCSquareScore - playerCSquareScore)/(computerCSquareScore + playerCSquareScore + 1)); //add one to avoid division by zero
}

int winScore(int boardSize, char computer, char player, int **computerMoves, int **playerMoves, char **gameBoard) {
	/*
	Returns a positive number if the computer has won, a negative number if the player has won, and zero otherwise
	*/
	if (!hasMoves(boardSize, computerMoves) && !hasMoves(boardSize, playerMoves)) {
		if (getCount(boardSize, computer, gameBoard) > getCount(boardSize, player, gameBoard))
			return 100;
		else return -100;
	}
	return 0;
}

double gameState(int boardSize, char **gameBoard) {
	/*
	Determines the game state
	The game state is the number of occupied squares divided by the total number of squares
	*/
	double state = 0;
	for (int row = 0; row < boardSize; row++) {
		for (int col = 0; col < boardSize; col++) {
			if (gameBoard[row][col] != 'U')
				state += 1;
		}
	}
	return(state/pow(boardSize, 2));
}

double totalScore(int boardSize, char computer, char player, int **computerMoves, int **playerMoves, char **gameBoard) {
	/*
	Calculates a total score, in the computer's perspective, based on the current state of gameBoard
	A higher total score indicates a more favorable position
	*/
	//weights of factors contributing to total score
	double numberPiecesWeight;
	double numberMovesWeight;
	double frontierSquaresWeight = -50;
	double cornerStabilityWeight = 40000;
	double XSquareStabilityWeight;
	double CSquareStabilityWeight;
	double winWeight = 500000;
	
	//some weights depend on the current game state
	double state = gameState(boardSize, gameBoard);
	
	if (state < 0.35) {
		XSquareStabilityWeight = -10000;
		CSquareStabilityWeight = -2500;
	} else {
		XSquareStabilityWeight = -10000/0.65 + 10000*state/0.65;
		CSquareStabilityWeight = -2500/0.65 + 2500*state/0.65;
	}
	
	if (state < 0.3) {
		numberPiecesWeight = 0;
		numberMovesWeight = 10000;
	} else if (state < 0.8) {
		numberPiecesWeight = -500;
		numberMovesWeight = 5000;
	} else {
		numberPiecesWeight = 60000;
		numberMovesWeight = 20000;
	}
	
	//determine score values of gameBoard
	int computerNumberPiecesScore = numberPiecesScore(boardSize, computer, player, gameBoard);
	int computerNumberMovesScore = numberMovesScore(boardSize, computer, player, computerMoves, playerMoves);
	int computerFrontierSquaresScore = frontierSquaresScore(boardSize, computer, player, gameBoard);
	int computerCornerStabilityScore = cornerStabilityScore(boardSize, computer, player, gameBoard);
	int computerXSquareStabilityScore = XSquareStabilityScore(boardSize, computer, player, gameBoard);
	int computerCSquareStabilityScore = CSquareStabilityScore(boardSize, computer, player, gameBoard);
	int computerWinScore = winScore(boardSize, computer, player, computerMoves, playerMoves, gameBoard);
	
	//calculate total score based on weighted sum
	double score = numberPiecesWeight*computerNumberPiecesScore + 
	               numberMovesWeight*computerNumberMovesScore + 
				   frontierSquaresWeight*computerFrontierSquaresScore + 
	               cornerStabilityWeight*computerCornerStabilityScore + 
				   XSquareStabilityWeight*computerXSquareStabilityScore + 
				   CSquareStabilityWeight*computerCSquareStabilityScore + 
				   winWeight*computerWinScore;
	return score;
}

double minimax(int currentDepth, int maxDepth, double alpha, double beta, 
               int boardSize, char computer, char player, int **computerMoves, int **playerMoves, char **gameBoard, bool computerTurn, char *bestMove, double *bestScore) {
	/*
	Computes the minimax score, with alpha-beta pruning, using a search depth given by maxDepth and a heuristic evaluation function given by totalScore()
	The parameters bestMove and bestScore are pointers used to store the best computer move and the score of that move, respectively
	*/
	//if maxDepth is reached, or neither player has a move
	if (!currentDepth || (!hasMoves(boardSize, computerMoves) && (!hasMoves(boardSize, playerMoves)))) {
		double boardScore = totalScore(boardSize, computer, player, computerMoves, playerMoves, gameBoard);
		return boardScore;
	}
	
	//allocate memory for copies of the game board and the allowed moves of the player and computer
	char **gameBoardTemp;
	gameBoardTemp = (char**) malloc(boardSize*sizeof(char*));
	for (int row = 0; row < boardSize; row++) {
		gameBoardTemp[row] = (char*) malloc(boardSize*sizeof(char));
	}
	
	int **computerMovesTemp;
	computerMovesTemp = (int**) malloc(boardSize*sizeof(int*));
	for (int row = 0; row < boardSize; row++) {
		computerMovesTemp[row] = (int*) malloc(boardSize*sizeof(int));
	}
	
	int **playerMovesTemp;
	playerMovesTemp = (int**) malloc(boardSize*sizeof(int*));
	for (int row = 0; row < boardSize; row++) {
		playerMovesTemp[row] = (int*) malloc(boardSize*sizeof(int));
	}
	
	if (computerTurn) { //maximizing player (computer)
		double maxScore = INT_MIN; //initialize best score to low number
		for (int row = 0; row < boardSize; row++) {
			for (int col = 0; col < boardSize; col++) {
				if (computerMoves[row][col]) {
					//make copy of game board
					for (int i = 0; i < boardSize; i++)
						memcpy(gameBoardTemp[i], gameBoard[i], boardSize*sizeof(char));
					
					char moveString[2];
					moveString[0] = row + 'a';
					moveString[1] = col + 'a';
					
					//execute move and update allowed moves
					move(boardSize, computer, moveString, gameBoardTemp);
					getMoves(boardSize, player, gameBoardTemp, playerMovesTemp);
					getMoves(boardSize, computer, gameBoardTemp, computerMovesTemp);
					
					double boardScore;
					if (hasMoves(boardSize, playerMovesTemp)) //recursive call to minimizing player
						boardScore = minimax(currentDepth - 1, maxDepth, alpha, beta, boardSize, computer, player, computerMovesTemp, playerMovesTemp, gameBoardTemp, false, bestMove, bestScore);
					else //recursive call back to maximizing player
						boardScore = minimax(currentDepth - 1, maxDepth, alpha, beta, boardSize, computer, player, computerMovesTemp, playerMovesTemp, gameBoardTemp, true, bestMove, bestScore);
					//set score to maximum minimax score
					maxScore = fmax(maxScore, boardScore);
					
					//check if minimax score is larger than best score found so far
					if ((currentDepth == maxDepth) && (maxScore > *bestScore)) {
						*bestScore = maxScore;
						bestMove[0] = row + 'a';
						bestMove[1] = col + 'a';
					}
					
					//alpha-beta pruning
					alpha = fmax(alpha, maxScore);
					if (beta <= alpha) {
						//free allocated memory
						for (int row = 0; row < boardSize; row++) {
							free(gameBoardTemp[row]);
							free(computerMovesTemp[row]);
							free(playerMovesTemp[row]);
						}

						free(gameBoardTemp);
						free(computerMovesTemp);
						free(playerMovesTemp);

						return maxScore;
					}
				}
			}
		}
		
		//free allocated memory
		for (int row = 0; row < boardSize; row++) {
			free(gameBoardTemp[row]);
			free(computerMovesTemp[row]);
			free(playerMovesTemp[row]);
		}
	
		free(gameBoardTemp);
		free(computerMovesTemp);
		free(playerMovesTemp);

		return maxScore;
	} else { //minimizing player
		double maxScore = INT_MAX; //initialize best score to high number
		for (int row = 0; row < boardSize; row++) {
			for (int col = 0; col < boardSize; col++) {
				if (playerMoves[row][col]) {
					//make copy of game board
					for (int i = 0; i < boardSize; i++)
						memcpy(gameBoardTemp[i], gameBoard[i], boardSize*sizeof(char));
					
					char moveString[2];
					moveString[0] = row + 'a';
					moveString[1] = col + 'a';
					
					//execute move and update allowed moves
					move(boardSize, player, moveString, gameBoardTemp);
					getMoves(boardSize, player, gameBoardTemp, playerMovesTemp);
					getMoves(boardSize, computer, gameBoardTemp, computerMovesTemp);
					
					double boardScore;
					if (hasMoves(boardSize, computerMovesTemp)) //recursive call to maximizing player
						boardScore = minimax(currentDepth - 1, maxDepth, alpha, beta, boardSize, computer, player, computerMovesTemp, playerMovesTemp, gameBoardTemp, true, bestMove, bestScore);
					else //recursive call back to minimizing player
						boardScore = minimax(currentDepth - 1, maxDepth, alpha, beta, boardSize, computer, player, computerMovesTemp, playerMovesTemp, gameBoardTemp, false, bestMove, bestScore);
					//set score to minimum minimax score
					maxScore = fmin(maxScore, boardScore);
					
					//alpha-beta pruning
					beta = fmin(beta, maxScore);
					if (beta <= alpha) {
						//free allocated memory
						for (int row = 0; row < boardSize; row++) {
							free(gameBoardTemp[row]);
							free(computerMovesTemp[row]);
							free(playerMovesTemp[row]);
						}

						free(gameBoardTemp);
						free(computerMovesTemp);
						free(playerMovesTemp);

						return maxScore;
					}
				}
			}
		}
		
		//free allocated memory
		for (int row = 0; row < boardSize; row++) {
			free(gameBoardTemp[row]);
			free(computerMovesTemp[row]);
			free(playerMovesTemp[row]);
		}

		free(gameBoardTemp);
		free(computerMovesTemp);
		free(playerMovesTemp);

		return maxScore;
	}
}
