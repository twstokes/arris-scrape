"""
Outputters module.
"""

class Outputter():
    """
    Subclass this for outputting Items to something.
    """
    def output(self, items):
        """
        Output list of items.

        Args:
            items ([Item]): List of items to output.
        """

    def reset(self):
        """
        Reset the outputter.
        """
