#include <stdlib.h>
#include <stdio.h>
#include "tree.h"
#include "queue.h"

void traverse_pre_order(Node *, Queue *);
void traverse_in_order(Node *, Queue *);
void traverse_post_order(Node *, Queue *);
Queue *traverse_tree(Tree *, void (*traverse)(Node *, Queue *));

int main(int argc, char const *argv[])
{
    Queue *visit_order;
    Tree *tree = newTree("apple");
    Node *root = tree->root;
    root->set_left_child(root, newNode("banana"));
    root->set_right_child(root, newNode("cherry"));
    root->left->set_left_child(root->left, newNode("dates"));
    root->right->set_left_child(root->right, newNode("uva"));
    root->right->set_right_child(root->right, newNode("pera"));

    visit_order = traverse_tree(tree, traverse_pre_order);
    printf("\nvisit pre order\n");
    visit_order->print(visit_order);
    visit_order = traverse_tree(tree, traverse_in_order);
    printf("\nvisit in order\n");
    visit_order->print(visit_order);
    visit_order = traverse_tree(tree, traverse_post_order);
    printf("\nvisit post order\n");
    visit_order->print(visit_order);
    return 0;
}

Queue *traverse_tree(Tree *tree, void (*traverse)(Node *node, Queue *visit_order))
{

    Queue *visit_order = newQueue();
    traverse(tree->root, visit_order);
    return visit_order;
}


void traverse_pre_order(Node *node, Queue *visit_order)
{
    if (node != NULL)
    {
        visit_order->enqueue(visit_order, node);

        traverse_pre_order(node->left, visit_order);
        traverse_pre_order(node->right, visit_order);
    }
}

void traverse_in_order(Node *node, Queue *visit_order)
{
    if (node != NULL)
    {

        traverse_in_order(node->left, visit_order);
        visit_order->enqueue(visit_order, node);
        traverse_in_order(node->right, visit_order);
    }
}

void traverse_post_order(Node *node, Queue *visit_order)
{
    if (node != NULL)
    {

        traverse_post_order(node->left, visit_order);
        traverse_post_order(node->right, visit_order);
        visit_order->enqueue(visit_order, node);
    }
}

