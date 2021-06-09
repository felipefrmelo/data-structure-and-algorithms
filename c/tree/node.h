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

Node *newNode(Value value);
