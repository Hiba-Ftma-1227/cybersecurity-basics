#include <stdio.h>

int main() {

    int port;

    printf("Enter port number: ");
    scanf("%d", &port);

    if(port == 80) {
        printf("HTTP Port\n");
    }
    else if(port == 443) {
        printf("HTTPS Port\n");
    }
    else if(port == 22) {
        printf("SSH Port\n");
    }
    else {
        printf("Unknown or Custom Port\n");
    }

    return 0;
}
