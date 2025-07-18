class Node:

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.left_children = []
        self.right_children = []

    def add_left_child(self, child):
        self.left_children.append(child)
        child.parent = self

    def add_right_child(self, child):
        self.right_children.append(child)
        child.parent = self

    def set_right_children(self, children):
        self.right_children = children
        for child in children:
            child.parent = self

    def set_left_children(self, children):
        self.left_children = children
        for child in children:
            child.parent = self

    def __str__(self):
        return f"Node(name=`{self.name}`, left_children={len(self.left_children)}, right_children={len(self.right_children)})"
