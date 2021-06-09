#define LEN(x) (sizeof(x) / sizeof(x[0]))
#define INITIAL_SIZE 10

typedef struct LinkedListNode
{
    char *key;
    int value;
    struct LinkedListNode *next;
} LinkedListNode;

typedef struct Hash
{
    int p;
    int num_entries;
    void (*put)(struct Hash *, char *, int);
    void (*delete)(struct Hash *, char *);
    int (*get)(struct Hash *, char *);
    LinkedListNode **bucket_array;
    int (*get_bucket_index)(struct Hash *, char *);
    int (*get_hash_code)(struct Hash *, char *);
    int (*size)(struct Hash *);
    double load_factor;
    int bucket_size;
} Hash;

Hash *newHash();