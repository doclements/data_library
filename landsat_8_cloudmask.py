
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cStringIO

from es_data_lib.query.templates import l8_cloudmask
from es_data_lib.utils import create_query, web_post, web_post_file
from es_data_lib.query.query import Query
from es_data_lib.service import Service


class L8CloudMask(Query):
    def __init__(self, service, south, north, west, east, date, coverage_id, output="png"):
        coverage = service.coverages['L8_B5_'+coverage_id]
        super(L8CloudMask, self).__init__(service, coverage)
        self.template_params = {
            "swath_id": coverage_id,
            "south": south,
            "north": north,
            "west": west,
            "east": east,
            "date": date,
            "time_label":self.coverage_time,
            "x_label":self.x_name,
            "y_label":self.y_name,
            "output" : output
        }
        self.output = output
        self.template = l8_cloudmask
        self._get_data()

    def _get_data(self):
        self.query = create_query(self)
        if self.output == "csv":
            self.data = web_post(self.wcps_url, {"query":self.query})[1:-1]
        if self.output == "netcdf":
            self.data = web_post_file(self.wcps_url, {"query":self.query})
        if self.output == "gtiff":
            self.data = web_post_file(self.wcps_url, {"query":self.query})
        if self.output == "png":
            self.data = web_post_file(self.wcps_url, {"query":self.query})


meeo_service = Service('https://eodataservice.org/rasdaman/ows')


meeo_area = L8CloudMask(meeo_service, 4900991, 4917275, 367983, 410000, "2015-05-31T10:34:57Z" , "32631_30",output="png")
# print meeo_area.data.shape
# print meeo_area.data
# print np.min(meeo_area.data)
# print np.max(meeo_area.data)
im = Image.open(cStringIO.StringIO(meeo_area.data))

im.show()
# plt.imshow(meeo_area.data)
# plt.show()
# with open("meeo_output.tif",'w') as output_file:
#     output_file.write(meeo_area.data)


# Image.open( "meeo_output.tif" ).show()