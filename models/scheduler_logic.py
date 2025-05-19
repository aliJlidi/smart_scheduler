import sqlite3

def get_jobs_and_machines():
    conn = sqlite3.connect("scheduler.db")
    cur = conn.cursor()
    cur.execute("SELECT id, duration, deadline FROM jobs")
    jobs = cur.fetchall()
    cur.execute("SELECT id FROM machines WHERE is_available = 1")
    machines = cur.fetchall()
    return jobs, machines

def schedule_jobs():
    jobs, machines = get_jobs_and_machines()
    machine_available = {m[0]: 0 for m in machines}
    schedule = []

    for job in sorted(jobs, key=lambda x: x[2]):  # deadline sort
        best_machine = min(machine_available, key=machine_available.get)
        start_time = machine_available[best_machine]
        end_time = start_time + job[1]
        tardiness = max(0, end_time - job[2])
        schedule.append({
            "job_id": job[0],
            "machine_id": best_machine,
            "start": start_time,
            "end": end_time,
            "tardiness": tardiness
        })
        machine_available[best_machine] = end_time

    makespan = max(entry["end"] for entry in schedule)
    avg_tardiness = sum(entry["tardiness"] for entry in schedule) / len(schedule)
    late_jobs = sum(1 for entry in schedule if entry["tardiness"] > 0)

    return schedule, makespan, avg_tardiness, late_jobs
