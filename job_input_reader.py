JOB_FOLDER_PATH = "job-files/"
NUMBER_OF_BATCHES = 3


def job_file_to_array():
    batch_list = []

    for i in range(1, NUMBER_OF_BATCHES + 1):
        with open(
            JOB_FOLDER_PATH + "batch" + str(i) + ".txt", "r", encoding="utf-8"
        ) as file:
            job_list = []

            for line in file.readlines():
                if line[0] == "J":
                    continue

                job_list.append(int(line))

            batch_list.append(job_list)

    return batch_list
