import os
import subprocess as sp
from app import main as app
import re

ip = app

connect = f'adb connect {ip}'

sp.run(connect,stdout=sp.DEVNULL)

scrcpy = r'E:\Games\scrcpy\scrcpy.exe'

os.startfile(scrcpy)
