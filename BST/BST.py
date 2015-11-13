from collections import deque

class BinarySearchTree(object):

    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

    def insert(self, data):
        if self.data:
            if self.data < data:
                if self.right is None:
                    self.right = BinarySearchTree(data, parent=self)
                else:
                    self.right.insert(data)
            elif self.data > data:
                if self.left is None:
                    self.left = BinarySearchTree(data, parent=self)
                else:
                    self.left.insert(data)
        else:
            self.data = data

    def display(self):
        if not self.data:
            return
        if self.left:
            self.left.display()
        print self.data
        if self.right:
            self.right.display()

    def search(self, data):
        if self.data:
            if self.data == data:
                return self
            if self.data > data:
                if self.left:
                    return self.left.search(data)
                else:
                    return None
            else:
                if self.right:
                    return self.right.search(data)
                else:
                    return None
        else:
            return None

    def min(self):
        if self.data:
            if not self.right and not self.left:
                return self
            else:
                if self.left:
                    return self.left.min()
                return self
        else:
            return None

    def max(self):
        if self.data:
            if not self.right and not self.left:
                return self
            else:
                if self.right:
                    return self.right.max()
                return self
        else:
            return None

    def delete(self, data):
        node = self.search(data)
        if not node.parent:
            left = node.left
            right = node.right
            data = node.data
            root = True
        if node:
            if not node.left and not node.right:
                if not root:
                    if node.parent.left == node:
                        node.parent.left = None
                    elif node.parent.right == node:
                        node.parent.right = None
                else:
                    self.data = None
                    self.left = None
                    self.right = None
            elif node.left and node.right:
                promote_node = node.right.min() or node.left.max()
                node.data = promote_node.data
                if promote_node.parent.left == promote_node:
                    promote_node.parent.left = promote_node.right
                else:
                    promote_node.parent.right = promote_node.right

            else:
                if node.parent.left == node:
                    node.parent.left = node.left
                elif node.parent.right == node:
                    node.parent.right = node.right
        else:
            return None

    def common_ancestor(self, val1, val2):
        node1 = self.search(val1)
        node2 = self.search(val2)

        if not (node1.parent and node2.parent):
            return self

        common_ancestor_node = None
        while node1.parent or node2.parent:
            node1 = node1.parent
            node2 = node2.parent
            if node1 == node2:
                common_ancestor_node = node1
                break
        if not common_ancestor_node:
            return self
        else:
            return common_ancestor_node

    def childern_count(self):

        if self.right and self.left:
            return (2, self.left.data, self.right.data)
        elif self.right or self.left:
            if self.left:
                return (1, self.left.data)
            else:
                return (1, self.right.data)
        else:
            return (0, None, None)

    def level_order_traversal(self):
        orders = deque()
        bfs = []
        if self:
            orders.append((self, self.childern_count()))
        while orders:
            node, children_details = orders.popleft()
            count, left, right = children_details
            bfs.append((node.data, count, left, right))
            if node.left:
                orders.append((node.left, node.left.childern_count()))
            if node.right:
                orders.append((node.right, node.right.childern_count()))
            
        return bfs

    def depth_order_traversal(self):
        orders = []
        dfs = []
        if self:
            orders.append((self, self.childern_count()))
        while orders:
            node, children_details = orders.pop()
            count, left, right = children_details
            dfs.append((node.data, count, left, right))
            if node.left:
                orders.append((node.left, node.left.childern_count()))
            if node.right:
                orders.append((node.right, node.right.childern_count()))
            
        return dfs

def main():
    root = BinarySearchTree(9)
    root.insert(12)
    root.insert(6)
    root.insert(7)
    root.insert(5)
    root.insert(18)
    root.display()
    root.delete(9)
    root.display()
    print root.common_ancestor(12,18)
    print root.common_ancestor(7,5)
    print root.level_order_traversal()
    print root.depth_order_traversal()

if __name__ == '__main__':
    main()

