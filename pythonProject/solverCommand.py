from abc import ABC, abstractmethod


# Command pattern to select solving algorithms
class SolverCommand(ABC):
    @abstractmethod
    def execute(self):
        pass
