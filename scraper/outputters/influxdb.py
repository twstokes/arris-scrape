from influxdb import InfluxDBClient
from .outputter import Outputter

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
