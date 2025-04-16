import os
import shutil


def copy_content(files, source, target):
    if not files:
        return

    file = files.pop(0)

    if os.path.isfile(f"{source}/{file}"):
        shutil.copy(f"{source}/{file}", f"{target}/{file}")

    if os.path.isdir(f"{source}/{file}"):
        os.mkdir(f"{target}/{file}")
        for f in os.listdir(f"{source}/{file}"):
            files.append(f"/{file}/{f}")

    copy_content(files, source, target)


def clear_dir(target):
    shutil.rmtree(target)
    os.mkdir(target)


def copy(source, target):
    files = os.listdir(source)

    clear_dir(target)
    copy_content(files, source, target)
