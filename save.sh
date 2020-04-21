#!/bin/bash

sudo mount -t vfat -o uid=pi,gid=pi /dev/sdb1 /media/usbstick/

cp /home/pi/data.csv /media/usbstick/

sudo umount /media/usbstick
