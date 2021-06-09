typedef Node *ValueQueue;

typedef struct NodeQueue
{
    ValueQueue value;
    struct NodeQueue *next;

} NodeQueue;

NodeQueue *newNodeQueue(ValueQueue value);

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

Queue *newQueue();