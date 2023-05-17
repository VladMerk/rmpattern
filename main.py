import argparse
import os


def remove_prefix(root_dir: str, prefix: str) -> None:
    for entry in os.listdir(root_dir):
        full_path = os.path.join(root_dir, entry)
        if os.path.isdir(full_path):
            new_name = os.path.join(root_dir, entry.replace(prefix, "").strip())
            os.rename(os.path.join(full_path), os.path.join(new_name))
            remove_prefix(new_name, prefix)
        elif os.path.isfile(full_path):
            new_name = os.path.join(root_dir, entry.replace(prefix, "").strip())
            os.rename(os.path.join(full_path), os.path.join(new_name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prefix", help="prefix to remove from file and directory name")
    args = parser.parse_args()

    remove_prefix("/data", args.prefix)
