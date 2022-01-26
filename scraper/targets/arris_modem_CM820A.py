"""
Arris modem module.
"""
from lxml import html

from .arris_modem import ArrisModem, UpstreamItem, DownstreamItem

class ArrisModemCM820A(ArrisModem):
    """
    ArrisModem subclass that represents an Arris modem model CM820A
    running software 9.1.103S.
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
        # CM820A upstream tables have a blank record so set start record to 2 or higher
        rows = tree.xpath('/html/body/div[1]/div[3]/table[4]/tbody//tr[position()>2]')

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
