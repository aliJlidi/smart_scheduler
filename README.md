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
```

### 2. Set Up Python Environment

Ensure Python 3.7 or newer is installed:

```bash
python --version
```

### 3. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 4. Install Required Packages

Tkinter and SQLite are standard in most Python distributions, but for plotting:

```bash
pip install -r requirements.txt
```

If `tkinter` is missing on Linux:

```bash
sudo apt install python3-tk
```

---

## Usage

### Step 1: Initialize the Database

This creates the SQLite database and populates it with default values:

```bash
python main.py
```

You should see:

```
Database initialized.
```

### Step 2: Run the Scheduler GUI

Launch the graphical interface:

```bash
python ui/scheduler_gui.py
```

Inside the app:
- Enter number of jobs and machines
- Click **Generate Data**
- Click **Run Scheduler**

---

## How It Works

### Database

- `jobs` table contains: `id`, `duration`, `deadline`, `energy_required`
- `machines` table contains: `id`, `capacity`, and `is_available`

### Scheduling Logic

- Jobs are sorted by **earliest deadline first**
- Each job is assigned to the machine with the **earliest availability**
- The algorithm records:
  - Job ID
  - Assigned machine
  - Start and end times
  - Tardiness

### GUI

- Built using Python’s built-in `tkinter` module
- Displays results in a responsive table
- Includes a dynamic Gantt chart with optional animation

---

## Sample Output (Console)

```text
Job 1 → Machine 2, Start: 0, End: 4, Tardiness: 0
Job 2 → Machine 1, Start: 0, End: 3, Tardiness: 1
...
Total jobs scheduled: 50
```





## Credits

**Developed by:** Ali Jlidi  
**PhD Candidate**, University of Miskolc  
**June 2025**  
**Research Topic:** Smart Scheduling in Industry 4.0
