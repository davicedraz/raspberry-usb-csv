import export as thread

backup_thread = thread.USBListener(thread.new_drive_signal)

backup_thread.start()
print("Waiting for USB connections ...")