# pylint: disable=W0311
import requests
from es_data_lib import x_y_lookup


def create_query(queryObj):
   queryObj.template_params['coverage'] = queryObj.coverage
   _q = queryObj.template.format(**queryObj.template_params)
   return _q


def web_post(url, payload):
   # remove question mark from URL if given
   url = url.replace('?','')
   # remove newline characters from template query
   payload['query'] = payload['query'].replace('\n', ' ')
   return requests.post(url, data=payload).text

def web_post_file(url, payload):
   return requests.post(url, data=payload).content


def get_lat_long(test_value):
   for p in x_y_lookup:
      if test_value in x_y_lookup[p]:
         return p
