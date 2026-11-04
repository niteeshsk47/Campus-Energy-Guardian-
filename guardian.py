"""Application services and energy analysis."""
from models import (
    Room, Light, Fan, AirConditioner, Computer,
    DEVICE_TYPES, ValidationError
)


class CampusEnergyGuardian:
    """Coordinates rooms, devices, calculations and recommendations."""

    def __init__(self, tariff=8.0, emission_factor=0.82):
        self._rooms = {}
        self.tariff = float(tariff)              # currency units per kWh
        self.emission_factor = float(emission_factor)  # kg CO2 per kWh
        if self.tariff < 0 or self.emission_factor < 0:
            raise ValidationError("Tariff and emission factor cannot be negative.")

    @property
    def rooms(self):
        return tuple(self._rooms.values())

    def add_room(self, room_id, room_name, building):
        room_id = str(room_id).strip()
        if room_id in self._rooms:
            raise ValidationError("Room ID already exists.")
        room = Room(room_id, room_name, building)
        self._rooms[room_id] = room
        return room

    def get_room(self, room_id):
        return self._rooms.get(str(room_id))

    def add_device(self, room_id, kind, device_id, name, wattage, hours):
        room = self.get_room(room_id)
        if room is None:
            raise ValidationError("Room not found.")
        device_class = DEVICE_TYPES.get(kind.lower())
        if device_class is None:
            raise ValidationError("Choose light, fan, ac or computer.")
        device = device_class(device_id, name, wattage, hours)
        room.add_device(device)
        return device

    def update_device_hours(self, room_id, device_id, hours):
        room = self.get_room(room_id)
        if room is None:
            raise ValidationError("Room not found.")
        device = room.find_device(device_id)
        if device is None:
            raise ValidationError("Device not found.")
        device.daily_hours = hours

    def campus_summary(self, days=30):
        total_kwh = sum(room.monthly_kwh(days) for room in self.rooms)
        return {
            "days": days,
            "energy_kwh": total_kwh,
            "estimated_cost": total_kwh * self.tariff,
            "carbon_kg": total_kwh * self.emission_factor,
            "room_count": len(self._rooms),
            "device_count": sum(len(room.devices) for room in self.rooms)
        }

    def room_report(self, room):
        kwh = room.monthly_kwh()
        notes = []
        for device in room.devices:
            # Polymorphism: each concrete device supplies its own usage_note().
            note = device.usage_note()
            if "Consider" in note or "Check" in note or "Set AC" in note or "Enable" in note:
                notes.append(f"{device.name}: {note}")
        return {
            "room": room.room_name,
            "building": room.building,
            "monthly_kwh": kwh,
            "monthly_cost": kwh * self.tariff,
            "carbon_kg": kwh * self.emission_factor,
            "devices": len(room.devices),
            "recommendations": notes
        }

    def highest_consuming_room(self):
        if not self._rooms:
            return None
        return max(self.rooms, key=lambda room: room.monthly_kwh())

    def to_dict(self):
        return {
            "tariff": self.tariff,
            "emission_factor": self.emission_factor,
            "rooms": [room.to_dict() for room in self.rooms]
        }

    @classmethod
    def from_dict(cls, data):
        guardian = cls(data.get("tariff", 8.0), data.get("emission_factor", 0.82))
        for room_data in data.get("rooms", []):
            room = Room.from_dict(room_data)
            guardian._rooms[room.room_id] = room
        return guardian
