"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730699792"


class Simpy:
    """A simple, single dimension implementation of NumPy."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, inp_list: list[float]) -> None:
        """Initialize a simpy object."""
        self.values = inp_list

    def __str__(self) -> str:
        """Returns the simpy object as a string."""
        return f"Simpy({str(self.values)})"
    
    def fill(self, value: float, repetitions: int) -> None:
        """Adapt simpy object to have 'repetitions' number of 'value'."""
        self.values = []
        for i in range(0, repetitions):
            self.values.append(float(value))
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Adapt simpy object to have values from 'start' to 'stop', increasing with a 'step'."""
        self.values = []
        while start != stop:
            self.values.append(float(start))
            start += step
        
    def sum(self) -> float:
        """Return the total of each value within the simpy object."""
        total: float = 0.0
        for value in self.values:
            total += value
        return total
    
    def __add__(self, addend: Union[Simpy, float]) -> Simpy:
        """Overloading the addition operator to interact with simpy objects."""
        out: Simpy = Simpy([])
        # if addend is another simpy
        if type(addend) is Simpy:
            # need lengths to be the same
            assert len(self.values) == len(addend.values)
            # add simpys together by their corresponding values
            for idx in range(0, len(self.values)):
                out.values.append(self.values[idx] + addend.values[idx])
        # if addend is a float
        else:
            # increase each simpy value by the addend
            for value in self.values:
                out.values.append(value + addend)
        return out
    
    def __pow__(self, exp: Union[Simpy, float]) -> Simpy:
        """Overloading the power operator to interact with simpy objects."""
        out: Simpy = Simpy([])
        # if exp is another simpy
        if type(exp) is Simpy:
            # need lengths to be the same
            assert len(self.values) == len(exp.values)
            # add simpys together by their corresponding values
            for idx in range(0, len(self.values)):
                out.values.append(self.values[idx] ** exp.values[idx])
        # if exp is a float
        else:
            # increase each simpy value by the exp
            for value in self.values:
                out.values.append(value ** exp)
        return out
    
    def __eq__(self, compared: Union[Simpy, float]) -> list[bool]:
        """Adapting the equality operator to interact with Simpy objects."""
        # if compared is another simpy
        out: list[bool] = []
        if type(compared) is Simpy:
            # need lengths to be the same
            assert len(self.values) == len(compared.values)
            # add simpys together by their corresponding values
            for idx in range(0, len(self.values)):
                out.append(self.values[idx] == compared.values[idx])
        # if compared is a float
        else:
            # increase each simpy value by the compared
            for value in self.values:
                out.append(value == compared)
        return out
    
    def __gt__(self, compared: Union[Simpy, float]) -> list[bool]:
        """Adapting the equality operator to interact with Simpy objects."""
        # if compared is another simpy
        out: list[bool] = []
        if type(compared) is Simpy:
            # need lengths to be the same
            assert len(self.values) == len(compared.values)
            # add simpys together by their corresponding values
            for idx in range(0, len(self.values)):
                out.append(self.values[idx] > compared.values[idx])
        # if compared is a float
        else:
            # increase each simpy value by the compared
            for value in self.values:
                out.append(value > compared)
        return out
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adapting subscription notation to work with simpy objects."""
        # if rhs is a list of bools
        if type(rhs) is list:
            out: Simpy = Simpy([])
            # need lengths to be the same
            assert len(self.values) == len(rhs)
            # add simpys together by their corresponding values
            for idx in range(0, len(self.values)):
                if (rhs[idx]):
                    out.values.append(self.values[idx])
        # if rhs is an int
        else:
            # increase each simpy value by the rhs
            out: float = self.values[rhs]
        return out