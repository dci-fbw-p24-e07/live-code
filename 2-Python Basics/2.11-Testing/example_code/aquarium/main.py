class FishTank:
    
    def __init__(self, tank_name):
        self.tank_name = tank_name
        self.has_water = False
        self.num_of_fish = 0
        
    def add_fish_to_tank(self, fish_list: list) -> dict:
        if len(fish_list) > 10:
            raise ValueError("A maximum of 10 fish per tank")
        return {self.tank_name: fish_list}
    
    def fill_with_water(self):
        self.has_water = True
