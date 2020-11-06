import os
import sys
import subprocess


USERNAME = os.environ['USERNAME']

def install_modules():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])


    except Exception as e:
        print(e)


def run_tasks():
    try:
        subprocess.check_call([sys.executable, "email.py"])
        subprocess.check_call([sys.executable, "tasks.py"])


    except Exception as e:
        print(e)


def main():
    install_modules()
    run_tasks()

if __name__ == "__main__":
    main()
