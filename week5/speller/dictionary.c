// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 10000;

unsigned int word_count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);

    for (node *ptr = table[index]; ptr != NULL; ptr = ptr->next)
    {
        if (strcasecmp(ptr->word, word) == 0)
        {
            return true;
        }
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int sum = 0;
    for (int i = 0; i < word[i] != '\0'; i++)
    {
        sum += toupper(word[i]);
    }
    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary file
    FILE *source = fopen(dictionary, "r");

    if (source == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        return false;
    }

    // Read strings from file one at a time

    char word[LENGTH + 1];

    while (fscanf(source, "%s", word) != EOF)
    {
        // Create a new node for each word
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(source);
            return false;
        }

        strcpy(n->word, word);

        // Hash word to obtain a hash value
        int index = hash(word);

        // Insert node into hash table at that location
        n->next = table[index];
        table[index] = n;
    }

    // Close the dictionary file
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        for (node *ptr = table[i]; ptr != NULL; ptr = ptr->next)
        {
            word_count += 1;
        }
    }
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *ptr = table[i];
        while (ptr != NULL)
        {
            node *tmp = ptr->next;
            free(ptr);
            ptr = tmp;
        }
    }
    return true;
}
