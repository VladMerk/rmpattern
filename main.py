import argparse
import os


# def remove_prefix(root_dir: str, prefix: str) -> None:
#     for root, dirs, files in os.walk(root_dir):
#         for d in dirs:
#             if d.startswith(prefix):
#                 os.rename(os.path.join(root, d), os.path.join(root, d.replace(prefix, '')))
#                 remove_prefix(os.path.join(root, d[len(prefix):]), prefix)
#         for f in files:
#             if f.startswith(prefix):
#                 os.rename(os.path.join(root, f), os.path.join(root, f.replace(prefix, '')))

def remove_prefix(root_dir: str, prefix: str) -> None:
    for entry in os.listdir(root_dir):
        full_path = os.path.join(root_dir, entry)
        print(full_path)
        if os.path.isdir(full_path):
            new_name = os.path.join(root_dir, entry.replace(prefix, '').strip())
            os.rename(os.path.join(full_path), os.path.join(new_name))
            remove_prefix(new_name, prefix)
        elif os.path.isfile(full_path):
            new_name = os.path.join(root_dir, entry.replace(prefix, '').strip())
            os.rename(os.path.join(full_path), os.path.join(new_name))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', default='.', help="Path to the directory to process")
    parser.add_argument('-p', '--prefix', help="prefix to remove from file and directory name")
    args = parser.parse_args()

    remove_prefix(args.dir, args.prefix)
