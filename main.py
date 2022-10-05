import os
import subprocess as sp


ip = '192.168.0.182'
connect = f'adb connect {ip}'

sp.run(connect,stdout=sp.DEVNULL)

scrcpy = r'E:\Games\scrcpy\scrcpy.exe'

os.startfile(scrcpy)
