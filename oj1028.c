#include<stdio.h>
int main()
{
    int num;
    scanf("%d",&num);
    if (num % 4 == 0 && num % 100 != 0)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }
}