
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cStringIO

from es_data_lib.query.templates import ecmwf_1
from es_data_lib.utils import create_query, web_post, web_post_file
from es_data_lib.query.query import Query
from es_data_lib.service import Service


class Temp2MAvg(Query):
    def __init__(self, service, south, north, west, east, date1, date2,  output="csv"):
        coverage = service.coverages['temp2m']
        super(Temp2MAvg, self).__init__(service, coverage)
        self.template_params = {
            "south": south,
            "north": north,
            "west": west,
            "east": east,
            "date1": date1,
            "date2": date2,
            "time_label":self.coverage_time,
            "x_label":self.x_name,
            "y_label":self.y_name,
            "output" : output
        }
        self.output = output
        self.template = ecmwf_1
        self._get_data()

    def _get_data(self):
        self.query = create_query(self)
        if self.output == "csv":
            self.data = web_post(self.wcps_url, {"query":self.query})#[1:-1]
        if self.output == "netcdf":
            self.data = web_post_file(self.wcps_url, {"query":self.query})
        if self.output == "gtiff":
            self.data = web_post_file(self.wcps_url, {"query":self.query})
        if self.output == "png":
            self.data = web_post_file(self.wcps_url, {"query":self.query})


ecmwf_service = Service('http://earthserver.ecmwf.int/rasdaman/ows')


temperature_array = Temp2MAvg(ecmwf_service, 30, 50, 5, 20, "2000-01-31T21:00","2002-01-31T21:00")
# print meeo_area.data
# print np.min(meeo_area.data)
# print np.max(meeo_area.data)
data_arr = np.array(temperature_array.data.split(','))
plt.plot(data_arr)
plt.show()
# with open("meeo_output.tif",'w') as output_file:
#     output_file.write(meeo_area.data)


# Image.open( "meeo_output.tif" ).show()


#Lat(30.000000:50.000000), Long(5.000000:20.000000
#ansi("2000-01-31T21:00":"2002-01-31T21:00")