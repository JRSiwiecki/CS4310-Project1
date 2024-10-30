import job_input_reader
import fcfs


def main():
    batch_list = job_input_reader.job_file_to_array()

    fcfs.run_scheduler(batch_list)


if __name__ == "__main__":
    main()
