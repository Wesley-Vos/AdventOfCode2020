
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data) + " and next is " + str(self.next.data)


class CircularLinkedList:
    def __init__(self, elements):
        self.head = None
        self.tail = None
        self.node_map = {}
        self.length = 0
        self.min_val = 10000000
        self.max_val = 0
        self._insert(elements)

    def _insert(self, elements):
        for element in elements:
            self.length += 1
            self.min_val = min(self.min_val, element)
            self.max_val = max(self.max_val, element)
            ptr = Node(element)
            if self.head == None:
                self.head = ptr
                self.tail = ptr
                ptr.next = self.head
            else:
                self.tail.next = ptr
                self.tail = ptr
                self.tail.next = self.head
            self.node_map[element] = ptr

    def __len__(self):
        return self.length

    def remove_at(self, start_idx, end_idx):
        pass

    def __str__(self):
        tmp = self.head
        string = ""
        while tmp.next != self.head:
            string += str(tmp.data)
            tmp = tmp.next
        string += str(tmp.data)
        return string


class RotateCups:
    def __init__(self, config):
        self.cups = CircularLinkedList(config)
        self.cur = self.cups.head
        self.picked_cups = []
        self.picked_data = []

    def __str__(self):
        return str(self.cups)

    def _pick_cups(self):
        self.picked_cups = [self.cur.next,
                            self.cur.next.next, self.cur.next.next.next]
        self.picked_data = [cup.data for cup in self.picked_cups]

    def move(self):
        self._pick_cups()
        label = self.cur.data - 1
        while label in self.picked_data or label == 0:
            label -= 1
            label = self.cups.max_val if label < self.cups.min_val else label

        des = self.cups.node_map[label]
        self.cur.next = self.picked_cups[2].next
        self.picked_cups[2].next = des.next
        des.next = self.picked_cups[0]
        self.cur = self.cur.next


def play(config, moves, part):
    config = [int(c) for c in str(config)]
    if part == 2:
        config += [i for i in range((max(config) + 1), 1000001)]

    cups = RotateCups(config)

    for _ in range(moves):
        cups.move()

    cur = cups.cups.node_map[1].next
    if part == 1:
        output = ""
        while cur.data != 1:
            output += str(cur.data)
            cur = cur.next
        return output
    elif part == 2:
        return cur.data * cur.next.data
    return "Problem, no right part given"


def main():
    config = 398254716
    test_config = 389125467
    print("Test 1:", play(test_config, 10, 1))
    print("Part 1:", play(config, 100, 1))
    print("Test 2:", play(test_config, 10000000, 2))
    print("Part 2:", play(config, 10000000, 2))


if __name__ == "__main__":
    main()
