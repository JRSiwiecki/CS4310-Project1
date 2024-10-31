def run_scheduler(batch_list):
    """Runs the Shortest-Job-First (SJF) Scheduler algorithm.

    Args:
        batch_list (List[List[int]]): A list where each inner list contains
        float values representing jobs.
    """
    print("----------- SJF Scheduler -----------")

    # Run scheduler for each job list in batch_list
    for batch_number, job_list in enumerate(batch_list):
        print("##### batch" + str(batch_number + 1) + ".txt #####")
        print(job_list)

        # Use copy of job_list so as to not modify underlying job_list
        job_list_copy = job_list.copy()
        completed_job_indexes = []
        job_turnaround_times = []
        current_time = 0

        # To find shortest job in list without just sorting (and possibly messing up
        # the job numbers), must make some passes through array to find the shortest job
        # and work on it once we find it.
        while len(completed_job_indexes) < len(job_list):

            # Any number we find in the job_list will be smaller than infinity, so we
            # begin the comparison at infinity
            shortest_job_time = float("inf")
            shortest_job_number = -1

            # Finds the shortest job in the list
            for i, time in enumerate(job_list_copy):
                if (
                    i not in completed_job_indexes
                    and time > 0
                    and time < shortest_job_time
                ):
                    shortest_job_time = time
                    shortest_job_number = i

            # Offset job number by 1 for display for easier understanding
            print(
                "\nJob #"
                + str(shortest_job_number + 1)
                + " Scheduled - "
                + str(job_list_copy[shortest_job_number])
                + " Units of Work"
            )

            current_time += job_list[shortest_job_number]
            job_list_copy[shortest_job_number] = work_on_job(
                job_list_copy[shortest_job_number]
            )
            completed_job_indexes.append(shortest_job_number)

            job_turnaround_times.append(current_time)

            print("Job #" + str(shortest_job_number + 1) + " Complete")
            print("Current Time:", current_time)

        average_turnaround_time = round(sum(job_turnaround_times) / len(job_list), 2)

        print("\nAverage Turnaround Time:", average_turnaround_time, "Units of Work")
        print("----------------------")


def work_on_job(job_time):
    """Do work on job based on job_time

    Args:
        job_time (int): Length of job.

    Returns:
        int: Always returns 0, as in SJF the entire job is completed in one go.
    """
    print("Doing " + str(job_time) + " Units of Work")
    return 0
