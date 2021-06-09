#include "node.h"
#include "queue.h"

typedef struct Tree
{
    Node *root;
    char *(*to_string)(struct Tree *);
} Tree;

char *to_string(struct Tree *tree);

Tree *newTree(Value value);