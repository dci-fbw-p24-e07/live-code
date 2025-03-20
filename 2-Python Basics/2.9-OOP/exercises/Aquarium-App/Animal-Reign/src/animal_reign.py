#!/usr/bin/env python

from animal import Animal
from dog import Dog
from german_shepard import GermanShepard


def main():
    # Behavior of a human.
    human = Animal(2, 2)
    human.summary()
    print()
    human.breathe()
    print()
    human.walk()
    print("=====")

    # Behavior of a dog
    dog = Dog()
    dog.summary()
    print()
    dog.breathe()
    print()
    dog.walk()
    print("=====")

    # Behavior of a German Shepard
    german_shepard = GermanShepard()
    german_shepard.summary()
    print()
    german_shepard.breathe()
    print()
    german_shepard.walk()
    print("=====")

if __name__ == "__main__":
    main()
