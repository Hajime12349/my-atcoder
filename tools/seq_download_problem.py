import subprocess

if __name__ == "__main__":
    start = 10
    end = 10

    for i in range(start, end + 1):
        subprocess.call(f"sh tools/download_problem.sh abc{i:03d}", shell=True)
