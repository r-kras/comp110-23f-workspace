"""File to define River class."""

__author__ = "730699792"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """A river of fish and bears that can eat and repopulate."""

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Remove any old fish from river."""
        # initialize temp lists
        tmp_fish: list[Fish] = []
        tmp_bears: list[Bear] = []
        # iterate through
        for single_fish in self.fish:
            if not (single_fish.age > 3):
                tmp_fish.append(single_fish)
        for single_bear in self.bears:
            if not (single_bear.age > 5):
                tmp_bears.append(single_bear)
        # update living 
        self.fish = tmp_fish
        self.bears = tmp_bears
        return None

    def bears_eating(self) -> None:
        """Simulates bears eating fish in the river."""
        for single_bear in self.bears:
            if len(self.fish) >= 5:
                single_bear.eat(3)
                self.remove_fish(3)

        return None
    
    def check_hunger(self) -> None:
        """Removing any 'Starving' bears from the population."""
        tmp_bears = []
        for single_bear in self.bears:
            if not (single_bear.hunger_score < 0):
                tmp_bears.append(single_bear)
        self.bears = tmp_bears
        return None
        
    def repopulate_fish(self) -> None:
        """Adding additional fish into the river."""
        for i in range(0, ((len(self.fish) // 2) * 4)):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self) -> None:
        """Adding additional bears into the river."""
        for i in range(0, len(self.bears) // 2):
            self.bears.append(Bear())
        return None
    
    def view_river(self) -> None:
        """Print the days, fish population, and bear population."""
        print(f"~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear Population: {len(self.bears)}")
        return None
            
    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self) -> None:
        """Simulate one week of life in the river."""
        # call one_river_day 7 times
        for day in range(0, 7):
            self.one_river_day()
        
    def remove_fish(self, amount: int) -> None:
        """Removes a set amount of fish from the river."""
        for i in range(0, amount):
            self.fish.pop(0)
        
    