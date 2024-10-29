import job_input_reader


def main():
    batch_list = job_input_reader.job_file_to_array()
    print(batch_list)


if __name__ == "__main__":
    main()
