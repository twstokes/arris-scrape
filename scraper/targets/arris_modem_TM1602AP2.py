"""
Arris modem module.
"""
from lxml import html

from ..target import Target
from ..items import InfluxableItem
from .arris_modem import ArrisModem, UpstreamItem, DownstreamItem

class ArrisModemTM1602AP2(ArrisModem):
    """
    Target subclass that represents an Arris modem model TM1602AP2
    running software 9.1.103J6J.

    Args:
        Target (string): [HTML]
    """

    def get_downstream_items(self,html_string):
        """
        Function to convert an HTML string to a list of DownstreamItems.

        Args:
            html_string (string): HTML

        Returns:
            [DownstreamItem]: List of DownstreamItems
        """
        tree = html.fromstring(html_string)
        # grab the downstream table and skip the first row
        rows = tree.xpath('/html/body/div[1]/div[3]/table[2]/tbody//tr[position()>1]')

        # key order must match the table column layout
        keys = [
            'downstream_id',
            'dcid',
            'freq',
            'power',
            'snr',
            'modulation',
            'octets',
            'correcteds',
            'uncorrectables'
        ]

        items = []

        for row in rows:
            values = row.xpath('td/text()')
            zipped = dict(zip(keys, values))
            items.append(DownstreamItem(zipped.items()))

        return items

    def get_upstream_items(self,html_string):
        """
        Function to convert an HTML string to a list of UpstreamItems.

        Args:
            html_string (string): HTML

        Returns:
            [UpstreamItem]: List of UpstreamItems
        """
        tree = html.fromstring(html_string)
        # grab the upstream table and skip the first row
        rows = tree.xpath('/html/body/div[1]/div[3]/table[4]/tbody//tr[position()>1]')

        # key order must match the table column layout
        keys = [
            'upstream_id',
            'ucid',
            'freq',
            'power',
            'channel_type',
            'symbol_rate',
            'modulation'
        ]

        items = []

        for row in rows:
            values = row.xpath('td/text()')
            zipped = dict(zip(keys, values))
            items.append(UpstreamItem(zipped.items()))

        return items
