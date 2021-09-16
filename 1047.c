#include <stdio.h>
#include <stdlib.h>

int calc_dif(int inicio, int fim)
{
  return inicio - fim;
}

int main()
{
  int h_inicial, min_inicial, h_final, min_final;

  scanf("%d %d %d %d", &h_inicial, &min_inicial, &h_final, &min_final);

  h_inicial *= 60;
  h_final *= 60;

  int dif = (h_final + min_final) - (h_inicial + min_inicial);

  if (dif == 0)
  {
    printf("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)\n");
  }
  else if (dif < 0)
  {
    int h = (1440 - abs(dif)) / 60;
    int min = (1440 - abs(dif)) % 60;
    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", h, min);
  }
  else
  {
    int h = dif / 60;
    int min = dif % 60;
    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", h, min);
  }

  return 0;
}