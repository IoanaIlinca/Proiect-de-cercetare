import subprocess
import threading
from time import sleep


def run():
    for i in range(0, 5000):
        subprocess.check_call(
            [r"H:\Faculta\an 3\Genetic-Path-Finding\mainActivity.exe"])
        print("Iteration ", str(i))
        sleep(0.1)


if __name__ == "__main__":
    run()
