#include <stdio.h>
#include <stdlib.h>
void safe_malloc(int size) {}
void clean_string(char* s) {}
void smart_null_test(char* smart_ptr){
    if(smart_ptr != NULL){
        smart_ptr[0] = 'A';
    }
    else {
        smart_ptr[0] = 'B';
    }

}
struct MyStruct{
int data;
};
int get_user_size(){
return 200;
}
void null_pointer_test() {
    struct MyStruct* dangling_ptr = NULL;
    int value;
    value = dangling_ptr->data;
}
void memory_operations(){
    FILE* a = _popen("ls", NULL);
    char* ptr1 = (char*)malloc(10);
    char* ptr2 = (char*)malloc(10);
    char* abcd = (char*)malloc(10);
    free(ptr1);
    printf("ptr1 was freed");
    free(ptr2);
    ptr2 = NULL;
    free(ptr2);
}
int main() {
    char user_input[] = "Hello from user";
    char unsafe_buffer[100];
    char safe_buffer[100];
    char final_dest[100];
    int size = 2147483647;
    int sizePrime = 2147483647;
    int efgh = malloc(200);
    scanf("%s", unsafe_buffer);
    strcpy(safe_buffer, unsafe_buffer);
    strcpy(final_dest, safe_buffer);
    clean_string(safe_buffer);
    strcpy(final_dest, safe_buffer);
    printf("%s\n", user_input);
    printf(user_input);
    safe_malloc(size + sizePrime);
    memory_operations();
    null_pointer_test();
    int size1 = 2000000000;
    int size2 = 2000000000;
    safe_malloc(size1+size2);
    int user_size = get_user_size();
    safe_malloc(size1+user_size);
    int small_size = 100;
    safe_malloc(size1+small_size);

    char* p1 = (char*)malloc(10);
    char* p2 = NULL;
    smart_null_test(p1);
    smart_null_test(p2);
    return 0;
}
