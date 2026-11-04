"""Command-line interface for Campus Energy Guardian."""
from guardian import CampusEnergyGuardian
from storage import JSONStorage
from reports import print_campus_report, print_room_report
from models import EnergyGuardianError


def ask(prompt, cast=str):
    value = input(prompt).strip()
    return cast(value)


def show_menu():
    print("""
========== CAMPUS ENERGY GUARDIAN ==========
1. Add a room
2. Add an electrical device
3. Update device operating hours
4. View all rooms and devices
5. View a room energy report
6. View campus monthly report
7. Save data
0. Save and exit
============================================
""")


def main():
    storage = JSONStorage()
    guardian = storage.load()
    print("Welcome! Campus Energy Guardian is ready.")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1":
                room_id = ask("Room ID: ")
                room_name = ask("Room name: ")
                building = ask("Building: ")
                guardian.add_room(room_id, room_name, building)
                print("Room added successfully.")

            elif choice == "2":
                room_id = ask("Room ID: ")
                print("Device types: light / fan / ac / computer")
                kind = ask("Device type: ").lower()
                device_id = ask("Device ID: ")
                name = ask("Device name: ")
                wattage = ask("Rated power (watts): ", float)
                hours = ask("Average daily usage (0-24 hours): ", float)
                guardian.add_device(room_id, kind, device_id, name, wattage, hours)
                print("Device added successfully.")

            elif choice == "3":
                room_id = ask("Room ID: ")
                device_id = ask("Device ID: ")
                hours = ask("New daily operating hours: ", float)
                guardian.update_device_hours(room_id, device_id, hours)
                print("Operating hours updated.")

            elif choice == "4":
                if not guardian.rooms:
                    print("No rooms registered yet.")
                for room in guardian.rooms:
                    print(f"\n{room.room_id} - {room.room_name} ({room.building})")
                    if not room.devices:
                        print("  No devices registered.")
                    for device in room.devices:
                        print(
                            f"  {device.device_id}: {device.name} | "
                            f"{device.wattage:g} W | {device.daily_hours:g} h/day"
                        )

            elif choice == "5":
                room = guardian.get_room(ask("Room ID: "))
                if room is None:
                    print("Room not found.")
                else:
                    print_room_report(guardian, room)

            elif choice == "6":
                print_campus_report(guardian)

            elif choice == "7":
                storage.save(guardian)
                print("Data saved.")

            elif choice == "0":
                storage.save(guardian)
                print("Data saved. Goodbye!")
                break

            else:
                print("Invalid choice. Please select from the menu.")

        except (EnergyGuardianError, ValueError) as error:
            print(f"Error: {error}")
        except KeyboardInterrupt:
            print("\nSaving before exit...")
            storage.save(guardian)
            break


if __name__ == "__main__":
    main()
