from abc import ABC, abstractmethod


class ASTNode(ABC):
    @abstractmethod
    def pretty_print(self, indent: str = "") -> str:
        """Return a formatted string representation of this node."""
        raise NotImplementedError
