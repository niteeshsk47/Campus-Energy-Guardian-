# Campus Energy Guardian ⚡

## Project overview
Campus Energy Guardian is a Python command-line application that helps a college estimate and monitor electricity consumption in classrooms and laboratories. It calculates monthly energy use, estimated electricity cost and carbon emissions, then gives device-specific energy-saving recommendations.

## Problem statement
Educational institutions operate lights, fans, air conditioners and computers for long periods. Without room-level monitoring, unnecessary usage can go unnoticed. This project provides a simple software-based way to estimate energy use and identify possible savings.

## Objectives
- Maintain a list of campus rooms and electrical devices.
- Estimate daily and monthly electricity consumption in kWh.
- Estimate electricity cost and carbon emissions.
- Identify high-usage devices and display practical recommendations.
- Store data in a JSON file so it remains available after restarting the program.

## OOP concepts demonstrated

| Concept | Where it is used |
|---|---|
| Class and object | `Room`, `Device`, `Light`, `Fan`, `AirConditioner`, `Computer` |
| Abstraction | `Device` is an abstract base class with `usage_note()` |
| Inheritance | Concrete device classes inherit from `Device` |
| Encapsulation | Wattage and operating hours are stored in protected attributes and exposed through properties |
| Polymorphism | Each device type implements its own `usage_note()` |
| Composition | A `Room` contains multiple `Device` objects |
| Exception handling | Custom `ValidationError` handles invalid input |

## Project structure

```text
Campus_Energy_Guardian/
├── main.py
├── models.py
├── guardian.py
├── storage.py
├── reports.py
├── README.md
├── requirements.txt
├── data/
│   └── .gitkeep
└── tests/
    └── test_guardian.py
```

## Requirements
- Python 3.9 or newer
- No external libraries required

## How to run
1. Extract the project ZIP.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

## How energy is calculated

Energy consumption is calculated using:

`Energy (kWh) = Power (watts) × Usage hours ÷ 1000`

Monthly cost:

`Monthly cost = Monthly energy (kWh) × Tariff per kWh`

Estimated carbon emissions:

`CO2 (kg) = Monthly energy (kWh) × Emission factor`

The default tariff and emission factor are illustrative values. Change them in `CampusEnergyGuardian()` to match the assumptions required by your institution or electricity provider.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Sample demonstration
1. Add room `R101`, name `Physics Lab`, building `AB1`.
2. Add an AC: type `ac`, ID `AC1`, name `Lab AC`, wattage `1500`, hours `8`.
3. Add a fan: type `fan`, ID `F1`, name `Ceiling Fan`, wattage `75`, hours `10`.
4. Open the room report and campus report.
5. Change device hours and view how the estimates change.

## Limitations and future scope
- This is an estimate-based academic prototype, not a live electricity meter.
- Actual energy consumption can vary with device condition, load and operating settings.
- Future versions could connect to IoT smart meters, provide a graphical dashboard, add user login roles and export PDF reports.

## Author
Student project for Python Object-Oriented Programming.
