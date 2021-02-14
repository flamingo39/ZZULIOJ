#include<stdio.h>
int main()
{
    char a,b,c,max;
    scanf("%c %c %c",&a,&b,&c);
    if (c > b)
    {
        max = c;
        b = c;
        b = max;
    }
    if (b > a)
    {
        max = b;
        a = b;
        a = max;
    }
    printf("%c",a);
}