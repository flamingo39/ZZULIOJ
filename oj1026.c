#include<stdio.h>
int main()
{
    printf("请输入一个字符: ");
    char c;
    scanf("%c",&c);
    if (c >= 'A' && c <= 'Z')
    {
        printf("upper");
    }
    else if (c >= 'a' && c <= 'z')
    {
        printf("lower");
    }
    else if (c >= '0' && c <= '9')
    {
        printf("digit");
    }
    else
    {
        printf("other");
    }
}