"""File to define Fish class."""


class Fish:
    """Simulating a fish mainly using its age."""
    # attributes
    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Initializing the attributes of the Fish class."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self) -> None:
        """Aging the fish one day."""
        self.age += 1
        return None