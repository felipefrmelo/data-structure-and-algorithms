#include "stdio.h"

int factorial(int n)
{
    return n == 0 ? 1 : n * factorial(n - 1);
}

int main(int argc, char const *argv[])
{
    printf("%d \n", factorial(10));

    return 0;
}
