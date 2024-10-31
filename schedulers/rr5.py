def run_scheduler(batch_list):
    print("----------- Round Robin 5 Scheduler -----------")

    for batch_number, job_list in enumerate(batch_list):
        print("##### batch" + str(batch_number + 1) + ".txt #####")
        print(job_list)
        job_list_copy = job_list.copy()
        completed_job_indexes = []
        job_turnaround_times = []
        current_time = 0

        while len(completed_job_indexes) < len(job_list):
            for current_job_number in range(len(job_list)):
                if current_job_number in completed_job_indexes:
                    continue

                print(
                    "\nJob #"
                    + str(current_job_number + 1)
                    + " Scheduled - "
                    + str(job_list_copy[current_job_number])
                    + " Units of Work"
                )

                if job_list_copy[current_job_number] > 0:
                    current_time += min(5, job_list_copy[current_job_number])
                    job_list_copy[current_job_number] = work_on_job(
                        job_list_copy[current_job_number]
                    )

                if job_list_copy[current_job_number] <= 0:
                    completed_job_indexes.append(current_job_number)
                    job_turnaround_times.append(current_time)
                    print("Job #" + str(current_job_number + 1) + " Complete")

                print("Current Time:", current_time)

        average_turnaround_time = round(sum(job_turnaround_times) / len(job_list), 2)

        print("\nAverage Turnaround Time:", average_turnaround_time, "Units of Work")
        print("----------------------")


def work_on_job(job_time):
    work_time_left = max(0, job_time - 5)
    print("Doing " + str(abs(work_time_left - job_time)) + " Units of Work")
    return work_time_left
