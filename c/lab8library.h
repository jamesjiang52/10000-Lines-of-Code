#ifndef LIBRARY_H
#define LIBRARY_H
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node Node;

void freeSong(Node *song);
Node *insertSong(Node *head, Node *newSong);
void printLibrary(Node *head);
void searchSong(Node *head, char *songName);
Node *deleteSong(Node *head, char *songName);

#endif
