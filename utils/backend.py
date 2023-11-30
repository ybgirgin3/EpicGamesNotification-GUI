from typing import DefaultDict, NamedTuple
import logging

from epicgamesnotification.commons._save import _save
from epicgamesnotification.utils.utils import open_file
from epicgamesnotification.apps.scrape.tasks import Scraper

from utils.utils import BackendState, Retailers, SaveOrNot, SendMail

scraper = Scraper()


def backend(state: BackendState):
    # collect vars
    # print(state)
    # print(state.retailer_id, state.save_or_not, state.send_mail)

    """
    Scrape ederken backend tarafina backend tarafina;
        • retailer_id
        • save_or_not
        • send_mail

    """
    print('raw state: ', state, list(SaveOrNot))

    _state = {
        # 'save': True if list(SaveOrNot)[state.save_or_not].value in (0, 1) else False,
        'open': True if list(SaveOrNot)[state.save_or_not].value in (0, 2) else False,
        'send_mail': True 
    }


    # scrape data
    # TODO: scrape kismi su an icin yalnizca epic icin tanimli oldugundan dolayi
    # direkt olarak scrape islemi yapabiliriz
    try:
        # scrape data
        data = scraper.scrape()

        # after scrape data if save?
        # if _state.get('save'):
        is_saved, saved_path_or_error = _save._save(data)
        print('saved?: ', is_saved, saved_path_or_error)
        if _state.get('open'):
            open_file(saved_path_or_error)
        if _state.get('send_mail'):
            print('mail sent')


    except Exception as e:
        pass

