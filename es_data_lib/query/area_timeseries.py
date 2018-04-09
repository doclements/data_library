# pylint: disable=W0311
import numpy as np

from .templates import area_timeseries_extraction
from es_data_lib.utils import create_query, web_post, web_post_file
from es_data_lib.query.query import Query

class AreaTimeseries(Query):
    def __init__(self, service, lat1,lat2, lon1, lon2, start_date, end_date, coverage, band='',output="csv"):
        super(AreaTimeseries, self).__init__(service, coverage)
        self.template_params = {
            "lat1": lat1,
            "lat2": lat2,
            "lon1": lon1,
            "lon2": lon2,
            "date1": start_date,
            "date2": end_date,
            "output": output,
            "time_label":self.coverage_time,
            "x_label":self.x_name,
            "y_label":self.y_name,
            "band" : band

        }
        self.output = output
        self.template = area_timeseries_extraction
        self._get_data()


    def _get_data(self):
        self.query = create_query(self)
        if self.output == "csv":
            self.data = web_post(self.wcps_url, {"query":self.query})
            self.data = self.data[2:-2]
            self.data = self.data.split('}},{{')

            self.data = [x.split('},{') for x in self.data]
            self.data = [[x.split(',') for x in y] for y in self.data]
            self.data = np.array(self.data)
            self.data = self.data.astype(np.float)
        if self.output == "netcdf":
            self.data = web_post_file(self.wcps_url, {"query":self.query})
        if self.output == "geotiff":
            self.data = web_post_file(self.wcps_url, {"query":self.query})
