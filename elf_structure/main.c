#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "pwd.h"

void encrypt(char *input, char *output, int key) {
    for (int i = 0; i < strlen(input); i++) {
        // 混合位移和數學操作
        output[i] = ((input[i] ^ key) + (i * key) - 7) & 0xFF;
    }
    output[strlen(input)] = '\0';
}

void decrypt(char *input, char *output, int key) {
    for (int i = 0; i < strlen(input); i++) {
        // 解密，逆轉加密的操作
        output[i] = ((input[i] & 0xFF) + 7 - (i * key)) ^ key;
    }
    output[strlen(input)] = '\0';
}

int main(){
    char* enc_flag = "G<m_Nt.a9k,XeB1k:kRXLA-k,XfRXl,<K>0v";
    // char* flag = (char*) malloc(sizeof(char) * (1+strlen(enc_flag)));
    int const flag_len = strlen(enc_flag)+1;
    char flag[40];
    // printf("enc = %s\ndec = %s\n", enc_flag, flag);
    char* pwd = get_pwd();
    char* auth = "share library share my secret too";
    if( !strcmp(pwd, auth) ){
        decrypt(enc_flag, flag, 0);
        printf("%s\n",flag);
    }
    else{
        printf("Wrong password.\n");
    }
    // printf("%ld", strlen("123"));
}