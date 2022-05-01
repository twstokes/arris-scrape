from .outputter import Outputter

class PrinterOutputter(Outputter):
    """
    Prints items to the screen.
    """
    def reset(self):
        pass

    @staticmethod
    def output(items):
        for item in items:
            print(item)
