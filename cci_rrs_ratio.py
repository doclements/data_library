
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cStringIO

from es_data_lib.query.templates import rrs_ratio
from es_data_lib.utils import create_query, web_post, web_post_file
from es_data_lib.query.query import Query
from es_data_lib.service import Service


class CCIRrsRatio(Query):
    def __init__(self, service, south, north, west, east, date, band1,band2, output="netcdf"):
        coverage = service.coverages['OCCCI_V3_monthly_rrs_'+band1]
        super(CCIRrsRatio, self).__init__(service, coverage)
        self.template_params = {
            "band1": band1,
            "band2": band2,
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
        self.template = rrs_ratio
        self._get_data()

    def _get_data(self):
        self.query = create_query(self)
        if self.output == "csv":
            self.data = web_post(self.wcps_url, {"query":self.query})
        if self.output == "netcdf":
            self.data = web_post_file(self.wcps_url, {"query":self.query})
        if self.output == "gtiff":
            self.data = web_post_file(self.wcps_url, {"query":self.query})
        if self.output == "png":
            self.data = web_post_file(self.wcps_url, {"query":self.query})


pml_service = Service('http://earthserver.pml.ac.uk/rasdaman/ows')


rrs_ratio_out = CCIRrsRatio(pml_service, -80, 80, -180, 179,  "2005-05-01T00:00:00.000Z" , "412","555",output="netcdf")
# print meeo_area.data.shape
# print meeo_area.data
# print np.min(meeo_area.data)
# print np.max(meeo_area.data)
# im = Image.open(cStringIO.StringIO(rrs_ratio.data))

# im.show()
# plt.imshow(meeo_area.data)
# plt.show()
with open("rrs_test",'wb') as output_file:
    output_file.write(rrs_ratio_out.data)


# Image.open( "meeo_output.tif" ).show()