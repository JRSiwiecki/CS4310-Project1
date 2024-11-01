"""Module containing code to run the FCFS scheduler algorithm."""


def run_scheduler(batch_list, debug=True):
    """Runs the First-Come-First-Serve (FCFS) Scheduler algorithm.
    This algorithm completes jobs as they appear.

    Args:
        batch_list (List[List[int]]): A list where each inner list contains
        integer values representing jobs.
        debug (bool): Whether or not to use print statements during execution.
    """
    if debug:
        print("----------- FCFS Scheduler -----------")

    average_turnaround_times = []

    # Run scheduler for each job list in batch_list
    for batch_number, job_list in enumerate(batch_list):
        if debug:
            print(f"\n##### Batch {batch_number + 1} #####")
            print("Jobs:", job_list)
            print(f"{'Job #':<6}{'Start Time':<12}{'End Time':<10}{'Work Left'}")

        # Use copy of job_list so as to not modify underlying job_list
        job_list_copy = job_list.copy()
        completed_job_indexes = []
        job_turnaround_times = []
        current_time = 0

        # For FCFS, can run each job just once since we will complete entire job as
        # they have appeared in the list. Enumerate the loop so we can track the job
        # numbers
        for job_number, job_time in enumerate(job_list):
            start_time = current_time
            current_time += job_time
            end_time = current_time
            job_list_copy[job_number] = work_on_job()
            completed_job_indexes.append(job_number)

            job_turnaround_times.append(current_time)

            if debug:
                print(f"{job_number + 1:<6}{start_time:<12}{end_time:<10}{'0':<15}")

        average_turnaround_time = round(sum(job_turnaround_times) / len(job_list), 2)
        average_turnaround_times.append(average_turnaround_time)

        if debug:
            print(f"\nAverage Turnaround Time: {average_turnaround_time} Units of Work")
            print("----------------------")

    return average_turnaround_times


def work_on_job():
    """Do work on job based on job_time. Return the amount of time left on the job.

    Returns:
        int: Always returns 0, as in FCFS the entire job is completed in one go.
    """
    return 0
