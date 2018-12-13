class Node():
    def __init__(self, num_children, num_metadata):
        self.children = [None] * num_children
        self.metadata = [None] * num_metadata

    def add_child(self, node):
        for index, child in enumerate(self.children):
            if child is None:
                self.children[index] = node
                return True
            else:
                if child.add_child(node):
                    return True
        return False

    def add_metadata(self, value):
        for index, child in enumerate(self.children):
            if child is not None and child.add_metadata(value):
                return True

        for data_index, data_slot in enumerate(self.metadata):
            if data_slot is None:
                self.metadata[data_index] = value
                return True

        return False

    def expecting(self):
        for child in self.children:
            if child is not None and child.expecting():
                return child.expecting()

        if None in self.children:
            return 'header'
        elif None in self.metadata:
            return 'metadata'
        else:
            return None

    def sum_metadata(self):
        total = sum(self.metadata)
        for child in self.children:
            if child is not None:
                total += child.sum_metadata()
        return total

    def sum_by_reference(self):
        total = 0
        if len(self.children) == 0:
            total = sum(self.metadata)
        else:
            for value in self.metadata:
                if len(self.children) >= value:
                    total += self.children[value - 1].sum_by_reference()

        return total


def load():
    return [
        int(val)
        for line in open('input.txt', 'r')
        for val in line.strip().split()
    ]


input = load()
expecting = 'header'
index = 0
root = None

while index < len(input):
    if expecting == 'header':
        children = input[index]
        metadata = input[index + 1]
        index += 2
        if root is None:
            root = Node(children, metadata)
        else:
            root.add_child(Node(children, metadata))
    elif expecting == 'metadata':
        value = input[index]
        index += 1
        root.add_metadata(value)

    expecting = root.expecting()

print('Part 1:', root.sum_metadata())
print('Part 2:', root.sum_by_reference())
