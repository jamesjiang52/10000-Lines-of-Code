#include "ui.h"

void inputStringFromUser(char prompt[], char s[], int maxStrLength) {
    /*
    Gets input string from the user
    */
    int i = 0;
    char c;
    
    printf("%s --> ", prompt);
    while ((i < maxStrLength) && ((c = getchar()) != '\n'))
        s[i++] = c;
    s[i] = '\0';
}

void songNameDuplicate(char songName[]) {
    /*
    Prints message when inserting a song that is already in the library
    */
	printf("\nA song with the name '%s' is already in the music library.\nNo new song entered.\n", songName);
}

void songNameFound(char songName[]) {
    /*
    Prints message when song is found in the library
    */
    printf("\nThe song name '%s' was found in the music library.\n", songName);
}

void songNameNotFound(char songName[]) {
    /*
    Prints message when song is not found in the library
    */
    printf("\nThe song name '%s' was not found in the music library.\n", songName);
}

void songNameDeleted(char songName[]) {
    /*
    Prints message when song is deleted from the library
    */
    printf("\nDeleting a song with name '%s' from the music library.\n", songName);
}

void printMusicLibraryEmpty() {
    /*
    Prints message when printing an empty library
    */
    printf("\nThe music library is empty.\n");
}

void printMusicLibraryTitle() {
    /*
    Prints message when library is printed
    */
    printf("\nMy Personal Music Library: \n");
}
