#include <stdio.h>
#include <stdlib.h>

float calc_percent(float qnt, float total)
{
  return (qnt * 100 / total);
}

int main()
{
  int n, qnt;
  char tipo;
  int coelhos, ratos, sapos;
  coelhos = ratos = sapos = 0;

  scanf("%d", &n);

  for (int i = 0; i < n; i++)
  {
    scanf("%d %c", &qnt, &tipo);

    switch (tipo)
    {
    case 'R':
      ratos += qnt;
      break;
    case 'S':
      sapos += qnt;
      break;
    case 'C':
      coelhos += qnt;
      break;
    }
  }

  int total = sapos + ratos + coelhos;

  printf("Total: %d cobaias\n", total);
  printf("Total de coelhos: %d\n", coelhos);
  printf("Total de ratos: %d\n", ratos);
  printf("Total de sapos: %d\n", sapos);
  printf("Percentual de coelhos: %.2f %%\n", calc_percent(coelhos, total));
  printf("Percentual de ratos: %.2f %%\n", calc_percent(ratos, total));
  printf("Percentual de sapos: %.2f %%\n", calc_percent(sapos, total));

  return 0;
}