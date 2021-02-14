money = int(input())
if money < 500:
    print('%.2f' % money)
elif money >= 500 and money <= 1000:
    print('%.2f' % (money * 0.95))
elif money >= 1000 and money < 3000:
    print('%.2f' % (money * 0.9))
elif money >= 3000 and money < 5000:
    print('%.2f' % (money * 0.85))
elif money >= 5000:
    print('%.2f' % (money * 0.8))
