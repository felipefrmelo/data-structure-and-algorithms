#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef char *Value;

typedef struct Node
{
    Value value;
    struct Node *left;
    struct Node *right;
    void (*set_value)(struct Node *, Value);
    void (*set_left_child)(struct Node *, struct Node *);
    void (*set_right_child)(struct Node *, struct Node *);
    int (*has_left_child)(struct Node *);
    int (*has_right_child)(struct Node *);
    char *(*toString)(struct Node *);
} Node;

void set_value(struct Node *self, Value value)
{
    strcpy(self->value, value);
};

void set_left_child(struct Node *self, struct Node *left)
{
    self->left = left;
}

void set_right_child(struct Node *self, struct Node *right)
{
    self->right = right;
}

int has_left_child(struct Node *self)
{
    return self->left != NULL;
};

int has_right_child(struct Node *self)
{
    return self->right != NULL;
};

char *toString(struct Node *self)
{
    char *str = malloc(strlen(self->value) + 100);
    strcat(str, "Node(");
    strcat(str, self->value);
    strcat(str, ")");
    return str;
};

Node *newNode(Value value)
{
    Node *new = malloc(sizeof(Node));
    new->value = malloc(strlen(value));
    strcpy(new->value, value);
    new->set_value = set_value;
    new->set_left_child = set_left_child;
    new->set_right_child = set_right_child;
    new->has_left_child = has_left_child;
    new->has_right_child = has_right_child;
    new->toString = toString;

    return new;
}
