#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After: ");

    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", toupper(s[i]));

        /*if (s[i] >= 'a' && s[i] <= 'z')
        {
            // Change s[i] to uppercase
            //printf("%c", s[i] - 32);

            // If you don't remember the distance between the 'a' to 'A' is equal 32, you can use this method bellow:
            //printf("%c", s[i] - ('a' - 'A'));

            // ctype.h -> toupper()
            printf("%c", toupper(s[i]));
        }
        else
        {
            // Just print s[i]
            printf("%c", s[i]);
        }*/
    }
    printf("\n");
}
