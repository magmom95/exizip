class parent_class1:
    def parent1(self):
        print('부모 클래스1 입니다.')


class parent_class2:
    def parent2(self):
        print('부모 클래스2 입니다.')


class child_class(parent_class1, parent_class2):
    def child(self):
        print('자식 클래스 입니다.')


test = child_class()


test.child()
test.parent2()
test.parent1()
