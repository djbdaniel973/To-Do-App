import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        filepath = pathlib.Path(filepath)
        for filepath in filepaths:
            archive.write(filepath, arcname=filepath.name)


if  __name__ == "__main__":
    make_archive(filepaths=["Experiment 4", "Experiment 5.B"], dest_dir="dest")
