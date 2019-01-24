import sys
import os
import os.path
from collections import defaultdict


def process_files(start_path, processor=lambda _: None):
    for directory, subdirectories, files in os.walk(start_path):
        for filename in files:
            full_path = os.path.join(directory, filename)
            processor(full_path)


class DuplicatesStatHandler:
    def __init__(self):
        self.storage = defaultdict(list)

    def get_ident_key(self, path):
        file_name = os.path.basename(path)
        file_size = os.stat(path).st_size
        return file_name, file_size

    def add_file(self, path):
        key = self.get_ident_key(path)
        self.storage[key].append(path)

    def get_dublicates(self):
        keys_with_dublicates = filter(lambda x: len(self.storage[x]) > 1, self.storage.keys())
        return map(lambda x: (x, self.storage[x]), keys_with_dublicates)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Please pass directory as a param")

    dirname = sys.argv[1]

    if not os.path.isdir(dirname):
        sys.exit("Please pass correct directory name")

    duplicate_handler = DuplicatesStatHandler()

    process_files(sys.argv[1], duplicate_handler.add_file)

    duplicates = list(duplicate_handler.get_dublicates())

    if not duplicates:
        sys.exit("No dublicates detected")

    print("Next dublicates detected:")

    for duplication_info, duplicates_group in duplicates:
        print("Group `{0} - {1} byte(s)`".format(*duplication_info))
        print("\n".join(duplicates_group))
