from threading import Thread
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

import dbus

class USBListener(Thread):
    def __init__(self, callback_function):
        super().__init__()

        if not callable(callback_function):
            raise TypeError("Object is not callabble...")

        DBusGMainLoop(set_as_default=True)
        self.bus = dbus.SystemBus()

        self.signal = "InterfacesAdded"
        self.interface = "org.freedesktop.DBus.ObjectManager"
        self.bus.add_signal_receiver(
            callback_function, self.signal, self.interface)

    def run(self):
        loop = GLib.MainLoop()
        loop.run()
