"""JSON persistence layer."""
import json
import os
from guardian import CampusEnergyGuardian


class JSONStorage:
    def __init__(self, file_path="data/campus_data.json"):
        self.file_path = file_path

    def save(self, guardian):
        folder = os.path.dirname(self.file_path)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(guardian.to_dict(), file, indent=4)

    def load(self):
        if not os.path.exists(self.file_path):
            return CampusEnergyGuardian()
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return CampusEnergyGuardian.from_dict(data)
