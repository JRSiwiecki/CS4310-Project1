def run_scheduler(batch_list):
    print("----------- FCFS Scheduler -----------")

    for batch_number, job_list in enumerate(batch_list):
        print("##### batch" + str(batch_number + 1) + ".txt #####")
        print(job_list)
        job_list_copy = job_list.copy()
        completed_job_indexes = []
        job_turnaround_times = []
        current_time = 0

        for job_number, job_time in enumerate(job_list):
            print(
                "\nJob #"
                + str(job_number + 1)
                + " Scheduled - "
                + str(job_list_copy[job_number])
                + " Units of Work"
            )

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
    print("Doing " + str(job_time) + " Units of Work")
    return 0
