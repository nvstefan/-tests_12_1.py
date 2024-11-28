# Домашнее задание
# по теме "Простые Юнит-Тесты"

#Задача "Проверка на выносливость":

import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walk = Runner('walk')
        for i in range(10):
            walk.walk()
        self.assertEqual(walk.distance, 50)

    def test_run(self):
        run = Runner('run')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)
    def test_challenge(self):
        run = Runner('run')
        walk = Runner('walk')
        for i in range(10):
            run.run()
            walk.walk()
        self.assertNotEqual(run.distance, walk.distance)


if __name__ == '__main__':
    unittest.main()
