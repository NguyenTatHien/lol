import random
class BST:
    class __Node:
        def __init__(self, value):
            self.data = value
            self.left = self.right = None

    def __init__(self):
        self.__root = None

    def __preOrder(self, root, x):
        if root is not None:
            x.append(root.data)
            self.__preOder(root.left, x)
            self.__preOder(root.right, x)

    def preOrder(self):
        x = []
        self.__preOrder(self.__root, x)
        return x

    def __inOrder(self, root, x):
        if root is not None:
            self.__inOrder(root.left, x)
            x.append(root.data)
            self.__inOrder(root.right, x)

    def inOrder(self):
        x = []
        self.__inOrder(self.__root, x)
        return x
    
    def __postOrder(self, root, x):
        if root is not None:
            self.__postOrder(root.left, x)
            self.__postOrder(root.right, x)
            x.append(root.data)

    def postOrder(self):
        x = []
        self.__postOrder(self.__root, x)
        return x

    def insert(self, value):
        if self.__root is None:
            self.__root = self.__Node(value)
        else:
            self.__insert(self.__root, value)

    def __printLevel(self, root, level):
        if root is None:
            return ''
        s = self.__printLevel(root.right, level + 1)
        s += f'{level:2}' + ' '.rjust(5 * level, ' ') + str(root.data) + '\n'
        s += self.__printLevel(root.left, level + 1)
        return s

    def printLevel(self):
        return self.__printLevel(self.__root, 0)

def main():
    t = BST()
    n = int(input("Nhập số lượng phần tử: "))
    print("Các số phát sinh ngẫu nhiên: ", end="")
    for i in range(n):
        x = random.randint(-30, 50)
        t.insert(x)
        print(x, end=' ')
    print()
    print(f'Duyệt LNR: {t.inOrder()}')
    print(t.printLevel())

if __name__ == "__main__":
    main()