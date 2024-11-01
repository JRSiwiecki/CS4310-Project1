"""Module containing code to run the scheduler algorithms."""

import random
from schedulers import fcfs, sjf, rr2, rr5

JOB_FOLDER_PATH = "job-files/"
NUMBER_OF_BATCHES = 3


def job_file_to_array():
    """Convert batch job files (batch1.txt, batch2.txt, batch3.txt) to a list of
    list of jobs.

    Returns:
        List[List[int]]: A list where each inner list contains int
        values representing jobs.
    """
    batch_list = []

    for i in range(1, NUMBER_OF_BATCHES + 1):
        with open(
            JOB_FOLDER_PATH + "batch" + str(i) + ".txt", "r", encoding="utf-8"
        ) as file:
            job_list = []

            for line in file.readlines():
                # Don't really care what the name/number of the job is, can just be
                # tracked by its position in the list
                if line[0] == "J":
                    continue

                job_list.append(int(line))

            batch_list.append(job_list)

    return batch_list


def generate_random_batch_list(num_batches=20, max_job_length=25, job_count=5):
    """
    Generate a list of random job batches for testing the scheduler.
    Each batch will have lists that contain either 5, 10, or 15 jobs (all in lists will
    be same length).

    Args:
        num_batches (int): Number of batches to generate
        max_job_length (int): Maximum length of each job

    Returns:
        List[List[int]]: List of job batches, where each batch is a list of job lengths
    """

    batch_list = []

    for _ in range(num_batches):
        # Generate random job lengths between 1 and max_job_length
        job_list = [random.randint(1, max_job_length) for _ in range(job_count)]
        batch_list.append(job_list)

    return batch_list


def main():
    """
    Runs job_file_to_array then runs each scheduler.
    Note that we assume that all jobs arrive at the same time (0).
    """
    file_batch_list = job_file_to_array()

    fcfs.run_scheduler(file_batch_list)
    sjf.run_scheduler(file_batch_list)
    rr2.run_scheduler(file_batch_list)
    rr5.run_scheduler(file_batch_list)

    random_batch_list = generate_random_batch_list()

    # ATT -> Average Turnaround Time
    fcfs_att = sum(fcfs.run_scheduler(random_batch_list, False)) / len(
        random_batch_list
    )
    sjf_att = sum(sjf.run_scheduler(random_batch_list, False)) / len(random_batch_list)
    rr2_att = sum(rr2.run_scheduler(random_batch_list, False)) / len(random_batch_list)
    rr5_att = sum(rr5.run_scheduler(random_batch_list, False)) / len(random_batch_list)

    print("FCFS Average Turnaround Time:", round(fcfs_att, 2), "Units of Work")
    print("SJF Average Turnaround Time:", round(sjf_att, 2), "Units of Work")
    print("RR2 Average Turnaround Time:", round(rr2_att, 2), "Units of Work")
    print("RR5 Average Turnaround Time:", round(rr5_att, 2), "Units of Work")


if __name__ == "__main__":
    main()
