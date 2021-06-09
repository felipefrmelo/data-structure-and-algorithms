#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define isPalindrome(n) is_palindrome(n) ? "true": "false"

int is_palindrome(char *string)
{
    int lengthString = strlen(string);

    if (lengthString <= 1)
    {
        return 1;
    }
    char *subString = malloc(sizeof(char) * lengthString);
    subString = strncpy(subString, string + 1, lengthString - 2);
    char fistChar, lastChar;
    fistChar = string[0];
    lastChar = string[lengthString - 1];
    return fistChar == lastChar && is_palindrome(subString);
}

int main(int argc, char const *argv[])
{
    printf("is palindrome %s\n", isPalindrome("ufu"));
    printf("is palindrome %s\n", isPalindrome("a"));
    printf("is palindrome %s\n", isPalindrome("madam"));
    printf("is palindrome %s\n", isPalindrome("abba"));
    printf("is palindrome %s\n", isPalindrome("udacitu"));
    printf("is palindrome %s\n", isPalindrome("udachadu"));
    return 0;
}
