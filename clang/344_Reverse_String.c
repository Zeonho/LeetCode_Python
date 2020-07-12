#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}


int main() {
    int a = 5;
    int b = 10;
    swap(&a, &b);
    printf("a:%d, b:%d\n", a, b);
    int aArray[] = {1, 2, 3, 4, 5, 6};
    int *l = aArray;
    int *r = aArray + 6 - 1;
    while (l < r) {
        swap(l, r);
        l++;
        r--;
    }

    // printf("%d %d\n", *l, *r);
    for (int i = 0; i < 6; i++) {
        printf("%d ", aArray[i]);
    }
    printf("\n");
    return 0;
}