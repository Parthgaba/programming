class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self, node, st):
        if node.left is None and node.right is None:
            return "Node( \""+node.val+"\" )"
        if node.left is not None:
            st+= "Node( \""+node.val+"\", "+self.serialize(node.left, st)+", "
        if node.right is not None:
            st+= self.serialize(node.right, st)+" )"
        return st

    def Inorder(self, root):
        if root:
            self.Inorder(root.left)
            print(root.val,end=" ")
            self.Inorder(root.right)

    def deserialize(self, ser_st):
        return eval(ser_st)

string = ""
node = Node('1')
node.left = Node('2')
node.right = Node('3')
node.left.left = Node('4')
node.left.right = Node('5')
string = node.serialize(node,string)
print("\n")
print('Before serializing:', end=" ")
node.Inorder(node)
print("\n")
print('Serialized string:', end=" ")
print(string)
print("\n",end=" ")
node1 = node.deserialize(string)
print('After Deserializing:', end=" ")
node1.Inorder(node1)
print("\n")