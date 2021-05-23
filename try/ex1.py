try:
    n = int(input("숫자를 입력하세요 "))
    print(n)
except ValueError as e:
    print("숫자가 아닙니다.", e)
