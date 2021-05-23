try:
    n1, n2 = map(int, input("나눗셈 계산기입니다. 나눌 두수를 입력해주세요 ").split())
except ZeroDivisionError as e:
    print(f'{0}으로 나누면 안됩니다.', e)
else:
    print(f'{n1/n2}')
