"""
Outputters module.
"""
from influxdb import InfluxDBClient


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

class InfluxDBOutputter(Outputter):
    """
    InfluxDB Outputter subclass.
    """
    client = None
    config = None

    def __init__(self, config):
        self.config = config
        self._setup()

    def __del__(self):
        if self.client is not None:
            self.client.close()

    def _setup(self):
        if self.client is not None:
            self.client.close()
        self.client = InfluxDBClient(**self.config)
        self.client.create_database(self.config['database'])

    def reset(self):
        self._setup()

    def output(self, items):
        points = list(map(lambda i: i.output_for_influxdb(), items))
        self.client.write_points(points)
