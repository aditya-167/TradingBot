import logging as lg
import os
from datetime import datetime 

def initialize_logging():
    log_dir = 'logs/'

    try:
        os.mkdir(log_dir)
    except OSError:
        print('Failed to create directory at {}'.format(log_dir))
    else:
        print("Succsessfuly created directory at {}".format(log_dir))

    date = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_name = date + '.log'
    curr_log_path = log_dir + log_name
    lg.basicConfig(filename=curr_log_path, format = '%(asctime)s - %(levelname)s: %(message)s',level = lg.DEBUG)

    lg.getLogger().addHandler(lg.StreamHandler())

    lg.info('Log Initialized')