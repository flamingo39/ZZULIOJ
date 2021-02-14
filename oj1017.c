#include<stdio.h>
#include<math.h>
int main()
{
    int i;
    int num;
    int count = 0;

    scanf("%d",&num);
    while(num > 0)
    {
        num /=  10;
        ++ count; //前置++，和后置++，谁在前，先干嘛
    }
    printf("%d",count);
    return 0;
}