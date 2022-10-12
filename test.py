import os
import subprocess as sp

import re

ip = ''

connect = f'adb connect {ip}'

sp.run(connect,stdout=sp.DEVNULL)

scrcpy = r'E:\Games\scrcpy\scrcpy.exe'

os.startfile(scrcpy)
