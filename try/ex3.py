try:
    lst = [10, 20, 30]

    index, n = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())

    print(f'{lst[index]//n}')
except IndexError as e:
    print(e)

finally:
    print("야는 무조건 나와야된다 ㅇㅈ?")
