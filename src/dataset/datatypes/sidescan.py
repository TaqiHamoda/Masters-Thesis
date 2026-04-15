from typing import Self, Dict, Any

from .navigation import Navigation


class SideScanSonar:
    headers = Navigation.headers + ["num_samples", "slant_range", "delay_range", "bin_size", "frequency", "speed_of_sound"]

    def __init__(self,
        navigation: Navigation,
        num_samples: int,
        slant_range: float,
        delay_range: float,
        frequency: int,
        speed_of_sound: float,
    ):
        self.navigation = navigation
        self.num_samples = num_samples
        self.slant_range = slant_range
        self.delay_range = delay_range
        self.frequency = frequency
        self.speed_of_sound = speed_of_sound

        self.bin_size = self.slant_range / self.num_samples

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> Self:
        return SideScanSonar(
            navigation=Navigation.from_dict(data),
            num_samples=int(data["num_samples"]),
            slant_range=float(data["slant_range"]),
            delay_range=float(data["delay_range"]),
            frequency=int(data["frequency"]),
            speed_of_sound=float(data["speed_of_sound"])
        )

    def to_dict(self) -> Dict[str, Any]:
        return self.navigation.to_dict() | {
            "num_samples": self.num_samples,
            "slant_range": self.slant_range,
            "delay_range": self.delay_range,
            "bin_size": self.bin_size,
            "frequency": self.frequency,
            "speed_of_sound": self.speed_of_sound
        }