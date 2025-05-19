# Smart Scheduler: Industry 4.0 Scheduling System

This project implements a **smart scheduling system** inspired by Industry 4.0 principles, based on a real-world use case (e.g., Bosch production line). It efficiently assigns jobs to machines using a lightweight heuristic algorithm and provides a user-friendly desktop GUI for interaction.

The scheduler:

- Uses a **SQLite** database to store job and machine data.
- Applies a **greedy scheduling algorithm** to minimize tardiness and makespan.
- Offers a desktop **GUI built with Tkinter** (no external dependencies required).

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Sample Output](#sample-output)
- [Future Work](#future-work)
- [Credits](#credits)

---

## Features

- No internet or package installation required (except Python itself).
- Runs entirely on a local machine using **SQLite** and **Tkinter**.
- **Greedy job scheduling algorithm** using deadline-based prioritization.
- GUI displays job-to-machine assignments, start/end times, and tardiness.
- Easily extendable for optimization models, breakdowns, and real-time data.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart_scheduler.git
cd smart_scheduler

## Project Structure

smart_scheduler/
├── db/
│ └── init_db.py # Creates SQLite tables
├── models/
│ ├── job_generator.py # Inserts random jobs
│ ├── machine_generator.py # Inserts random machines
│ └── scheduler_logic.py # Greedy job assignment
├── ui/
│ └── scheduler_gui.py # GUI with embedded Gantt chart + animation
├── scheduler.db # SQLite database (auto-generated)
├── main.py # Entry point to initialize database
├── requirements.txt # Python dependencies
└── README.md # Project documentation