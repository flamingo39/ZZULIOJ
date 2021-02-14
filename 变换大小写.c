#include <stdio.h>
int main()
{
    char c;
    printf("输入一个字母\n");
    scanf("%c", &c);
    if (c >= 'a' && c <= 'z')
    {
        printf("其大写字母为:%c\n", c - 32);
    }
    else if (c >= 'A' && c <= 'Z')
    {
        printf("其小写字母为:%c\n", c + 32);
    }
    else
    {
        printf("脑瘫字母都能输歪来\n");
    }
}