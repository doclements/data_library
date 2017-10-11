# pylint: disable=W0311

import hashlib
import os

from owslib.wcs import WebCoverageService
import json

from es_data_lib.utils import get_lat_long



class Service(object):
    def __init__(self, url, config_path=None):
        super(Service, self).__init__()
        self.url = url
        self.wcps_url = self.url+ '/wcps'
        self.url_hash = hashlib.md5(self.url).hexdigest()
        self.config_path = config_path
        # these two lists are to fix issues at the moemnt NEED TO BE REMOVED
        self.axis_removes = ['Lat','Lon','latitude','longitude','lat','lon','Long','long','Latitude', 'Longitude', 'Easting', 'Northing','E','N']
        self.banned = ['NCITest4', 'NCITest5', 'L8_B8_32631_15', 'LS8_test_tile']
        self.coverages = {}
        self._setup()




    def _setup(self):
        if not self.config_path:
           if not self.config_exists():
              print "config does not exists - CREATING new config"
              _fpath = os.path.join(os.path.dirname(__file__), 'configs', self.url_hash+'.json')
              with open(_fpath, 'w') as config_file:
                  self.init_config(config_file)
           else:
               #print "config found using cached copy - can edit / add to it"
               self._populate_from_cache()


    def get_config_filepath(self):
       return os.path.join(os.path.dirname(__file__), 'configs', self.url_hash+'.json')


    def config_exists(self):
        return os.path.isfile(os.path.join(os.path.dirname(__file__), 'configs', self.url_hash+'.json'))

    def init_config(self, config_file):
        _wcs = WebCoverageService(self.url, version="2.0.1")
        config = {}
        _covs = _wcs.contents.keys()
        config['coverages'] = {}
        for _cov in _covs:
            #print "writting coverage info for "+_cov
            #if _cov not in self.banned:
            try:
               t_cov = {}
               try:
                   t_cov['time_axis_name'] = [item for item in _wcs.contents[_cov].grid.axislabels if item not in self.axis_removes][0]
               except Exception, e:
                   t_cov['time_axis_name'] = ''
               spatial_axis = [item for item in _wcs.contents[_cov].grid.axislabels if item in self.axis_removes]
               del _wcs.contents[_cov]
               for p in spatial_axis:
                   t_cov[get_lat_long(p)+'_axis_name'] = p
               # gather X and Y coords definition
               t_cov['name'] = _cov
               config['coverages'][_cov] = t_cov
               self.coverages[_cov] = t_cov
            except Exception, e:
               print e
               print "coverage {} failed you should check it".format(_cov)
        config_file.write(json.dumps(config))
        return


    def _populate_from_cache(self):
       config_file = self.get_config_filepath()
       with open(config_file) as _config:
          config_obj = json.load(_config)
          self.config = config_obj
          self.coverages = config_obj['coverages']
