#include <stdio.h>

int main(){
    char *tokenArr[8];
    for(int i = 0; i < 8; i++){
        tokenArr[i] = "AAA";
    }
    for(int i = 0; i < 8; i++){
       printf("%s\n",tokenArr[i]);
    }
    return 0;
}