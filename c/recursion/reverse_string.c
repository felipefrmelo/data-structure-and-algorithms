#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "reverse_string.h"

char *reverse_string(const char *string)
{
    int lengthString = strlen(string);
    char *reversed_substring = malloc(sizeof(char) * lengthString);
    char *sub_string = malloc(sizeof(char) * lengthString);

    if (lengthString == 0)
    {
        return "";
    }

    strcpy(sub_string, string + 1);
    strcpy(reversed_substring, reverse_string(sub_string));
    return strncat(reversed_substring, string, 1);
}

int main(int argc, char const *argv[])
{
    if (argc > 1)
    {
        int lengthString = 0;
        for (size_t i = 1; i < argc; i++)
        {
            lengthString += strlen(argv[i]) + 1;
        }

        char *s = malloc(sizeof(char) * lengthString);
        char *args = malloc(sizeof(char) * lengthString);

        for (size_t i = 1; i < argc; i++)
        {
            strcat(args, argv[i]);
            strcat(args, " ");
            strcat(s, reverse_string(argv[i]));
            strcat(s, " ");
        }

        printf("string: %s \t reversed: %s\n", args, s);
        free(s);
        free(args);
    }
    else
    {
        printf("Passe o texto como argumento\n");
    }
    return 0;
}
