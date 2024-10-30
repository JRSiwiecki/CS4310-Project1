def run_scheduler(batch_list):
    print("----------- FCFS Scheduler -----------")

    average_turnaround_times = []

    for batch_number, job_list in enumerate(batch_list):
        print("##### batch" + str(batch_number) + ".txt #####")
        print(job_list)

        completed_job_indexes = []
        job_complete_time = 0

        for job_number, job_time in enumerate(job_list):
            if job_number in completed_job_indexes:
                continue

            print("-----------")
            print("Job #" + str(job_number + 1) + " Scheduled")

            job_time = work_on_job(job_time)

            if job_time == 0:
                print("Job #" + str(job_number + 1) + " Complete")

                job_complete_time += job_list[job_number]
                completed_job_indexes.append(job_number)

        average_turnaround_time = round(job_complete_time / len(job_list), 2)
        average_turnaround_times.append(average_turnaround_time)

    print("-----------")
    print("Average Turnaround Time:", average_turnaround_times)


def work_on_job(job_time):
    print("Doing " + str(job_time) + " Units of Work")
    job_time = job_time - job_time
    print("Time Left: " + str(job_time))
    return job_time
