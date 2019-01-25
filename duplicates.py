import sys
import os
import os.path
from collections import defaultdict


def process_files(start_path, processor=lambda _: None):
    for directory, subdirectories, files in os.walk(start_path):
        for filename in files:
            full_path = os.path.join(directory, filename)
            processor(full_path)


def get_ident_key(path):
    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size
    return file_name, file_size


def add_file_to_storage(storage, path):
    storage[get_ident_key(path)].append(path)


def get_dublicates(storage):
    keys_with_dublicates = filter(lambda x: len(storage[x]) > 1, storage.keys())
    return map(lambda x: (x, storage[x]), keys_with_dublicates)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Please pass directory as a param")

    dirname = sys.argv[1]

    if not os.path.isdir(dirname):
        sys.exit("Please pass correct directory name")

    storage = defaultdict(list)

    process_files(sys.argv[1], lambda path: add_file_to_storage(storage, path))

    duplicates = list(get_dublicates(storage))

    if not duplicates:
        print("No dublicates detected")
        sys.exit()

    print("Next dublicates detected:")

    for duplication_info, duplicates_group in duplicates:
        print("Group `{0} - {1} byte(s)`".format(*duplication_info))
        print("\n".join(duplicates_group))
