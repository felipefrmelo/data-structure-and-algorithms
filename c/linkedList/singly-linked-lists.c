#include "stdio.h"
#include "stdlib.h"
#include "string.h"

typedef struct Node
{
    long int value;
    struct Node *next;

} Node;

typedef struct LinkedList
{
    Node *head;
    void (*append)(struct LinkedList *, long int);
    char *(*to_string)(struct LinkedList *);
    int (*length)(struct LinkedList *);

} LinkedList;

int length(LinkedList *self)
{
    Node *node = self->head;
    int length = 1;
    while (node->next != NULL)
    {
        node = node->next;
        length++;
    }
    return length;
}

void append(LinkedList *self, long int value)
{
    Node *new = malloc(sizeof(Node));

    if (self->head == NULL)
    {
        new->value = value;
        self->head = new;
        return;
    }
    Node *node = self->head;

    while (node->next)
    {
        node = node->next;
    }
    
    new->value = value;
    node->next = new;
}

char *to_string(LinkedList *self)
{
    Node *node = self->head;

    char *ptr;
    char *value = malloc(sizeof(long int));

    ptr = malloc(sizeof("Node: value -> ") * self->length(self));

    while (node->next != NULL)
    {
        strcat(ptr, "Node: ");
        sprintf(value, "%lu -> ", node->value);
        strcat(ptr, value);
        node = node->next;
    }
    strcat(ptr, "Node: ");
    sprintf(value, "%lu", node->value);
    strcat(ptr, value);

    return ptr;
}
LinkedList newLinkedList()
{
    Node *head;
    LinkedList new;
    new.head = head;
    new.append = append;
    new.length = length;
    new.to_string = to_string;
    return new;
}

int main(int argc, char const *argv[])
{
    LinkedList l = newLinkedList();
    l.append(&l, 1);
    l.append(&l, 61);
    l.append(&l, 7);
    l.append(&l, 8);
    l.append(&l, 8888);
    l.append(&l, 121211212);
    printf("length: %d\n", l.length(&l));
    printf("Lista %s\n", l.to_string(&l));

    return 0;
}
