#include <stdio.h>
#include <string.h>

void transform(char *input, char *output) {
    for (int i = 0; i < strlen(input); i++) {
        output[i] = input[i] ^ 0x63;
    }
    output[strlen(input)] = '\0';
}

int main(){
    char flag[] = "\x0a\x54\x44\x56\x3c\x47\x54\x2a\xf\xf\x3c\x22\x3c\x1\x22\x21\x1a\x0";
    char input[18];
    transform(flag, flag);
    printf("Please input password: ");
    scanf("%s", input);

    if(!strcmp(flag, input))
        printf("Here's the flag: NCtfU{%s}\n", input);
    else
        printf("Wrong password.\n");
        
    return 0;
}

