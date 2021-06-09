#include "hash.h"
#include "stdlib.h"
#include "string.h"
#include "stdio.h"

int main(int argc, char const *argv[])
{
    Hash *hash_map = newHash();
    hash_map->put(hash_map, "one", 1);
    hash_map->put(hash_map, "two", 2);
    hash_map->put(hash_map, "three", 33);
    // hash_map->put(hash_map, "neo", 11);
    // hash_map->put(hash_map, "abc", 1);
    // hash_map->put(hash_map, "acc", 2);
    // hash_map->put(hash_map, "fgd", 3);
    // hash_map->put(hash_map, "asa", 11);
    printf("size: %d\n", hash_map->size(hash_map));
    printf("one: %d\n", hash_map->get(hash_map, "one"));
    printf("neo: %d\n", hash_map->get(hash_map, "neo"));
    printf("three: %d\n", hash_map->get(hash_map, "three"));

    // hash_map->delete (hash_map, "one");
    hash_map->delete (hash_map, "two");
    printf("\nsize: %d\n", hash_map->size(hash_map));
    printf("one: %d\n", hash_map->get(hash_map, "one"));
    printf("two: %d\n", hash_map->get(hash_map, "two"));
    printf("three: %d\n", hash_map->get(hash_map, "three"));


    return 0;
}
