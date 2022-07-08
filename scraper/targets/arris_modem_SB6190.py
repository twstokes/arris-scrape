"""
Arris modem module.
"""
from lxml import html

from bs4 import BeautifulSoup
from .arris_modem import ArrisModem, UpstreamItem, DownstreamItem

class ArrisModemSB6190(ArrisModem):
    """
    ArrisModem subclass that represents an Arris modem model SB6190
    running software 
    """

    def get_downstream_items(self,html_string):
        """
        Function to convert an HTML string to a list of DownstreamItems.

        Args:
            html_string (string): HTML

        Returns:
            [DownstreamItem]: List of DownstreamItems
        """

        # Use BeautifulSoup with html5lib. lxml doesn't play well with the SB6190.
        soup = BeautifulSoup(html_string, 'html5lib')
        
        # key order must match the table column layout
        keys = [
            'downstream_id',
            'lock_status',
            'modulation',
            'dcid',
            'freq',
            'power',
            'snr',
            'correcteds',
            'uncorrectables',
            'octets',
        ]
        items = []
        
        for table_row in soup.find_all("table")[2].find_all("tr")[2:]:
            if table_row.th:
                continue
            channel = table_row.find_all('td')[0].text.strip()
            lock_status = table_row.find_all('td')[1].text.strip()
            modulation = table_row.find_all('td')[2].text.strip()
            channel_id = table_row.find_all('td')[3].text.strip()
            frequency = table_row.find_all('td')[4].text.replace(" Hz", "").strip()
            power = table_row.find_all('td')[5].text.replace(" dBmV", "").strip()
            snr = table_row.find_all('td')[6].text.replace(" dB", "").strip()
            corrected = table_row.find_all('td')[7].text.strip()
            uncorrectables = table_row.find_all('td')[8].text.strip()
            octets = "0"

            values = ( channel, lock_status, modulation, channel_id, frequency, power, snr, corrected, uncorrectables, octets)
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
        # Use BeautifulSoup with html5lib. lxml doesn't play well with the SB6190.
        soup = BeautifulSoup(html_string, 'html5lib')

        # key order must match the table column layout
        keys = [
            'upstream_id',
            'lock_status',
            'channel_type',
            'ucid',
            'symbol_rate',
            'freq',
            'power',
        ]

        items = []

        # upstream table
        for table_row in soup.find_all("table")[3].find_all("tr")[2:]:
            if table_row.th:
                continue
            upstream_id = table_row.find_all('td')[0].text.strip()
            lock_status = table_row.find_all('td')[1].text.strip()
            channel_type = table_row.find_all('td')[2].text.strip()
            ucid = table_row.find_all('td')[3].text.strip()
            symbol_rate = table_row.find_all('td')[4].text.replace(" kSym/sec", "").strip()
            freq = table_row.find_all('td')[5].text.replace(" Hz", "").strip()
            power = table_row.find_all('td')[6].text.replace(" dBmV", "").strip()

            values = (upstream_id, lock_status, channel_type, ucid, symbol_rate, freq, power )
            zipped = dict(zip(keys, values))
            items.append(UpstreamItem(zipped.items()))

        return items
