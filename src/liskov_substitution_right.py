#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def move(self):
        pass


class FlyingBird(Bird):
    def move(self):
        self.fly()

    def fly(self):
        print("Flying")


class NonFlyingBird(Bird):
    def move(self):
        self.walk()

    def walk(self):
        print("Walking")


class Sparrow(FlyingBird):
    pass


class Penguin(NonFlyingBird):
    pass


def make_bird_move(bird: Bird):
    bird.move()


sparrow = Sparrow()
penguin = Penguin()

make_bird_move(sparrow)
make_bird_move(penguin)
