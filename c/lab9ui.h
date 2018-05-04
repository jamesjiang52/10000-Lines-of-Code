#ifndef UI_H
#define UI_H
#include <stdio.h>
#include <stdlib.h>

void inputStringFromUser(char prompt[], char s[], int arraySize);
void printMusicLibraryEmpty(void);
void printMusicLibraryTitle(void);
void printLibrary(Song library[], int size);

#endif
