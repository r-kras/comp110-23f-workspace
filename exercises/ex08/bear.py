"""File to define Bear class."""


class Bear:
    """Simulating a bear using its age and its hunger."""
    # attributes
    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Initializing the attributes of the Bear class."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self) -> None:
        """Aging the bear one day and decreasing its hunger."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Adjusts the bear's hunger score based on the amount fish eaten."""
        self.hunger_score += num_fish
        return None