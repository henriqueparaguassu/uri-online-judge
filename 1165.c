#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int isprimo(int numero)
{
  if ((numero != 0) && (numero != 1))
  {
    if (numero > 3)
    {
      for (int i = 2; i < (int)(pow(numero, 0.5) + 1); i++)
      {
        if (numero % i == 0)
        {
          return -1;
          break;
        }
      }
    }
    return 0;
  }
  return -1;
}

int main()
{
  int n;
  int a;

  scanf("%d", &n);

  for (int i = 0; i < n; i++)
  {
    scanf("%d", &a);
    printf("%d %s", a, isprimo(a) ? "nao eh primo\n" : "eh primo\n");
  }

  return 0;
}