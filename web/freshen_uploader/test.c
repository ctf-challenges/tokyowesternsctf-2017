#include <stdio.h>
#include <stdlib.h>

int comp(const void *a, const void *b) {
  return *(int*)a - *(int*)b;
}

int main() {
  int n, i;
  int A[1024];

  scanf("%d", &n);
  for(i = 0; i < n; i++) {
    scanf("%d", &A[i]);
  }
  qsort(A, n, sizeof(int), comp);
  for(i = 0; i < n; i++) printf("%d\n", A[i]);

  return 0;
}
