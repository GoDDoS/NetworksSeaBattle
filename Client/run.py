from tkinter import Tk
import socket

from server_listener import ServerListener
from view_factory import ViewFactory

root = Tk()
root.title('Морской бой')
root.resizable(width=False, height=False)
root.rowconfigure(1, weight=1)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('0.0.0.0', 47775))
    viewController = ViewFactory(root, sock)
    viewController.changeView('Menu')
    # run server listener
    ServerListener(viewController, sock).start()
except Exception:
    viewController = ViewFactory(root, '')
    viewController.changeView('Error')

root.mainloop()
