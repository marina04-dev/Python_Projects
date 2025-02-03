# Garden Simulator Text Based Game 
import random
game_title = "Garden Simulator Text Based Game"


class Plant:
    def __init__(self, name, harvest_yield):
        self.name = name
        self.harvest_yield = harvest_yield
        self.growth_stages = ["seed", "sprout", "mature", "flower", "fruit", "harvest-ready"]
        self.current_growth_stage = self.growth_stages[0] # Initial growth stage is seed
        self.harvestable = False

    def grow(self):
        current_index = self.growth_stages.index(self.current_growth_stage)
        if self.current_growth_stage == self.growth_stages[-1]:
            print(f"{self.name} is already fully grown!")
        elif current_index < len(self.growth_stages) - 1:
            self.current_growth_stage = self.growth_stages[current_index + 1]
            if self.current_growth_stage == "harvest-ready":
                self.harvestable = True

    def harvest(self):
        if self.harvestable:
            self.harvestable = False
            return self.harvest_yield
        else:
            return None
            
        

# Define Specific Plant Types(sub-classes) 
class Tomato(Plant):
    def __init__(self):
        super().__init__("Tomato", 10)
        

class Lettuce(Plant):
    def __init__(self):
        super().__init__("Lettuce", 5)
        self.growth_stages = ["seed","sprout","mature","harvest-ready"]
        
class Carrot(Plant):
    def __init__(self):
        super().__init__("Carrot", 8)
        self.growth_stages = ["seed","sprout","mature","harvest-ready"]
        
        
# Continuous Prompting for Selecting Items
def select_item(items):
    # Determine if items is a dictionary or a list
    if type(items) == dict:
        item_list = list(items.keys())
    elif type(items) == "list":
        item_list = items 
    else:
        print("Invalid items type!")
        return None 
        
    # Print out the items 
    for i in range(len(item_list)):
        try:
            item_name = item_list[i].name
        except:
            item_name = item_list[i]
        print(f"{i+1}. {item_name}")

    # Get user input 
    while True:
        user_input = input("Select an item: ")
        try:
            user_input = int(user_input)
            if 0 < user_input <= len(item_list):
                return item_list[user_input -1]
            else:
                print("Invalid Input!")
        except:
            print("Invalid Input!")
            
            
# Defining the Gardener Class 
class Gardener:
    # Represents a gardener who can plant and harvest plants.
    plant_dict = {"tomato": Tomato, "lettuce": Lettuce, "carrot": Carrot}
    
    def __init__(self, name):
        self.name = name
        self.planted_plants = []
        self.inventory = {}
        
    def plant(self):
        selected_plant = select_item(self.inventory)
        if selected_plant in self.inventory and self.inventory[selected_plant] > 0:
            self.inventory[selected_plant] -= 1
            if self.inventory[selected_plant] == 0:
                del self.inventory[selected_plant]
            new_plant = self.plant_dict[selected_plant]()
            self.planted_plants.append(new_plant)
            print(f"{self.name} planted a {selected_plant}!")
        else:
            print(f"{self.name} does not have any {selected_plant} to plant!")
            
    
    def tend(self):
        for plant in self.planted_plants:
            if plant.harvestable:
                print(f"{plant.name} is ready to be harvested!")
            else:
                plant.grow()
                print(f"{plant.name} is now a {plant.current_growth_stage}!")
                
                
    def harvest(self):
        selected_plant = select_item(self.planted_plants)
        if selected_plant.harvestable == True:
            if selected_plant.name in self.inventory:
                self.inventory[selected_plant.name] += selected_plant.harvest()
            else:
                self.inventory[selected_plant.name] = selected_plant.harvest()
            print(f"You harvested a {selected_plant.name}!")
            self.planted_plants.remove(selected_plant)
        else:
            print(f"You can not harvest a {selected_plant.name}!")
            
            
    def forage_for_seeds(self):
        seed = random.choice(all_plant_types)
        if seed in self.inventory:
            self.inventory[seed] += 1 
        else:
            self.inventory[seed] = 1 
        print(f"{self.name} found a {seed} seed!")
        
        
# Setting Up The Main Game Loop
all_plant_types = ["tomato","lettuce","carrot"]
valid_commands = ["plant","tend","harvest","forage","help","quit"]

# Print Welcome message
print("Welcome to the garden! You will act as a virtual gardener. \nForage for new seeds, plant them, and then watch them grow!\nStart by entering your name.")

# Create gardener (no valid name input checking - it can be anything)
gardener_name = input("What is your name? ")
print(f"Welcome, {gardener_name}! Let's get gardening!\nType 'help' for a list of commands!")
gardener = Gardener(gardener_name)


# Main game loop 
while True:
    player_action = input("What would you like to do? ")
    player_action = player_action.lower()
    if player_action in valid_commands:
        if player_action == "plant":
            gardener.plant()
        elif player_action == "tend":
            gardener.tend()
        elif player_action == "harvest":
            gardener.harvest()
        elif player_action == "forage":
            gardener.forage_for_seeds()
        elif player_action == "help":
            print("*** Commands ***")
            for command in valid_commands:
                print(command)
        elif player_action == "quit":
            print("Goodbye!")
            break
    else:
        print("Invalid Command!")
