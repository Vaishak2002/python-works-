
from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def open(self):

        pass

    @abstractmethod
    def write(self):

        pass

    @abstractmethod
    def debug(self):

        pass

    @abstractmethod
    def execute(self):

        pass

class Vscode(Editor):

    def open(self):
        
        print("vs code open method")

    def write(self):
        
        print("vs code write method")

    def debug(self):
        
        print("vscode debug method")

    def execute(self):
        
        print("vscode execute method")

vscode_instance=Vscode()

vscode_instance.open()
vscode_instance.write()
vscode_instance.debug()
vscode_instance.execute()

