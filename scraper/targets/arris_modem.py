"""
Arris modem module.
"""
from lxml import html

from ..target import Target
from ..items import InfluxableItem


class ArrisModem(Target):
    """
    Target subclass that represents an Arris modem model

    Args:
        Target (string): [HTML]
    """
    
    def extract_items_from_html(self, html_string):
        # get items from the downstream table
        downstream_items = self.get_downstream_items(html_string)
        # get items from the upstream table
        upstream_items = self.get_upstream_items(html_string)

        return downstream_items + upstream_items

    def get_downstream_items(self,html_string):
        """
        Function to convert an HTML string to a list of DownstreamItems.

        Args:
            html_string (string): HTML

        Returns:
            [DownstreamItem]: List of DownstreamItems
        """
        # Override in subclass for individual modem model
        pass


    def get_upstream_items(self,html_string):
        """
        Function to convert an HTML string to a list of UpstreamItems.

        Args:
            html_string (string): HTML

        Returns:
            [UpstreamItem]: List of UpstreamItems
        """
        # Override in subclass for individual modem model
        pass

class DownstreamItem(InfluxableItem):
    """
    InfluxableItem subclass that represents a downstream table row.
    """
    snr = None
    dcid = None
    freq = None
    power = None
    octets = None
    correcteds = None
    modulation = None
    downstream_id = None
    uncorrectables = None

    def output_for_influxdb(self):
        return {
            'measurement': 'downstream',
            'tags': {
                'downstream_id': self.downstream_id,
                'modulation': self.modulation
            },
            'fields': {
                'snr': self.float_at_pos(self.snr),
                'dcid': self.int_at_pos(self.dcid),
                'freq': self.float_at_pos(self.freq),
                'power': self.float_at_pos(self.power),
                'octets': self.int_at_pos(self.octets),
                'correcteds': self.int_at_pos(self.correcteds),
                'uncorrectables': self.int_at_pos(self.uncorrectables)
            }
        }

class UpstreamItem(InfluxableItem):
    """
    InfluxableItem subclass that represents an upstream table row.
    """
    freq = None
    ucid = None
    power = None
    modulation = None
    symbol_rate = None
    upstream_id = None
    channel_type = None

    def output_for_influxdb(self):
        return {
            'measurement': 'upstream',
            'tags': {
                'upstream_id': self.upstream_id,
                'modulation': self.modulation,
                'channel_type': self.channel_type
            },
            'fields': {
                'ucid': self.int_at_pos(self.ucid),
                'freq': self.float_at_pos(self.freq),
                'power': self.float_at_pos(self.power),
                'symbol_rate': self.int_at_pos(self.symbol_rate)
            }
        }



