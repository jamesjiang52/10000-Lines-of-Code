#include "ui.h"

void inputStringFromUser(char prompt[], char s[], int maxStrLength) {
    /*
    Gets input string from the user
    */
    int i = 0;
    char c;

    printf("%s --> ", prompt);
    while(i < maxStrLength && (c = getchar()) != '\n')
        s[i++] = c;
    s[i] = '\0';
}

void printMusicLibraryEmpty(void) {
    /*
    Prints message when printing an empty library
    */
    printf("\nThe music library is empty.\n");
}

void printMusicLibraryTitle(void) {
    /*
    Prints message when library is printed
    */
    printf("\nMy Personal Music Library: \n");
}

void printLibrary(Song library[], int size) {
    /*
	Prints entire library
	*/
    if (size == 0) {
        printMusicLibraryEmpty();
    } else {
        printMusicLibraryTitle();
        for(int i = 0; i < size; i++)
            printf("\n%s\n%s\n%s\n", library[i].songName, library[i].artist, library[i].genre);
    }
}
