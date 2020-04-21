from config import config as env

from os.path import basename
from string import digits
import datetime
import time
import shutil
import os

disk_type = "org.freedesktop.UDisks2"

def copy_data(disk_path):
    shutil.copy(src=env.FILE_PATH, dst=str(disk_path))
    print("Physical backup of data" + " at " +
          datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def _get_mount_point(device):
    with open("/proc/mounts", "r") as partitions:
        for info in partitions:
            for path in info.split():
                if device in basename(path):
                    properties = info.split()
                    return properties[1]

def new_drive_signal(path=None, properties=None):
    if disk_type + ".Drive" in properties:
        info = properties[disk_type + ".Drive"]
        print("\nDevice connected:", info["Id"])
        os.system('./save.sh')

    if disk_type + ".Block" in properties:
        time.sleep(1)
        device = basename(path)

        for char in device:
            if char in digits:
                print("New partition mounted:" + device)
                disk_path = _get_mount_point(device)
                if(disk_path != None):
                    print("Copying " + env.FILE_PATH + " file to:", disk_path)
                    copy_data(disk_path)
