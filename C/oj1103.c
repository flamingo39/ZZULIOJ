#include <stdio.h>
#include <math.h>
int GP(int n);
int main()
{
    int n, m, ncase;
    scanf("%d", &ncase);
    double sum1 = 0, sum2 = 0;
    while (ncase--)
    {
        scanf("%d%d", &m, &n);
        sum1 += GP(n) * m;
        sum2 += m;
    }
    printf("%.1f", sum1 / sum2);

    return 0;
}
int GP(int n)
{
    if (n < 60)
        return 0;
    else
        return (n - 50) / 10;
}