# pylint: disable=W0311
import numpy as np

from .templates import area_extraction, area_extraction_no_date
from es_data_lib.utils import create_query, web_post, web_post_file
from es_data_lib.query.query import Query

class Area(Query):
    def __init__(self, service, lat1,lat2, lon1, lon2, coverage, band='', output="csv",date=None):
        super(Area, self).__init__(service, coverage)
        self.template_params = {
            "lat1": lat1,
            "lat2": lat2,
            "lon1": lon1,
            "lon2": lon2,
            "date": date,
            "time_label":self.coverage_time,
            "x_label":self.x_name,
            "y_label":self.y_name,
            "output": output,
            "band" : band
        }
        self.output = output
        if date is None:
            self.template = area_extraction_no_date
        else:
           self.template = area_extraction


    def _get_data(self):
        self.query = create_query(self)
        if self._data is None:
            if self.output == "csv":
                self._data = web_post(self.wcps_url, {"query":self.query})[1:-1]
                self._data = self._data.split('},{')
                self._data = [x.split(',') for x in self._data]
                self._data = np.array(self._data)
                self._data = self._data.astype(np.float)
            if self.output == "netcdf":
                self._data = web_post_file(self.wcps_url, {"query":self.query})
            if self.output == "gtiff":
                self._data = web_post_file(self.wcps_url, {"query":self.query})
        else:
            return self._data
 
        return self._data

    data = property(_get_data, None)