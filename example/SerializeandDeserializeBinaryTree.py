# Сериализация — это процесс преобразования структуры данных или объекта в последовательность битов, 
# чтобы их можно было сохранить в файле или буфере памяти или передать по сетевому соединению 
# для последующего восстановления в той же или другой компьютерной среде.

# Разработайте алгоритм для сериализации и десериализации бинарного дерева. Нет ограничений на то, как алгоритм сериализации/десериализации должен работать. 
# Нужно просто гарантировать, что бинарное дерево может быть сериализовано в строку, и эта строка может быть десериализована в исходную структуру дерева.

"""
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
"""

class TreeNode:
    def __init__(self, val=0, left=None, rigth=None):
        self.val = val
        self.left = left
        self.rigth = rigth


class Codec:
    def rserialize(self, root, string):
        if root is None:
            string += "None,"
        else:
            string += str(root.val) + ","
            string = self.rserialize(root.left, string)
            string = self.rserialize(root.right, string)
        return string

    def serialize(self, root):
        return self.rserialize(root, "")

    def rdeserialize(self, data_list):
        if data_list[0] == "None":
            data_list.pop(0)
            return None

        root = TreeNode(int(data_list.pop(0)))
        root.left = self.rdeserialize(data_list)
        root.right = self.rdeserialize(data_list)
        return root

    def deserialize(self, data):
        data_list = data.split(',')
        return self.rdeserialize(data_list)

if __name__ == "__main__":
    example = Codec()
    res = example.serialize(root = [1,2,3,None,None,4,5])
    print(res)