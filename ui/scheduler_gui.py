import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.scheduler_logic import schedule_jobs
from main import generate_data
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class SchedulerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Scheduler")
        self.root.rowconfigure(3, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.geometry("1200x700")  # Default window size
        self.root.minsize(1000, 600)    # Minimum window size
        # Input frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=5)

        tk.Label(input_frame, text="Number of Jobs:").grid(row=0, column=0)
        self.jobs_entry = tk.Entry(input_frame, width=5)
        self.jobs_entry.insert(0, "50")
        self.jobs_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Number of Machines:").grid(row=0, column=2)
        self.machines_entry = tk.Entry(input_frame, width=5)
        self.machines_entry.insert(0, "10")
        self.machines_entry.grid(row=0, column=3, padx=5)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.btn_generate = ttk.Button(btn_frame, text="Generate Data", command=self.generate_data)
        self.btn_generate.grid(row=0, column=0, padx=10, pady=5)

        self.btn_schedule = ttk.Button(btn_frame, text="Run Scheduler", command=self.run_scheduler)
        self.btn_schedule.grid(row=0, column=1, padx=10, pady=5)

        # Table
        self.tree = ttk.Treeview(root, columns=("Job", "Machine", "Start", "End", "Tardiness"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        # Stats label
        self.stats_label = tk.Label(root, text="", font=("Arial", 10), justify="left", anchor="w")
        self.stats_label.pack(pady=10, padx=10, anchor="w")

        # Gantt Chart frame
        self.figure = Figure(figsize=(8, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)


    def generate_data(self):
        try:
            n_jobs = int(self.jobs_entry.get())
            n_machines = int(self.machines_entry.get())
            if n_jobs <= 0 or n_machines <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Please enter positive integers.")
            return

        generate_data(n_jobs, n_machines)
        messagebox.showinfo("Success", f"{n_jobs} jobs and {n_machines} machines generated.")

    def run_scheduler(self):
        self.tree.delete(*self.tree.get_children())
        schedule, makespan, avg_tardiness, late_jobs = schedule_jobs()

        for entry in schedule:
            self.tree.insert("", "end", values=(
                entry["job_id"],
                entry["machine_id"],
                entry["start"],
                entry["end"],
                entry["tardiness"]
            ))

        self.stats_label.config(text=(
            f"Total Makespan: {makespan}\n"
            f"Average Tardiness: {avg_tardiness:.2f}\n"
            f"Late Jobs: {late_jobs} out of {len(schedule)}"
        ))

        self.draw_gantt_chart(schedule)

    def draw_gantt_chart(self, schedule):
        self.ax.clear()
        machine_colors = {}

        for i, entry in enumerate(schedule):
            machine = entry["machine_id"]
            job = f"J{entry['job_id']}"
            start = entry["start"]
            duration = entry["end"] - entry["start"]

            if machine not in machine_colors:
                machine_colors[machine] = f"C{machine % 10}"

            self.ax.barh(
                y=machine,
                width=duration,
                left=start,
                height=0.6,
                color=machine_colors[machine],
                edgecolor='black'
            )
            self.ax.text(start + duration/2, machine, job, ha='center', va='center', fontsize=8, color='white')

        self.ax.set_ylabel("Machine ID")
        self.ax.set_xlabel("Time")
        self.ax.set_title("Gantt Chart: Job Distribution Over Time")
        self.ax.grid(True)
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerGUI(root)
    root.mainloop()