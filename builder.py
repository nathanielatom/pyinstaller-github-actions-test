from PyInstaller.__main__ import run

try:
    run(['sample.py'])
except BaseException as e:
    raise e
