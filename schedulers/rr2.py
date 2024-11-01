"""Module containing code to run the RR2 scheduler algorithm."""


def run_scheduler(batch_list, debug=True):
    """Runs the Round-Robin-2 (RR2) Scheduler algorithm.
    This algorithm goes through every job in a list and does 2 (or less if the job
    has less than 2 units of work left) units of work until every job is complete.

    Args:
        batch_list (List[List[int]]): A list where each inner list contains
        integer values representing jobs.
        debug (bool): Whether or not to use print statements during execution.
    """
    if debug:
        print("----------- Round Robin 2 Scheduler -----------")

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

        # Continue processing jobs in a round-robin manner until all are completed
        while len(completed_job_indexes) < len(job_list):
            for current_job_number in range(len(job_list)):
                if current_job_number in completed_job_indexes:
                    continue

                start_time = current_time

                # Perform 2 or less units of work on the job
                work_done = min(2, job_list_copy[current_job_number])
                current_time += work_done
                job_list_copy[current_job_number] = work_on_job(
                    job_list_copy[current_job_number], debug
                )
                end_time = current_time

                # If job is completed, mark it as complete
                if job_list_copy[current_job_number] <= 0:
                    completed_job_indexes.append(current_job_number)
                    job_turnaround_times.append(current_time)

                # Print each job's details in table format
                if debug:
                    print(
                        f"{current_job_number + 1:<6}{start_time:<12}{end_time:<10}{job_list_copy[current_job_number]}"
                    )

        # Calculate and print average turnaround time for the batch
        average_turnaround_time = round(sum(job_turnaround_times) / len(job_list), 2)
        average_turnaround_times.append(average_turnaround_time)

        if debug:
            print(f"\nAverage Turnaround Time: {average_turnaround_time} Units of Work")
            print("----------------------")

    return average_turnaround_times


def work_on_job(job_time, debug=True):
    """Do work on job based on job_time. Return the amount of time left on the job.

    Args:
        job_time (int): Length of job.
        debug (bool): Whether or not to use print statements during execution.

    Returns:
        int: Will return 0 or job_time - 2 depending on the amount of work left.
    """
    work_time_left = max(0, job_time - 2)
    return work_time_left
