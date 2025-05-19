from db.init_db import init_db
from models.job_generator import generate_jobs
from models.machine_generator import generate_machines

def generate_data(num_jobs=50, num_machines=10):
    init_db()
    generate_jobs(num_jobs)
    generate_machines(num_machines)
    print("Data generated.")

if __name__ == "__main__":
    generate_data()
