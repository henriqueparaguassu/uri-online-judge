#include <stdio.h>
#include <stdlib.h>

int main()
{
  int a, b;
  scanf("%d %d", &a, &b);

  printf("%d %d\n", (int)(a / b), a % b);

  return 0;
}