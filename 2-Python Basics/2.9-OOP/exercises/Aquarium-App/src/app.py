#!/usr/bin/env python


class AquariumApp:
    def __init__(self, fish_count, eye_color, skin_color):
        self.fish_count = fish_count
        self.eye_color = eye_color
        self.skin_color = skin_color

        self.__swim_count = 0
        self._dead_fish_count = 0

    def swim(self):
        if self.fish_count == 0:
            print("There are no alive fish left.")
            return
        self.__swim_count += 1

        print(
            str(self.fish_count)
            + " fish are swimming. Their eyes are "
            + self.eye_color
            + " and their skin is "
            + self.skin_color
            + "."
        )
        print(
            "There are "
            + str(self._dead_fish_count)
            + " dead fish with them in the aquarium."
        )
        print("The fish have now been swimming " + str(self.__swim_count) + " times.")

    def die_fish(self, number: int):
        if self.fish_count == 0:
            print("All fish are dead.")
            print("GAME OVER")
            print("=====")
            return
        self.fish_count -= number
        self._dead_fish_count += number
        if number > 1:
            print(str(number) + " fish have died.")
        else:
            print("A fish has died.")


if __name__ == "__main__":
    my_aquarium_app = AquariumApp(5, "blue", "red")
    my_aquarium_app.swim()
    my_aquarium_app.die_fish(2)
    my_aquarium_app.swim()
    my_aquarium_app.die_fish(1)
    my_aquarium_app.swim()
    my_aquarium_app.die_fish(2)
    my_aquarium_app.swim()
    my_aquarium_app.die_fish(1)
