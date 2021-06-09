#include "stdio.h"
#include "stdlib.h"

void bubble_sort(int *arr, int size)
{
    int aux, swapped;
    for (size_t n = size - 1; n > 1; n--)
    {
        swapped = 0;
        for (size_t i = 0; i < n; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                aux = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = aux;

                swapped = 1;
            }
        }
        if (!swapped)
            break;
    }
}

void print_arr(int arr[], int size)
{
    printf("\n[");
    for (size_t i = 0; i < size - 1; i++)
    {
        printf("%d, ", arr[i]);
    }
    printf("%d]\n", arr[size - 1]);
}

int main(int argc, char const *argv[])
{
    int wakeup_times[] = {16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45};

    int size = sizeof wakeup_times / sizeof wakeup_times[0];

    bubble_sort(wakeup_times, size);

    print_arr(wakeup_times, size);
    return 0;
}
