#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")


class RobotWorker(Workable):
    def work(self):
        print("Robot working")


def manage_worker(worker: Workable):
    worker.work()


def manage_eater(eater: Eatable):
    eater.eat()


human = HumanWorker()
robot = RobotWorker()

manage_worker(human)
manage_worker(robot)

manage_eater(human)
