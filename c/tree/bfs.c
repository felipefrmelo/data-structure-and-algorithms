#include "tree.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>


void bfs(Tree *tree, Queue *visit_order);

int main(int argc, char const *argv[])
{
    
    Queue *visit_order = newQueue();
    Tree *tree = newTree("apple");
    Node *root = tree->root;
    root->set_left_child(root, newNode("banana"));
    root->set_right_child(root, newNode("cherry"));
    root->left->set_left_child(root->left, newNode("dates"));
    root->left->set_right_child(root->left, newNode("melao"));
    root->right->set_left_child(root->right, newNode("uva"));
    root->right->set_right_child(root->right, newNode("pera"));

    bfs(tree, visit_order);

    visit_order->print(visit_order);

    printf("\n%s\n", tree->to_string(tree));
    return 0;
}

void bfs(Tree *tree, Queue *visit_order)
{
    Queue *queue = newQueue();
    Node *node = tree->root;

    queue->enqueue(queue, node);

    while (!queue->is_empty(queue))
    {
        node = queue->dequeue(queue);
        visit_order->enqueue(visit_order, node);
        if (node->has_left_child(node))
            queue->enqueue(queue, node->left);
        
        if (node->has_right_child(node))
            queue->enqueue(queue, node->right);
    }
}