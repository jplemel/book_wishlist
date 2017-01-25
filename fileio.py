import os


def write_to_file(write_directory, file_name, output_data):
    # Create data directory
    try:
        os.mkdir(write_directory)
    except FileExistsError:
        pass  # Ignore - if directory exists, don't need to do anything.

    with open(file_name, 'w') as f:
        f.write(output_data)
