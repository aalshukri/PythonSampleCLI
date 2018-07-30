# -*- coding: utf-8 -*-
#from . import helpers

import helpers
#from . import helpers
import logging


def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        logging.debug(get_hmm())
