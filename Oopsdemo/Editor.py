

class Editor:

    def __init__(self,name,vendor):

        self.name=name
        self.vendor=vendor

    def open(self):

        print(f"{self.name} open")

    def execute(self):

        print(f"{self.name} execute")

class Vscode(Editor):

    def __init__(self, name, vendor):
         
         super().__init__(name, vendor)

class Pycharm(Editor):

    def __init__(self, name, vendor):

        super().__init__(name, vendor)

vsc_intance=Vscode("VisualStudioCode","vscvendor")
vsc_intance.open()

pyc_instance=Pycharm("Pycharm","jstbrains")
pyc_instance.open()
pyc_instance.execute()