#include <stdio.h>
#include <stdlib.h>

int main()
{
  char nome[50];
  char tipo;
  int a, e, h, m, x;
  a = e = h = m = x = 0;
  int n;

  scanf("%d", &n);

  for (int i = 0; i < n; i++)
  {
    scanf("%s %c", nome, &tipo);

    switch (tipo)
    {
    case 'A':
      a++;
      break;
    case 'E':
      e++;
      break;
    case 'M':
      m++;
      break;
    case 'H':
      h++;
      break;
    case 'X':
      x++;
      break;
    }
  }

  printf("%d Hobbit(s)\n", x);
  printf("%d Humano(s)\n", h);
  printf("%d Elfo(s)\n", e);
  printf("%d Anao(s)\n", a);
  printf("%d Mago(s)\n", m);

  return 0;
}