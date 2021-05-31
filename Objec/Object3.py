from abc import *

# 추상 클래스


class Jobs(metaclass=ABCMeta):

    # 추상 메소드
    @abstractmethod
    def stats(self):
        pass

    @abstractmethod
    def item(self):
        pass


class Warrior(Jobs):
    def stats(self, str, dex, int, luk, ad, ap):
        self.str = str
        self.dex = dex
        self.int = int
        self.luk = luk
        self.ad = ad
        self.ap = ap
        print('전사 직업 능력치')
        print(f'힘: {self.str}')
        print(f'민첩: {self.dex}')
        print(f'지력: {self.int}')
        print(f'운: {self.luk}')
        print(f'물리 공격력: {self.ad}')
        print(f'마법 공격력: {self.ap}')

    def item(self):
        print('소지중인 아이템: 검')


class Wizard(Jobs):
    def stats(self, str, dex, int, luk, ad, ap):
        self.str = str
        self.dex = dex
        self.int = int
        self.luk = luk
        self.ad = ad
        self.ap = ap
        print('마법사 직업 능력치')
        print(f'힘: {self.str}')
        print(f'민첩: {self.dex}')
        print(f'지력: {self.int}')
        print(f'운: {self.luk}')
        print(f'물리 공격력: {self.ad}')
        print(f'마법 공격력: {self.ap}')

    def item(self):
        print('소지중인 아이템: 지팡이')


class Archer(Jobs):
    def stats(self, str, dex, int, luk, ad, ap):
        self.str = str
        self.dex = dex
        self.int = int
        self.luk = luk
        self.ad = ad
        self.ap = ap
        print('궁수 직업 능력치')
        print(f'힘: {self.str}')
        print(f'민첩: {self.dex}')
        print(f'지력: {self.int}')
        print(f'운: {self.luk}')
        print(f'물리 공격력: {self.ad}')
        print(f'마법 공격력: {self.ap}')

    def item(self):
        print('소지중인 아이템: 활')


# 전사 능력치
test1 = Warrior()
test1.stats(30, 10, 10, 10, 40, 10)
# 전사가 소지중인 아이템
test1.item()

# 마법사 능력치
test2 = Wizard()
test2.stats(10, 10, 30, 10, 10, 50)
# 마법사가 소지중인 아이템
test2.item()

# 궁수 능력치
test3 = Archer()
test3.stats(10, 30, 10, 10, 50, 10)
# 궁수가 소지중인 아이템
test3.item()
