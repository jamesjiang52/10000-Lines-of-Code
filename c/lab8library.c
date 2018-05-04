#include "library.h"

struct node {
    char *artist;
    char *songName;
    char *genre;
    struct node *nextNode;
};

void freeSong(Node *song) {
	/*
	Frees all memory allocated for song
	*/
	free(song->songName);
	free(song->artist);
	free(song->genre);
	free(song);
}

Node *insertSong(Node *head, Node *newSong) {
	/*
	Inserts song alphabetically into library
	*/
	//list is empty
	if (!head)
		return newSong;
	
	//song goes before head
	if (strcmp(newSong->songName, head->songName) < 0) {
		newSong->nextNode = head;
		return newSong;
	}
	
	Node *current = head;
	while (!strcmp(newSong->songName, current->songName) && current->nextNode && (strcmp(newSong->songName, current->nextNode->songName) > 0))
		current = current->nextNode;
        
    if (!strcmp(newSong->songName, current->songName)) {
        songNameDuplicate(newSong->songName);
        freeSong(newSong);
        return head;
    }
    
	newSong->nextNode = current->nextNode;
	current->nextNode = newSong;
	
	return head;
}

void printLibrary(Node *head) {
	/*
	Prints entire library
	*/
	if (!head) { //list is empty
		printMusicLibraryEmpty();
	} else {
		printMusicLibraryTitle();
		Node *current = head;
		while (current) {
			printf("\n%s\n%s\n%s\n", current->songName, current->artist, current->genre);
			current = current->nextNode;
		}
	}
}

void searchSong(Node *head, char *songName) {
	/*
	Searches for song in library. If found, prints song info
	*/
	Node *current = head;
	while (current) {
		if (!strcmp(current->songName, songName)) {
			songNameFound(songName);
			printf("\n%s\n%s\n%s\n", current->songName, current->artist, current->genre);
			return;
		}
		if (strcmp(current->songName, songName) > 0) {
			songNameNotFound(songName);
			return;
		}
		current = current->nextNode;
	}
	songNameNotFound(songName);
}

Node *deleteSong(Node *head, char *songName) {
	/*
	Deletes song from library
	*/
	//list is empty
	if (!head) {
		songNameNotFound(songName);
		return head;
	}
	
	//song to delete is head
	if (!strcmp(head->songName, songName)) {
		Node *temp = head->nextNode;
		freeSong(head);
		songNameDeleted(songName);
		return temp;
	}
	
	Node *current = head;
	while (current->nextNode) {
		if (!strcmp(current->nextNode->songName, songName)) {
			Node *temp = current->nextNode;
			songNameDeleted(songName);
			current->nextNode = current->nextNode->nextNode;
			freeSong(temp);
			return head;
		}
		current = current->nextNode;
	}
	songNameNotFound(songName);
	return head;
}
