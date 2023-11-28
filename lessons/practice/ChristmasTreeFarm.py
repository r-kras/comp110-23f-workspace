from __future__ import annotations

class ChristmasTreeFarm:
    """A chrismas tree farm with trees in a plot."""

    plots: list[int]

    def __init__(self, plots: int, initial_planting: int) -> None:
        """Create an instance of the ChristmasTreeFarm class."""
        self.plots = []
        for idx in range(0, plots):
            if (idx < initial_planting):
                self.plots.append(1)
            else:
                self.plots.append(0)
            
    
    def plant(self, idx: int) -> None:
        """Plants new tree in index."""
        self.plots[idx] = 1

    def growth(self) -> None:
        """Increases each tree height by 1."""
        for plot in self.plots:
            if plot != 0:
                plot += 1
    
    def harvest(self, replant: bool) -> int:
        """Harvests trees that are larger than 4."""
        harvested: int = 0
        for plot in self.plots:
            if plot > 4:
                harvested += 1
                if replant == True:
                    plot = 1
                else:
                    plot = 0
        return harvested
    
    def __add__(self, addend: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Overloading the addition operator."""
        size: int = len(self.plots) + len(addend.plots)
        initial: int = 0
        for plot in self.plots:
            if plot != 0:
                initial += 1
        for plot in addend.plots:
            if plot != 0:
                initial += 1
        return ChristmasTreeFarm(size, initial)