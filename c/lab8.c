#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include "ui.h"
#include "library.h"

const int MAX_LENGTH = 1024;

int main() {
	Node *head = NULL;

    printf("Personal Music Library.\n\n");
    printf("%s", "Commands are I (insert), D (delete), S (search by song name),\nP (print), Q (quit).\n");
    
    char response;
    char input[MAX_LENGTH + 1];
    do {
        //user inputs a command
        inputStringFromUser("\nCommand", input, MAX_LENGTH);
        response = toupper(input[0]);

        if (response == 'I') {
            //insert song
			Node *newSong = (Node*) malloc(sizeof(Node));
			
            char *promptName = "Song name";
            char *promptArtist =  "Artist";
            char *promptGenre = "Genre";
			
			//get song info from user
			inputStringFromUser(promptName, input, MAX_LENGTH);
			newSong->songName = (char*) malloc((strlen(input) + 1)*(sizeof(char)));
			strcpy(newSong->songName, input);
			inputStringFromUser(promptArtist, input, MAX_LENGTH);
			newSong->artist = (char*) malloc((strlen(input) + 1)*(sizeof(char)));
			strcpy(newSong->artist, input);
			inputStringFromUser(promptGenre, input, MAX_LENGTH);
			newSong->genre = (char*) malloc((strlen(input) + 1)*(sizeof(char)));
			strcpy(newSong->genre, input);
			newSong->nextNode = NULL;
			
			head = insertSong(head, newSong);
        } else if (response == 'D') {
            //delete song
            char *prompt = "\nEnter the name of the song to be deleted";
			inputStringFromUser(prompt, input, MAX_LENGTH);
			head = deleteSong(head, input);
        } else if (response == 'S') {
            //search for song
            char *prompt = "\nEnter the name of the song to search for";
			inputStringFromUser(prompt, input, MAX_LENGTH);
			searchSong(head, input);
        } else if (response == 'P') {
            //print entire library
			printLibrary(head);
        } else if (response == 'Q') {
			//do nothing
            ;
        } else {
            printf("\nInvalid command.\n");
        }
    } while (response != 'Q');
  
    //delete entire library
	while (head) {
		Node *temp = head;
		songNameDeleted(head->songName);
		head = head->nextNode;
		freeSong(temp);
	}
	printLibrary(head);
	
    return 0;
}
