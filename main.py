from utilities import job_input_reader
from schedulers import fcfs, sjf, rr2, rr5


def main():
    batch_list = job_input_reader.job_file_to_array()

    fcfs.run_scheduler(batch_list)
    sjf.run_scheduler(batch_list)
    rr2.run_scheduler(batch_list)
    rr5.run_scheduler(batch_list)


if __name__ == "__main__":
    main()
