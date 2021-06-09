#include "node.c"

#ifndef STACK_H
#define STACK_H

typedef Node *ValueStack;

typedef struct NodeStack
{
    ValueStack value;
    struct NodeStack *next;

} NodeStack;

NodeStack *newNodeStack(ValueStack value)
{
    NodeStack *new = malloc(sizeof(NodeStack));
    new->value = malloc(sizeof(Value));
    new->value = value;

    return new;
}

typedef struct Stack
{
    NodeStack *head;
    int num_elements;
    void (*push)(struct Stack *, ValueStack);
    ValueStack (*pop)(struct Stack *);
    ValueStack (*top)(struct Stack *);
    int (*is_empty)(struct Stack *);
    void (*print)(struct Stack *);
    void (*toString)(struct Stack *);
} Stack;

void push(Stack *self, ValueStack value)
{
    NodeStack *new_node = newNodeStack(value);
    if (self->head == NULL)
    {
        self->head = new_node;
    }
    else
    {
        new_node->next = self->head;
        self->head = new_node;
    }

    self->num_elements++;
}

ValueStack pop(struct Stack *self)
{
    if (self->is_empty(self))
        return NULL;

    ValueStack value = self->head->value;
    self->head = self->head->next;
    self->num_elements--;
    return value;
}

ValueStack top(struct Stack *self)
{
    return self->is_empty(self) ? NULL : self->head->value;
}

int is_empty(struct Stack *self)
{
    return self->num_elements == 0;
}

void print(struct Stack *self)
{

    if (self->is_empty(self))
    {
        printf("\n<stack is empty>\n");
    }
    else
    {
        printf("\n<top of stack>");
        NodeStack *node = self->head;
        while (node)
        {
            ValueStack value = node->value;
            printf("\n_________________\n%s", value->toString(value));
            node = node->next;
        }
        printf("\n_________________\n<bottom of stack>\n");
    }
};

Stack *newStack()
{
    Stack *new = malloc(sizeof(Stack));
    new->num_elements = 0;
    new->pop = pop;
    new->push = push;
    new->top = top;
    new->print = print;
    new->is_empty = is_empty;
}

#endif