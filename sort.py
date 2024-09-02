from pathlib import Path
import shutil
from concurrent.futures import ThreadPoolExecutor
import time

p = "D:\\Projects\\pythonProject11\\dir"
d = "D:\\Projects\\pythonProject11\\sorted_dir"


def directory_process(source_dir, target_dir):
    start_time = time.time()
    Path(target_dir).mkdir(parents=True, exist_ok=True)

    for file in Path(source_dir).rglob("*.*"):
        print(file)
        if file.is_file():
            file_extension = file.suffix
            extension_dir = Path(target_dir) / file_extension[1:]
            extension_dir.mkdir(exist_ok=True)
            shutil.copy(file, extension_dir / file.name)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")


if __name__ == "__main__":
    # directory_process(p, d)
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(directory_process, p, d)
