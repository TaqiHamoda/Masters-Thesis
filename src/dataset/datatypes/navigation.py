from typing import Self, Dict, Any

from .pose import Pose


class Navigation:
    headers = Pose.headers + ["east", "north", "altitude", "roll", "pitch", "yaw"]

    def __init__(self,
        pose: Pose,
        east: float,
        north: float,
        altitude: float,
        roll: float,
        pitch: float,
        yaw: float
    ):
        self.pose = pose
        self.east = east
        self.north = north
        self.altitude = altitude
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> Self:
        return Navigation(
            pose=Pose.from_dict(data),
            east=float(data["east"]),
            north=float(data["north"]),
            altitude=float(data["altitude"]),
            roll=float(data["roll"]),
            pitch=float(data["pitch"]),
            yaw=float(data["yaw"])
        )

    def to_dict(self) -> Dict[str, Any]:
        return self.pose.to_dict() | {
            "east": self.east,
            "north": self.north,
            "altitude": self.altitude,
            "roll": self.roll,
            "pitch": self.pitch,
            "yaw": self.yaw
        }