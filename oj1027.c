#include<stdio.h>
#include<math.h>
int main()
{
    int number,number_1,number_2,number_3;
    scanf("%d",&number);
    number_1 = number % 10;
    number_2 = (number / 10) % 10;
    number_3 = (number / 100) % 10;
    if (number == pow(number_1,3) + pow(number_2,3) + pow(number_3,3))
    {
        printf("yes");
    }
    else
    {
        printf("no");
    }
}