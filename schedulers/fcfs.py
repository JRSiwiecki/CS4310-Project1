def run_scheduler(batch_list):
    """Runs the First-Come-First-Serve (FCFS) Scheduler algorithm.
    This algorithm completes jobs as they appear.

    Args:
        batch_list (List[List[int]]): A list where each inner list contains
        float values representing jobs.
    """
    print("----------- FCFS Scheduler -----------")

    # Run scheduler for each job list in batch_list
    for batch_number, job_list in enumerate(batch_list):
        print("##### batch" + str(batch_number + 1) + ".txt #####")
        print(job_list)

        # Use copy of job_list so as to not modify underlying job_list
        job_list_copy = job_list.copy()
        completed_job_indexes = []
        job_turnaround_times = []
        current_time = 0

        # For FCFS, can run each job just once since we will complete entire job as
        # they have appeared in the list. Enumerate the loop so we can track the job
        # numbers
        for job_number, job_time in enumerate(job_list):

            # Offset job number by 1 for display for easier understanding
            print(
                "\nJob #"
                + str(job_number + 1)
                + " Scheduled - "
                + str(job_list_copy[job_number])
                + " Units of Work"
            )

            # No need to check in if job_time left is 0 or not, as FCFS
            # will complete whole job as it works on them.
            current_time += job_time
            job_list_copy[job_number] = work_on_job(job_list_copy[job_number])
            completed_job_indexes.append(job_number)

            job_turnaround_times.append(current_time)

            print("Job #" + str(job_number + 1) + " Complete")
            print("Current Time:", current_time)

        average_turnaround_time = round(sum(job_turnaround_times) / len(job_list), 2)

        print("\nAverage Turnaround Time:", average_turnaround_time, "Units of Work")
        print("----------------------")


def work_on_job(job_time):
    """Do work on job based on job_time. Return the amount of time left on the job.

    Args:
        job_time (int): Length of job.

    Returns:
        int: Always returns 0, as in FCFS the entire job is completed in one go.
    """
    print("Doing " + str(job_time) + " Units of Work")
    return 0
