#include <stdio.h>
#include <stdlib.h>

int main()
{
  int a, b;
  int soma = 0;

  scanf("%d %d", &a, &b);

  while ((a > 0) && (b > 0))
  {
    if (a < b)
    {
      for (int i = a; i <= b; i++)
      {
        printf("%d ", i);
        soma += i;
      }
    }
    else
    {
      for (int i = b; i <= a; i++)
      {
        printf("%d ", i);
        soma += i;
      }
    }
    printf("Sum=%d\n", soma);
    scanf("%d %d", &a, &b);
    soma = 0;
  }

  return 0;
}