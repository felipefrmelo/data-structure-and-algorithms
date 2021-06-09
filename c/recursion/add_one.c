#include "stdio.h"
#include "stdlib.h"
#define ARRAY_SIZE(arr)    (int) (sizeof(arr) / sizeof((arr)[0]))

int length_arr(int *myArray){
    printf("%d\n", ARRAY_SIZE(myArray));
    return ARRAY_SIZE(myArray);
}
int main(int argc, char const *argv[])
{
    int arrs[] = {1, 2, 3, 4, 5};

    printf("%d\n", length_arr(arrs));
    return 0;
}
