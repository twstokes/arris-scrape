import os
import sys
import traceback

# adds the parent to the path
parent_path = os.path.abspath('..')
sys.path.insert(1, parent_path)

from config import debug_config
from scraper.outputters.printer import PrinterOutputter

MODEM_URL = debug_config['modem_url']
MODEM_MODEL = debug_config['modem_model']
IS_REMOTE = debug_config['is_remote']

if IS_REMOTE:
    from scraper.downloaders.requests import RequestsDownloader
else:
    from scraper.downloaders.local import LocalDownloader

def run_debugger():
    """
    Starts the debugger.
    """
    print("Starting debugger.")

    target = get_target(MODEM_MODEL)
    outputter = PrinterOutputter
    downloader = get_downloader()

    try:
        body = downloader.download(MODEM_URL)
        items = target.extract_items_from_html(body)
        outputter.output(items)
    except BaseException as err:
        traceback.print_exception(err)

def get_target(model):
    if model == "SB6183":
        from scraper.targets.arris_modem_SB6183 import ArrisModemSB6183
        return ArrisModemSB6183()
    if model == "TM1602AP2":
        from scraper.targets.arris_modem_TM1602AP2 import ArrisModemTM1602AP2
        return ArrisModemTM1602AP2()
    if model == "CM802A":
        from scraper.targets.arris_modem_CM820A import ArrisModemCM820A
        return ArrisModemCM820A()
    if model == "SB6190":
        from scraper.targets.arris_modem_SB6190 import ArrisModemSB6190
        return ArrisModemSB6190()

def get_downloader():
    if IS_REMOTE:
        return RequestsDownloader()

    return LocalDownloader()

if __name__ == "__main__":
    run_debugger()
