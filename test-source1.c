#include <stdio.h>
#include <string.h>

int main() {
    char src[10] = "Hello";
    char dest[10];

    strcpy(dest, src); // <- This should trigger the rule!

    printf("%s\n", dest);
    return 0;
}
