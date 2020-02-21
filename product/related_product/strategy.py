from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod

class Strategy(ABC):
    def populate_related_product(self,product) ->List:
        pass