import json
import sys

import common
from . import datasource


def load():
    pass


def load_json_file(file_path):
    with open(file_path) as json_file:
        return json.load(json_file)


file_name = common.safe_list_get(sys.argv, 1, '')
conf = load_json_file("{}_settings.json".format(file_name))

db_config = conf.get('datasource')
db = datasource.get_mongo_db(db_config['host'], db_config['port'], db_config['db-name'])
