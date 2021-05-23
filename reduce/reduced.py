from functools import reduce

n = int(input("팩토리얼을 구할게여 원하는 숫자를 대입하세요 "))
lst = list(range(1, n+1))
lst = reduce(lambda a, b: a*b, lst)

print(f'1부터 {n} 까지의 팩토리얼 값은 {lst} 입니다.')
