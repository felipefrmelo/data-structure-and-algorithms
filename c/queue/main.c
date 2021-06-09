#include "stdio.h"
#include "stdlib.h"
#include "queue.c"

Node *_reverseQueue(Node *n)
{

    if (n->next == NULL)
    {
        return n;
    }

    Node *last = _reverseQueue(n->next);
    last->next = n;
    n->next = NULL;
    return n;
}

void reverseQueue(Queue *q)
{
    Node *newTail = _reverseQueue(q->head);

    q->head = q->tail;
    q->tail = newTail;
}


int main(int argc, char const *argv[])
{
    Queue *q = newQueue();
    Value a = 1;
    Value b = 2;
    Value c = 3;
    Value d = 4;
    Value f = 5;
    Value g = 6;

    q->enqueue(q, &a);
    q->enqueue(q, &b);
    q->enqueue(q, &c);
    q->enqueue(q, &d);
    q->enqueue(q, &f);
    q->enqueue(q, &g);
    reverseQueue(q);
    printf("head value %d \n", *q->head->value);
    printf("tail value %d \n", *q->tail->value);
    printf("his size is %d\n", q->size(q));
    printf("dequeue %d\n", *q->dequeue(q));
    printf("dequeue %d\n", *q->dequeue(q));
    printf("dequeue %d\n", *q->dequeue(q));
    printf("dequeue %d\n", *q->dequeue(q));
    printf("dequeue %d\n", *q->dequeue(q));
    printf("dequeue %d\n", *q->dequeue(q));
    
    return 0;
}
