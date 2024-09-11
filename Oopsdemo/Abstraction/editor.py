
from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def debug(self):
        pass

class Vscode(Editor):

    def open(self):

        print("vscode open method")

    def execute(self):

        print("vscode execute method")

    def debug(self):

        print("vscode debug method")

vsc=Vscode()
vsc.open()