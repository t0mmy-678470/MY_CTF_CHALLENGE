#include <stdio.h>
#include <string.h>

int main(){
    char pwd[] = "b48y_rEvEr531S!";
    char input[16];
    printf("Please input password: ");
    scanf("%s", input);
    
    if(!strcmp(pwd, input))
        printf("Here's the flag: NCtfU{%s}\n", pwd);
    else
        printf("Wrong password.\n");

    return 0;
}