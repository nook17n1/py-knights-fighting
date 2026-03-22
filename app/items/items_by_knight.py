from typing import Optional


class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(self, name: str, effect: Optional[dict]) -> None:
        self.name = name
        self.effect = effect
