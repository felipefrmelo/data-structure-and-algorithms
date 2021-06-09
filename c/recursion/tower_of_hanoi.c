#include "stdio.h"
#include "stdlib.h"

int count = 0;

void tower_of_hanoi(int size, char source, char aux, char dest)
{
    count++;

    if (size == 1)
        printf("move o disco 1 da haste %c para %c\n", source, dest);

    else
    {
        tower_of_hanoi(size - 1, source, dest, aux);
        printf("move o disco %d da haste %c para %c\n", size, source, dest);

        tower_of_hanoi(size - 1, aux, source, dest);
    }
}

int main(int argc, char const *argv[])
{
   
    tower_of_hanoi(19, 'S', 'A', 'D');
    printf("\nnumero de movimentos %d\n\n", count);
    return 0;
}
