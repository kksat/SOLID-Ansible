#!/usr/bin/env python3


class Bird:
    def fly(self):
        print("Flying")


class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")


def make_bird_fly(bird: Bird):
    bird.fly()


sparrow = Bird()
penguin = Penguin()

make_bird_fly(sparrow)
make_bird_fly(penguin)
