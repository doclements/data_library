# pylint: disable=W0311

import logging
from .templates import point_extraction, point_extraction_no_date
from es_data_lib.utils import create_query, web_post
from es_data_lib.query.query import Query
import sys

class Point(Query):
    def __init__(self, service, lat, lon, coverage, band='', date=None):
        super(Point, self).__init__(service, coverage)
        self.template_params = {
            "lat": lat,
            "lon": lon,
            "date": date,
            "time_label":self.coverage_time,
            "x_label":self.x_name,
            "y_label":self.y_name,
            "band": band
        }
        self.logger = logging.getLogger(__name__)
        if date is None:
            self.template = point_extraction_no_date
        else:
            self.template = point_extraction
        

    def _get_data(self):
        self.query = create_query(self)
        if not self._data:
            try:
                t_data = web_post(self.wcps_url, {"query":self.query})[1:-1]    
                self._data = float(t_data)
            except ValueError, e:
                try:
                    self.logger.info("trying to marshal result into array due to %s", e)
                    self._data = [float(x) for x in t_data.split(' ')]
                except Exception, e:
                    self.logger.error(sys.exc_info()[0])
                    self.logger.error(self.query)
        else:
            return self._data
        
        return self._data
    
    data = property(_get_data, None)