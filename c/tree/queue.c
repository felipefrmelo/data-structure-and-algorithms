#include "node.h"

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef Node *ValueQueue;

typedef struct NodeQueue
{
    ValueQueue value;
    struct NodeQueue *next;

} NodeQueue;

NodeQueue *newNodeQueue(ValueQueue value)
{
    NodeQueue *result = malloc(sizeof(NodeQueue));
    result->value = value;
    return result;
}

typedef struct Queue
{
    NodeQueue *head;
    NodeQueue *tail;
    int num_elements;
    void (*enqueue)(struct Queue *, ValueQueue);
    ValueQueue (*dequeue)(struct Queue *);
    int (*is_empty)(struct Queue *);
    int (*size)(struct Queue *);
    void (*print)(struct Queue *);

} Queue;

void enqueue(Queue *self, ValueQueue value)
{
    NodeQueue *new_node = newNodeQueue(value);
    if (self->head == NULL)
    {
        self->head = new_node;
        self->tail = self->head;
    }
    else
    {
        self->tail->next = new_node;
        self->tail = self->tail->next;
    }

    self->num_elements++;
}

ValueQueue dequeue(Queue *self)
{
    if (self->is_empty(self))
    {
        return NULL;
    }
    ValueQueue value = self->head->value;
    self->head = self->head->next;
    self->num_elements--;
    return value;
}

int is_empty(Queue *self)
{
    return self->num_elements == 0 ? 1 : 0;
}

int size(Queue *self)
{
    return self->num_elements;
}

void print(struct Queue *self)
{

    if (self->is_empty(self))
    {
        printf("\n<queue is empty>\n");
    }
    else
    {
        printf("\n<top of queue>");
        NodeQueue *node = self->head;
        while (node)
        {
            ValueQueue value = node->value;
            printf("\n_________________\n%s", value->toString(value));
            node = node->next;
        }
        printf("\n_________________\n<bottom of queue>\n");
    }
};

Queue *newQueue()
{
    Queue *result = malloc(sizeof(Queue));
    result->num_elements = 0;
    result->enqueue = enqueue;
    result->dequeue = dequeue;
    result->is_empty = is_empty;
    result->size = size;
    result->print = print;

    return result;
}
