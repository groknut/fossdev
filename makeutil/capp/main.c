

#include <stdio.h>
#include <time.h>

int main() {
    time_t now = time(NULL);
    printf("Hello\n");
    printf("Run time: %td\n", now);
    return 0;
}

