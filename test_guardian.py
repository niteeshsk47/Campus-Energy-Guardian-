import os
import tempfile
import unittest

from guardian import CampusEnergyGuardian
from storage import JSONStorage
from models import Light, Fan, AirConditioner, Computer, ValidationError


class CampusEnergyGuardianTests(unittest.TestCase):
    def setUp(self):
        self.app = CampusEnergyGuardian(tariff=8, emission_factor=0.82)
        self.room = self.app.add_room("R101", "Physics Lab", "AB1")

    def test_device_energy_calculation(self):
        light = Light("L1", "LED", 20, 5)
        self.assertAlmostEqual(light.daily_kwh(), 0.1)
        self.assertAlmostEqual(light.monthly_kwh(), 3.0)

    def test_all_device_types(self):
        for kind in ("light", "fan", "ac", "computer"):
            self.app.add_device("R101", kind, kind, kind, 100, 2)
        self.assertEqual(len(self.room.devices), 4)

    def test_room_summary(self):
        self.app.add_device("R101", "fan", "F1", "Ceiling fan", 75, 4)
        summary = self.app.campus_summary()
        self.assertAlmostEqual(summary["energy_kwh"], 9.0)
        self.assertAlmostEqual(summary["estimated_cost"], 72.0)

    def test_invalid_hours(self):
        with self.assertRaises(ValidationError):
            self.app.add_device("R101", "light", "L1", "LED", 20, 25)

    def test_save_and_load(self):
        self.app.add_device("R101", "computer", "C1", "Desktop", 150, 6)
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            storage = JSONStorage(path)
            storage.save(self.app)
            loaded = storage.load()
            self.assertEqual(len(loaded.rooms), 1)
            self.assertEqual(len(loaded.rooms[0].devices), 1)


if __name__ == "__main__":
    unittest.main()
