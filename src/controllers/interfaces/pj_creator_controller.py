from typing import Dict
from abc import ABC, abstractmethod

class PJCreatorControllerInterface(ABC):

    @abstractmethod
    def create(self, person_info: Dict) -> Dict:
        pass
