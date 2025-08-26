#include <stdio.h>
#include <stdlib.h>
void safe_malloc(int size) {}
int main() {
    char user_input[] = "Hello from user";
    int size1 = 2000000000;
    int size2 = 2000000000;
    printf("%s\n", user_input);
    printf(user_input);
    safe_malloc(size1 + size2);
    return 0;
}