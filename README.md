Smart Scheduler: Industry 4.0 Scheduling System
This project implements a smart scheduling system inspired by Industry 4.0 principles and designed around a real-world use case (e.g., Bosch production line). The system assigns jobs to machines efficiently using a lightweight optimization heuristic and provides a user-friendly graphical interface for interaction.

The scheduler:

Uses a SQLite database to store job and machine data.

Applies a simple greedy algorithm to minimize tardiness and makespan.

Offers a desktop GUI built with Tkinter (no external installation required).

Table of Contents
Features

Project Structure

Installation

Usage

How It Works

Sample Output

Future Work

Credits

Features
No internet or package installation required (except Python itself).

Runs entirely on local machine using SQLite and Tkinter.

Greedy job scheduling algorithm with deadline-based prioritization.

GUI displays job-to-machine assignment, start and end times, and tardiness.

Easy to extend with optimization models, machine breakdown simulation, or real-time data.

Project Structure

smart_scheduler/
│
├── db/
│   └── init_db.py                # Creates SQLite tables
│
├── models/
│   ├── job_generator.py          # Inserts random jobs into database
│   ├── machine_generator.py      # Inserts random machines into database
│   └── scheduler_logic.py        # Greedy job scheduling algorithm
│
├── ui/
│   └── scheduler_gui.py          # Graphical interface using Tkinter
│
├── scheduler.db                  # SQLite database file (generated at runtime)
├── main.py                       # Initializes the database and populates it
├── requirements.txt              # List of Python dependencies
└── README.md                     # Project documentation
Installation
1. Clone the Repository
Open a terminal and run:


git clone https://github.com/your-username/smart_scheduler.git
cd smart_scheduler
2. Set Up Python Environment
Ensure you have Python 3.7 or later installed. Tkinter and SQLite come with standard Python distributions.

To verify:


python --version
3. (Optional) Create a Virtual Environment

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
4. Install Required Packages
Tkinter and SQLite are part of standard Python, but just in case:


pip install -r requirements.txt
If you get a tkinter error, you can install it manually:


sudo apt-get install python3-tk     # Ubuntu/Debian
Usage
Step 1: Initialize the Database
This will create a SQLite database and populate it with sample data (50 jobs and 10 machines):


python main.py
You should see:


Database initialized.
Step 2: Run the Scheduler GUI
Start the graphical application:


python ui/scheduler_gui.py
This will open a window where you can:

Click Run Scheduler

See the result: which job is assigned to which machine, start and end time, and tardiness.

How It Works
The logic follows a simplified version of MILP scheduling.

Database

jobs table contains: id, duration, deadline, energy_required.

machines table contains: id, capacity, and availability status.

Job Assignment Logic

Jobs are sorted by deadline (Earliest Deadline First strategy).

Each job is assigned to the machine with the earliest availability.

The algorithm records:

Job ID

Assigned machine

Start and end times

Tardiness (lateness beyond deadline)

Graphical User Interface

Built using Python’s built-in tkinter module.

Displays output in a table format.

Can be extended to allow manual job entry or simulate disruptions.

Sample Output (Console)
Example of scheduling results printed to console:


Job 1 → Machine 2, Start: 0, End: 4, Tardiness: 0
Job 2 → Machine 1, Start: 0, End: 3, Tardiness: 1
...
Total jobs scheduled: 50
The GUI shows the same results in a visual table format.


Credits
Developed by: Ali Jlidi
PhD Candidate, University of Miskolc
June 2025
Topic: Smart Scheduling in Industry 4.0