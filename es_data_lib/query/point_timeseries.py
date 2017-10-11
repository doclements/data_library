# pylint: disable=W0311, C0301

import numpy as np

from .templates import point_extraction_timeseries
from es_data_lib.utils import create_query, web_post
from es_data_lib.query.query import Query


class PointTimeSeries(Query):
    def __init__(self, service, lat, lon, start_date, end_date, coverage, output=None):
        super(PointTimeSeries, self).__init__(service, coverage)
        self.template_params = {
            "lat": lat,
            "lon": lon,
            "time_label":self.coverage_time,
            "date1": start_date,
            "date2": end_date,
            "x_label":self.x_name,
            "y_label":self.y_name
        }
        self.output = output
        self.template = point_extraction_timeseries
        self._get_data()

    def _get_data(self):
        self.query = create_query(self)
        if self.output is not None:
            self.data = self._get_complex_output()
        else:
            self.data = np.array([float(x) for x in web_post(self.wcps_url, {"query":self.query})[1:-1].split(',')])


    def _get_complex_output(self):
        data_array = [float(x) for x in web_post(self.wcps_url, {"query":self.query})[1:-1].split(',')]
        for d in data_array:
            pass