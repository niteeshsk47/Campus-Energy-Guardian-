"""Core domain models for Campus Energy Guardian."""
from abc import ABC, abstractmethod


class EnergyGuardianError(Exception):
    """Base exception for application errors."""


class ValidationError(EnergyGuardianError):
    """Raised when supplied data is invalid."""


class Device(ABC):
    """Abstract electrical device. Subclasses define their own usage behaviour."""

    def __init__(self, device_id, name, wattage, daily_hours=0):
        self.device_id = str(device_id).strip()
        self.name = str(name).strip()
        self._wattage = float(wattage)
        self._daily_hours = float(daily_hours)
        if not self.device_id or not self.name:
            raise ValidationError("Device ID and name cannot be empty.")
        if self._wattage <= 0:
            raise ValidationError("Wattage must be greater than zero.")
        if not 0 <= self._daily_hours <= 24:
            raise ValidationError("Daily operating hours must be between 0 and 24.")

    @property
    def wattage(self):
        return self._wattage

    @property
    def daily_hours(self):
        return self._daily_hours

    @daily_hours.setter
    def daily_hours(self, hours):
        hours = float(hours)
        if not 0 <= hours <= 24:
            raise ValidationError("Daily operating hours must be between 0 and 24.")
        self._daily_hours = hours

    @abstractmethod
    def usage_note(self):
        """Return a device-specific energy-saving observation."""

    def daily_kwh(self):
        return (self.wattage * self.daily_hours) / 1000

    def monthly_kwh(self, days=30):
        return self.daily_kwh() * days

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "device_id": self.device_id,
            "name": self.name,
            "wattage": self.wattage,
            "daily_hours": self.daily_hours
        }


class Light(Device):
    def usage_note(self):
        if self.daily_hours > 8:
            return "Consider daylight sensors or switching off unused lights."
        return "Lighting usage is within the suggested daily range."


class Fan(Device):
    def usage_note(self):
        if self.daily_hours > 12:
            return "Check whether fans are running in empty rooms."
        return "Fan usage is within the suggested daily range."


class AirConditioner(Device):
    def usage_note(self):
        if self.daily_hours > 8:
            return "Set AC near 24-26 C and keep doors and windows closed."
        return "AC usage is within the suggested daily range."


class Computer(Device):
    def usage_note(self):
        if self.daily_hours > 10:
            return "Enable sleep mode and shut down computers after lab sessions."
        return "Computer usage is within the suggested daily range."


DEVICE_TYPES = {
    "light": Light,
    "fan": Fan,
    "ac": AirConditioner,
    "computer": Computer
}


class Room:
    """A room owns a collection of devices (composition)."""

    def __init__(self, room_id, room_name, building):
        self.room_id = str(room_id).strip()
        self.room_name = str(room_name).strip()
        self.building = str(building).strip()
        self._devices = []
        if not all((self.room_id, self.room_name, self.building)):
            raise ValidationError("Room ID, room name and building are required.")

    @property
    def devices(self):
        return tuple(self._devices)

    def add_device(self, device):
        if any(d.device_id == device.device_id for d in self._devices):
            raise ValidationError("A device with this ID already exists in this room.")
        self._devices.append(device)

    def find_device(self, device_id):
        for device in self._devices:
            if device.device_id == str(device_id):
                return device
        return None

    def daily_kwh(self):
        return sum(device.daily_kwh() for device in self._devices)

    def monthly_kwh(self, days=30):
        return sum(device.monthly_kwh(days) for device in self._devices)

    def to_dict(self):
        return {
            "room_id": self.room_id,
            "room_name": self.room_name,
            "building": self.building,
            "devices": [device.to_dict() for device in self._devices]
        }

    @classmethod
    def from_dict(cls, data):
        room = cls(data["room_id"], data["room_name"], data["building"])
        for item in data.get("devices", []):
            device_class = DEVICE_TYPES.get(item["type"].lower())
            if device_class is None:
                continue
            room.add_device(device_class(
                item["device_id"], item["name"],
                item["wattage"], item["daily_hours"]
            ))
        return room
