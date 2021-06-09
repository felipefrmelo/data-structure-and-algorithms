#include "stdlib.h"

typedef int Value;

typedef struct Node
{
    Value *value;
    struct Node *next;

} Node;

Node *newNode(Value *value)
{
    Node *result = malloc(sizeof(Node));
    result->value = value;
    return result;
}

typedef struct Queue
{
    Node *head;
    Node *tail;
    int num_elements;
    void (*enqueue)(struct Queue *, Value *);
    Value *(*dequeue)(struct Queue *);
    int (*isEmpty)(struct Queue *);
    int (*size)(struct Queue *);

} Queue;

void enqueue(Queue *self, Value *value)
{
    Node *new_node = newNode(value);
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

Value *dequeue(Queue *self)
{
    if (self->isEmpty(self))
    {
        return NULL;
    }

    Value *value = self->head->value;
    self->head = self->head->next;
    self->num_elements--;
    return value;
}

int isEmpty(Queue *self)
{
    return self->num_elements == 0 ? 1 : 0;
}

int size(Queue *self)
{
    return self->num_elements;
}

Queue *newQueue()
{
    Queue *result = malloc(sizeof(Queue));
    result->num_elements = 0;
    result->enqueue = enqueue;
    result->dequeue = dequeue;
    result->isEmpty = isEmpty;
    result->size = size;

    return result;
}