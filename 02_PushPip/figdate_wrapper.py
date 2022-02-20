import venv
import subprocess
import shutil
import sys

venv.create('venv', with_pip=True)
subprocess.run(['./venv/bin/pip', 'install', 'pyfiglet'], capture_output=True)
if len(sys.argv) == 3:
    subprocess.run(['./venv/bin/python3', '-m', 'figdate', sys.argv[1], sys.argv[2]])
elif len(sys.argv) == 2:
    subprocess.run(['./venv/bin/python3', '-m', 'figdate', sys.argv[1]])
else:
    subprocess.run(['./venv/bin/python3', '-m', 'figdate'])
shutil.rmtree('venv')