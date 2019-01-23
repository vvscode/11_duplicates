import sys
import os
import os.path


def deep_files_iterate(start_path, processor=lambda _: None):
    for entity in os.scandir(start_path):
        if entity.is_dir():
            deep_files_iterate(entity.path, processor)
        else:
            processor(entity.path)


class DuplicatesStatHandler:
    def __init__(self):
        self.storage = {}

    def get_ident_key(self, path):
        filename = os.path.basename(path)
        file_size = os.stat(path).st_size
        return "{} with size {}".format(filename, file_size)

    def add_file(self, path):
        key = self.get_ident_key(path)
        if key not in self.storage:
            self.storage[key] = []

        self.storage[key].append(path)

    def get_dublicates(self):
        keys_with_dublicates = filter(lambda x: len(self.storage[x]) > 1, self.storage.keys())
        return map(lambda x: (x, self.storage[x]), keys_with_dublicates)


if len(sys.argv) < 2:
    sys.exit("Please pass directory as a param")

dirname = sys.argv[1]

if not os.path.isdir(dirname):
    sys.exit("Please pass correct directory name")

duplicate_handler = DuplicatesStatHandler()

deep_files_iterate(sys.argv[1], duplicate_handler.add_file)

duplicates = list(duplicate_handler.get_dublicates())

if not duplicates:
    sys.exit("No dublicates detected")

print("Next dublicates detected:")

for group_name, duplicates_group in duplicates:
    print("Group `{}`".format(group_name))
    print("\n".join(duplicates_group))
