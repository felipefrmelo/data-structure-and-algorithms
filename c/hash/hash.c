#include "stdlib.h"
#include "string.h"
#include "hash.h"
#include "stdio.h"

LinkedListNode *newLinkedList(char *key, int value)
{
    LinkedListNode *result = malloc(sizeof(LinkedListNode));
    result->key = key;
    result->value = value;
    result->next = NULL;
    return result;
}

void _rehash(struct Hash *self)
{
    int old_num_buckets = self->bucket_size;
    LinkedListNode **old_bucket_array = self->bucket_array;

    int num_buckets = 2 * old_num_buckets;
    self->bucket_array = malloc(sizeof(LinkedListNode) * num_buckets);
    self->bucket_size = num_buckets;

    for (size_t i = 0; i < old_num_buckets; i++)
    {
        LinkedListNode *head = old_bucket_array[i];
        while (head != NULL)
        {
            self->put(self, head->key, head->value);
            head = head->next;
        }
    }
}

void put(struct Hash *self, char *key, int value)
{
    int bucket_index = self->get_bucket_index(self, key);
    LinkedListNode *new_node = newLinkedList(key, value);
    LinkedListNode *head = self->bucket_array[bucket_index];

    while (head != NULL)
    {
        if (head->key == key)
        {
            head->value = value;
            return;
        }
        head = head->next;
    }

    head = self->bucket_array[bucket_index];
    new_node->next = head;
    self->bucket_array[bucket_index] = new_node;
    self->num_entries += 1;

    double current_load_factor = (double)self->num_entries / self->bucket_size;

    if (current_load_factor > self->load_factor)
    {

        self->num_entries = 0;
        _rehash(self);
    }
}

int get(struct Hash *self, char *key)
{
    int bucket_index = self->get_bucket_index(self, key);
    LinkedListNode *head = self->bucket_array[bucket_index];

    while (head != NULL)
    {
        if (head->key == key)
            return head->value;

        head = head->next;
    }

    return -1;
}

int size(Hash *self)
{
    return self->num_entries;
}

int get_bucket_index(struct Hash *self, char *string)
{
    return self->get_hash_code(self, string);
}

int get_hash_code(struct Hash *self, char *string)
{
    int current_coefficient = 1, hash_code = 0;

    int num_buckets = self->bucket_size;

    for (size_t i = 0; i < strlen(string); i++)
    {
        hash_code += (int)string[i] * current_coefficient;
        hash_code = hash_code % num_buckets;
        current_coefficient *= self->p;
        current_coefficient = current_coefficient % num_buckets;
    }

    return hash_code % num_buckets;
}

void delete (struct Hash *self, char *key)
{
    int bucket_index = self->get_bucket_index(self, key);

    LinkedListNode *head = self->bucket_array[bucket_index];

    LinkedListNode *previous = malloc(sizeof(LinkedListNode));
    previous = NULL;
    while (head != NULL)
    {
        if (head->key == key)
        {
            if (previous == NULL)
            {
                self->bucket_array[bucket_index] = head->next;
            }
            else
            {
                previous->next = head->next;
            }
            self->num_entries--;
            return;
        }
        else
        {
            previous = head;
            head = head->next;
        }
    }
}

Hash *newHash()
{

    Hash *hash = (struct Hash *)malloc(sizeof(Hash));
    hash->bucket_array = malloc(sizeof(LinkedListNode) * INITIAL_SIZE);
    hash->p = 31;
    hash->get_bucket_index = get_bucket_index;
    hash->get_hash_code = get_hash_code;
    hash->num_entries = 0;
    hash->put = put;
    hash->get = get;
    hash->size = size;
    hash->load_factor = 0.7;
    hash->bucket_size = INITIAL_SIZE;
    hash->delete = delete;
}
