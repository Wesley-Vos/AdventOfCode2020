
from collections import deque
from itertools import islice


class RotatingCups():
    def __init__(self, input):
        self.cups = deque([int(c) for c in str(input)])
        self.picked_cups = []
        self.min_cup = min(self.cups)
        self.idx = 0

    def __str__(self):
        return self._output(list(self.cups))

    def _output(self, output_val):
        return "".join(list(map(str, output_val)))

    def _pick_cups(self):
        # self.picked_cups = self.cups[(self.idx + 1):(self.idx + 4)]
        self.picked_cups = list(
            islice(self.cups, (self.idx + 1), (self.idx + 4)))

        if self.idx + 3 >= len(self.cups):
            print(3 - len(self.picked_cups), "too less")
            self.picked_cups += list(islice(self.cups,
                                            0, 3 - len(self.picked_cups)))

        print("Picked cups:", self.picked_cups)

    def _des_idx(self):
        des_label = self.cups[self.idx] - 1
        while des_label in self.picked_cups:
            des_label -= 1
            if des_label < self.min_cup:
                des_label = max(self.cups)
        des_idx = self.cups.index(des_label)
        return des_idx

    def _move_cups(self):
        print("Current:", self.idx, "label:", self.cups[self.idx])
        self._pick_cups()
        des_idx = (self._des_idx() + len(self.cups)) % len(self.cups)
        print("Move", self._output(self.picked_cups), "to des_idx",
              des_idx, "with label", self.cups[des_idx])
        print(self)

        for cup in self.picked_cups:
            self.cups.remove(cup)

        for i, cup in enumerate(self.picked_cups):
            self.cups.insert(des_idx + i - 2, cup)

        self.idx = (self.idx + 1) % len(self.cups)

    def do_move(self):
        self._move_cups()
        self._move_cups()
        self._move_cups()
        self._move_cups()
        # self._move_cups()
        # self._move_cups()
        # self._move_cups()
        # self._move_cups()
        # self._move_cups()
        # self._move_cups()


def play(configuration):

    cups = RotatingCups(configuration)
    cups.do_move()


def main():
    configuration = 398254716
    test_config = 389125467
    play(test_config)


if __name__ == "__main__":
    main()
