#include <stdio.h>
#include <string.h>
// NCtfU{0HnO_Y0U_p4TCH3d_i7}
void get_flag() {
    char input[] = "\x2d\x20\x17\x5\x36\x18\x53\x2b\xd\x2c\x3c\x3a\x53\x36\x3c\x13\x57\x37\x20\x2b\x50\x7\x3c\xa\x54\x1e";
    char output[30];
    for (int i = 0; i < strlen(input); i++) {
        output[i] = input[i] ^ 0x63;
    }
    output[strlen(input)] = '\0';
    printf("%s\n", output);
}

int main(){

    if(1){
        printf("HaHa, I hid the flag.");
    }
    else{
        get_flag();
    }
}