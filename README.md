# ⚡ Campus Energy Guardian
### Smart Campus Electricity Monitoring and Energy Optimization System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Project](https://img.shields.io/badge/Project-Python%20OOP-green)
![Status](https://img.shields.io/badge/Status-Academic%20Project-orange)

## 1. Project Overview

Campus Energy Guardian is a Python-based electricity monitoring and energy management application developed using Object-Oriented Programming (OOP) principles.

The application helps educational institutions estimate and monitor electricity consumption across classrooms, laboratories and other campus facilities.

It allows users to register rooms and electrical appliances, calculate daily and monthly energy consumption, estimate electricity costs and carbon emissions, and receive device-specific energy-saving recommendations.

The system uses a command-line interface and JSON-based data storage to provide a simple and practical energy monitoring solution.

## 2. Problem Statement

Educational institutions use various electrical appliances, including lights, fans, air conditioners and computers, throughout the day.

Without proper monitoring, excessive electricity consumption and unnecessary appliance usage can increase electricity expenses and environmental impact.

Campus Energy Guardian addresses this problem by providing a centralized system to estimate electricity consumption, identify high-energy usage and encourage efficient energy management.

## 3. Project Objectives

- Develop an application to manage campus rooms and electrical devices.
- Calculate daily and monthly electricity consumption.
- Estimate electricity costs based on energy usage.
- Estimate carbon dioxide emissions.
- Generate room-wise and campus-wide energy reports.
- Provide device-specific energy-saving recommendations.
- Demonstrate important Object-Oriented Programming concepts.
- Store application data using JSON for future access.

## 4. Key Features

### Room Management
- Add classrooms, laboratories and other campus rooms.
- Maintain unique room identification numbers.
- Organize rooms by building.

### Electrical Device Management
Supports four electrical device categories:
- Lights
- Fans
- Air conditioners
- Computers

Users can register devices with their names, identification numbers, rated power and average daily operating hours.

### Energy Consumption Calculation
- Calculate daily energy consumption.
- Calculate monthly energy consumption.
- Update device operating hours.
- Monitor total campus energy usage.

### Electricity Cost Estimation
Calculate estimated electricity expenses using the configured tariff per kWh.

### Carbon Emission Estimation
Estimate carbon dioxide emissions based on electricity consumption and the configured emission factor.

### Energy-Saving Recommendations
Generate device-specific suggestions to encourage efficient electricity usage.

### Report Generation
- Room-wise energy reports.
- Campus-wide monthly reports.
- Highest energy-consuming room identification.
- Estimated electricity cost and carbon emissions.

### Data Persistence
Store and retrieve campus information through JSON file handling.

## 5. Object-Oriented Programming Concepts

This project demonstrates the following OOP concepts:

| OOP Concept | Implementation |
|---|---|
| Classes and Objects | Room, Device, Light, Fan, AirConditioner and Computer |
| Abstraction | Abstract Device class |
| Inheritance | Electrical device subclasses inherit from Device |
| Encapsulation | Protected attributes and properties |
| Polymorphism | Device-specific usage_note() methods |
| Composition | A Room contains multiple Device objects |
| Exception Handling | Custom EnergyGuardianError and ValidationError classes |

### Explanation

**Abstraction:** The abstract Device class defines a common structure for electrical devices and requires subclasses to implement their own usage_note() method.

**Inheritance:** Light, Fan, AirConditioner and Computer inherit common properties and methods from the Device class.

**Encapsulation:** Device wattage and operating hours are stored using protected attributes and accessed through properties.

**Polymorphism:** Each device type implements its own usage_note() method, providing different energy-saving recommendations.

**Composition:** A Room object contains multiple electrical device objects.

**Exception Handling:** Custom exceptions handle invalid data, incorrect device information and other application errors.

## 6. Project Structure

```text
Campus-Energy-Guardian/
│
├── main.py
├── models.py
├── guardian.py
├── storage.py
├── reports.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── .gitkeep
│
├── tests/
│   └── test_guardian.py
│
└── screenshots/
    ├── main_menu.png
    ├── room_creation.png
    ├── device_creation.png
    ├── energy_report.png
    └── test_results.png
```

### File Descriptions

| File | Purpose |
|---|---|
| main.py | Main application and interactive menu |
| models.py | OOP classes and device models |
| guardian.py | Energy calculations and application logic |
| storage.py | JSON data storage and retrieval |
| reports.py | Room and campus report generation |
| requirements.txt | Dependency information |
| .gitignore | Git exclusion rules |
| tests/test_guardian.py | Automated unit tests |

## 7. Technologies Used

- **Programming Language:** Python
- **Programming Paradigm:** Object-Oriented Programming
- **Data Storage:** JSON
- **Testing Framework:** Python unittest
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

No external Python packages are required for the current implementation.

## 8. Energy Calculation Formulas

### Daily Energy Consumption

Energy (kWh) = Power (Watts) × Operating Hours / 1000

### Monthly Energy Consumption

Monthly Energy (kWh) = Daily Energy (kWh) × Number of Days

### Estimated Electricity Cost

Electricity Cost = Monthly Energy (kWh) × Tariff per kWh

### Estimated Carbon Emissions

CO₂ (kg) = Monthly Energy (kWh) × Emission Factor

**Default assumptions:**
- Electricity tariff: 8 currency units per kWh.
- Carbon emission factor: 0.82 kg CO₂ per kWh.
- Monthly calculation period: 30 days.

These are illustrative assumptions and can be adjusted according to the electricity provider or institution.

## 9. Installation and Execution

### Prerequisites
- Python 3.9 or newer.
- Visual Studio Code or another Python-compatible editor.

### Step 1: Clone the Repository

```bash
git clone https://github.com/niteeshsk47/Campus-Energy-Guardian-.git
```

### Step 2: Open the Project Folder

```bash
cd Campus-Energy-Guardian-
```

### Step 3: Run the Application

```bash
python main.py
```

The interactive menu will appear in the terminal.

## 10. Application Menu

The application provides the following options:

1. Add a room
2. Add an electrical device
3. Update device operating hours
4. View all rooms and devices
5. View a room energy report
6. View campus monthly report
7. Save data
0. Save and exit

## 11. Testing

The project includes automated unit tests using Python's built-in unittest framework.

Run the tests using:

```bash
python -m unittest discover -s tests -v
```

The tests are intended to verify device creation, energy calculations, validation, room summaries and data persistence.

Actual test results should be recorded after executing the test suite.

## 12. Sample Demonstration

Example demonstration:

1. Register a room with ID R101.
2. Set its name as Physics Lab.
3. Add an air conditioner with 1500 W rated power and 8 operating hours per day.
4. Add a ceiling fan with 75 W rated power and 10 operating hours per day.
5. Generate the room-wise energy report.
6. Generate the campus monthly report.
7. Review the energy-saving recommendations.

## 13. Limitations

- The application estimates energy consumption using rated power and operating hours.
- It does not directly measure real-time electricity consumption.
- Actual electricity usage may differ depending on appliance condition and operating settings.
- Carbon emissions are estimated using a configurable emission factor.

## 14. Future Enhancements

Possible improvements include:

- Integration with IoT-based smart electricity meters.
- A graphical web dashboard for monitoring energy consumption.
- Real-time electricity usage monitoring.
- PDF and Excel report generation.
- User authentication and role-based access.
- Historical energy usage analysis and visualization.

## 15. Conclusion

Campus Energy Guardian demonstrates how Python Object-Oriented Programming can be applied to a practical energy management problem.

By combining classes, inheritance, abstraction, encapsulation, polymorphism, exception handling and JSON data storage, the project provides a modular and extensible approach to estimating campus electricity consumption.

The project also promotes energy awareness by highlighting usage patterns and suggesting practical ways to reduce unnecessary electricity consumption.

---

## Author

**Python Object-Oriented Programming Academic Project**

**Repository:** https://github.com/niteeshsk47/Campus-Energy-Guardian-

**Developed using:** Python and Object-Oriented Programming
