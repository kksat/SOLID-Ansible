#!/usr/bin/env python3


class Worker:
    def work(self):
        pass

    def eat(self):
        pass


class HumanWorker(Worker):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")


class RobotWorker(Worker):
    def work(self):
        print("Robot working")

    def eat(self):
        raise NotImplementedError("Robots do not eat")


def manage_worker(worker: Worker):
    worker.work()
    worker.eat()


human = HumanWorker()
robot = RobotWorker()

manage_worker(human)
manage_worker(robot)
