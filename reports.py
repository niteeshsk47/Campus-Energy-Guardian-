"""Readable report formatting."""
from datetime import datetime


def print_campus_report(guardian):
    summary = guardian.campus_summary()
    print("\n" + "=" * 58)
    print("             CAMPUS ENERGY GUARDIAN")
    print("                MONTHLY REPORT")
    print("=" * 58)
    print(f"Rooms monitored       : {summary['room_count']}")
    print(f"Devices monitored     : {summary['device_count']}")
    print(f"Energy consumption    : {summary['energy_kwh']:.2f} kWh")
    print(f"Estimated electricity : {summary['estimated_cost']:.2f}")
    print(f"Estimated CO2         : {summary['carbon_kg']:.2f} kg")
    top = guardian.highest_consuming_room()
    if top:
        print(f"Highest-use room      : {top.room_name} ({top.monthly_kwh():.2f} kWh)")
    print(f"Generated             : {datetime.now():%d-%m-%Y %H:%M}")
    print("=" * 58)


def print_room_report(guardian, room):
    report = guardian.room_report(room)
    print(f"\nROOM: {report['room']} | BUILDING: {report['building']}")
    print("-" * 54)
    print(f"Devices: {report['devices']}")
    print(f"Monthly energy: {report['monthly_kwh']:.2f} kWh")
    print(f"Estimated cost: {report['monthly_cost']:.2f}")
    print(f"Estimated CO2 : {report['carbon_kg']:.2f} kg")
    print("Recommendations:")
    if report["recommendations"]:
        for note in report["recommendations"]:
            print(f"  * {note}")
    else:
        print("  * No major usage warnings detected.")
