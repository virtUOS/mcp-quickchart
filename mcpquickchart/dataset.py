from dataclasses import dataclass


@dataclass
class Dataset:
    label: str
    data: list[float | int]
