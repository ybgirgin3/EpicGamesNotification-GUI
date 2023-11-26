from typing import DefaultDict, NamedTuple
import logging

# from epicgamesnotification.commons._mail import _mail
from epicgamesnotification.commons._save import _save
from epicgamesnotification.commons._scrape import _scrape
from epicgamesnotification.utils.utils import open_file

from utils.utils import BackendState


def backend(state: BackendState):
    # collect vars
    retailer = type(state.retailer)
    print(retailer.value)
    # retailer = state.retailer
    # print("retailer", retailer)
    # save_or_not = state.save_or_not
    # send_mail: bool = state.send_mail

    # logging.info("selected retailer in backend", retailer)
    # logging.info("selected retailer in backend", save_or_not)
    # logging.info("selected retailer in backend", send_mail)

    # scrape data
    # data = _scrape._scrape()
