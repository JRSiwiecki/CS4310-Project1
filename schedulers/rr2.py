"""Module containing code to run the RR2 scheduler algorithm."""


def run_scheduler(batch_list):
    """Runs the Round-Robin-2 (RR2) Scheduler algorithm.
    This algorithm goes through every job in a list and does 2 (or less if the job
    has less than 2 units of work left) units of work until every job is complete.

    Args:
        batch_list (List[List[int]]): A list where each inner list contains
        float values representing jobs.
    """
    print("----------- Round Robin 2 Scheduler -----------")

    # Run scheduler for each job list in batch_list
    for batch_number, job_list in enumerate(batch_list):
        print("##### batch" + str(batch_number + 1) + ".txt #####")
        print(job_list)

        # Use copy of job_list so as to not modify underlying job_list
        job_list_copy = job_list.copy()
        completed_job_indexes = []
        job_turnaround_times = []
        current_time = 0

        # Must keep making passes through the list of jobs until we have completed every
        # job in the job_list
        while len(completed_job_indexes) < len(job_list):
            for current_job_number in range(len(job_list)):
                if current_job_number in completed_job_indexes:
                    continue

                # Offset job number by 1 for display for easier understanding
                print(
                    "\nJob #"
                    + str(current_job_number + 1)
                    + " Scheduled - "
                    + str(job_list_copy[current_job_number])
                    + " Units of Work"
                )

                # If there is still work left to be done on the job, do either 2 or less
                # units of work.
                if job_list_copy[current_job_number] > 0:
                    current_time += min(2, job_list_copy[current_job_number])
                    job_list_copy[current_job_number] = work_on_job(
                        job_list_copy[current_job_number]
                    )

                # If the current job is completed, then add it to the completed list so
                # we may skip it on the next pass.
                if job_list_copy[current_job_number] <= 0:
                    completed_job_indexes.append(current_job_number)
                    job_turnaround_times.append(current_time)
                    print("Job #" + str(current_job_number + 1) + " Complete")

                print("Current Time:", current_time)

        average_turnaround_time = round(sum(job_turnaround_times) / len(job_list), 2)

        print("\nAverage Turnaround Time:", average_turnaround_time, "Units of Work")
        print("----------------------")


def work_on_job(job_time):
    """Do work on job based on job_time. Return the amount of time left on the job.

    Args:
        job_time (int): Length of job.

    Returns:
        int: Will return 0 or job_time - 2 depending on the amount of work left.
    """
    work_time_left = max(0, job_time - 2)
    print("Doing " + str(abs(work_time_left - job_time)) + " Units of Work")
    return work_time_left
