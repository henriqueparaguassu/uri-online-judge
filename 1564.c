#include <stdio.h>
#include <stdlib.h>

int main()
{
  unsigned short int a;

  while (scanf("%hd", &a) != EOF)
  {

    if (a == 0)
    {
      printf("vai ter copa!\n");
    }
    else
    {
      printf("vai ter duas!\n");
    }
  }

  return 0;
}