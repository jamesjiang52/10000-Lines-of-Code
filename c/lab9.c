#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include "ui.h"
#include "library.h"

#define MAX_LIB_SIZE 100
#define MAX_LENGTH 1024

int main(void) {
    Song library[MAX_LIB_SIZE];
    int librarySize = 0;  //number of elements stored in the library

    printf("Personal Music Library.\n\n");
    printf("Commands are I (insert), S (sort by artist), P (print), Q (quit).\n");

    char response;
    char input[MAX_LENGTH + 1];
    do {
        //user inputs a command
        inputStringFromUser("\nCommand", input, MAX_LENGTH);
        response = toupper(input[0]);

        if (response == 'I') {
            //insert song
			Song newSong;

            char *promptName = "Song name";
            char *promptArtist =  "Artist";
            char *promptGenre = "Genre";

			//get song info from user
			inputStringFromUser(promptName, input, MAX_LENGTH);
			strcpy(newSong.songName, input);
			inputStringFromUser(promptArtist, input, MAX_LENGTH);
			strcpy(newSong.artist, input);
			inputStringFromUser(promptGenre, input, MAX_LENGTH);
			strcpy(newSong.genre, input);

			library[librarySize] = newSong;
			librarySize += 1;
        } else if (response == 'P') {
            //print entire libary
			printLibrary(library, librarySize);
        } else if (response == 'S') {
            //sort songs in alphabetical order by artist, then song name
			cocktailSort(library, librarySize);
			printLibrary(library, librarySize);
        } else if (response == 'Q') {
            // do nothing
			;
        } else {
            printf("\nInvalid command.\n");
        }
    } while(response != 'Q');

    return 0;
}
