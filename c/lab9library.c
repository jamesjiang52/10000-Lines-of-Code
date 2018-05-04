#include "library.h"

struct song {
    char songName[MAX_LENGTH];
    char artist[MAX_LENGTH];
    char genre[MAX_LENGTH];
};

void cocktailSort(Song library[], int size) {
    /*
    Sorts library in ascending alphabetical order, first by artist
    then by song name, using cocktail sort
    */
    bool goingUp = true;
    bool sorted = false;
    bool shouldSwap;
    int bottom = 0;
	int top = size - 1;
	int i;

    while (bottom < top && !sorted) {
        sorted = true;
		
        if (goingUp) {
            for (i = bottom; i < top; i++) {
                //set shouldSwap to true if song i should go after song (i + 1)
				shouldSwap = false;
				if (strcmp(library[i].artist, library[i + 1].artist) > 0) {
					shouldSwap = true;
				} else if (!(strcmp(library[i].artist, library[i + 1].artist))) {
					if (strcmp(library[i].songName, library[i + 1].songName) > 0) {
						shouldSwap = true;
					}
				}
				
                if (shouldSwap) {
                    Song temp = library[i];
                    library[i] = library[i + 1];
                    library[i + 1] = temp;
                    sorted = false;
                }
            }
            top--;
            goingUp = false;
        } else {
			for (i = top; i > bottom; i--) {
				//set shouldSwap to true if song (i - 1) should go after song i
				shouldSwap = false;
				if (strcmp(library[i - 1].artist, library[i].artist) > 0) {
					shouldSwap = true;
				} else if (!(strcmp(library[i - 1].artist, library[i].artist))) {
					if (strcmp(library[i - 1].songName, library[i].songName) > 0) {
						shouldSwap = true;
					}
				}

				if (shouldSwap) {
					Song temp = library[i - 1];
					library[i - 1] = library[i];
					library[i] = temp;
					sorted = false;
				}
			}
			bottom++;
			goingUp = true;
        }
    }
}
