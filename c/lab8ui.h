#ifndef UI_H
#define UI_H
#include <stdio.h>
#include <stdlib.h>

void inputStringFromUser(char prompt[], char s[], int arraySize);
void songNameDuplicate(char songName[]);
void songNameFound(char songName[]);
void songNameNotFound(char songName[]);
void songNameDeleted(char songName[]);
void printMusicLibraryEmpty();
void printMusicLibraryTitle();

#endif
