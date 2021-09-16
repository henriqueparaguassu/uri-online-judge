#include <stdio.h>

int main()
{
  int a, b, c, maior;
  scanf("%d %d %d", &a, &b, &c);
  if ((a > b) && (a > c))
  {
    printf("%d eh o maior\n", a);
  }
  else if ((c > b) && (c > a))
  {
    printf("%d eh o maior\n", c);
  }
  else if ((b > c) && (b > a))
  {
    printf("%d eh o maior\n", b);
  }
}