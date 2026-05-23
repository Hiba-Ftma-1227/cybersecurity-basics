#include <stdio.h>
#include <string.h>

int main() {

    char text[100];
    int i;

    printf("Enter message: ");
    scanf("%s", text);

    for(i = 0; text[i] != '\0'; i++) {
        text[i] = text[i] + 3;
    }

    printf("Encrypted Message: %s\n", text);

    return 0;
}
