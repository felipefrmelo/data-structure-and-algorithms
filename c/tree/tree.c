#include "node.h"
#include "queue.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct Tree
{
    Node *root;
    char *(*to_string)(struct Tree *);
} Tree;

char *to_string(struct Tree *tree)
{
    if (tree->root == NULL)
        return "<Tree empty>";

    Node *node = tree->root;
    int nodes_in_level = 1, nodes_in_childs = 0;
    Queue *queue = newQueue();
    queue->enqueue(queue, node);
    char *result = malloc(10000000);
    while (!queue->is_empty(queue))
    {
        node = queue->dequeue(queue);

        if (node == NULL)
        {
            strcat(result, nodes_in_level > 1 ? "node(empty) | " : "node(empty)");
            nodes_in_level--;
            continue;
        }

        nodes_in_childs += 2;

        queue->enqueue(queue, node->has_left_child(node) ? node->left : NULL);

        queue->enqueue(queue, node->has_right_child(node) ? node->right : NULL);

        strcat(result, node->toString(node));

        if (nodes_in_level > 1)
            strcat(result, " | ");

        nodes_in_level--;

        if (nodes_in_level == 0)
        {
            nodes_in_level = nodes_in_childs;
            nodes_in_childs = 0;
            strcat(result, "\n");
        }
    }
    return result;
}

Tree *newTree(Value value)
{
    Tree *new = malloc(sizeof(Tree));
    new->root = newNode(value);
    new->to_string = to_string;
    return new;
}