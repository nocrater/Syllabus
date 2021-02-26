import sys
from binding import *

from PyQt5.QtWidgets import QApplication

from registry.registry import Registry
from view.q_main import QMain

app = QApplication(sys.argv)


def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

sys._excepthook = sys.excepthook

sys.excepthook = my_exception_hook

window = QMain()
Registry.get_instance().set_main_presenter(window.get_presenter())
window.show()
app.exec_()