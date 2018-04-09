# pylint: disable=W0311

from es_data_lib import services
from es_data_lib.query.point import Point
from es_data_lib.query.point_timeseries import PointTimeSeries
from es_data_lib.query.area import Area
from es_data_lib.query.area_timeseries import AreaTimeseries
from es_data_lib.service import Service

from es_data_lib.query.query import Query

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

from es_data_lib import logger as _log
import logging

fh = logging.FileHandler('spam.log')
#fh.setLevel(logging.INFO)

#print(_log)
_log.addHandler(fh)
_log.setLevel(logging.DEBUG)
#_service = services['pml']
service = Service("http://earthserver.pml.ac.uk/rasdaman/ows")

point = Point(service,55, -40,  service.coverages['OCCCI_V3_1_chlor_a_monthly'],band=".chlor_a",date="2006-06-01T00:00:00Z")

print point.data

# area = Area(service, 40, 65, -30, 10, service.coverages['OCCCI_V3_1_chlor_a_monthly'], band=".chlor_a", date="2006-09-01T00:00:00Z", output="csv")
# area.data[area.data == 9.96921e+36] = None
# plt.imshow(area.data, norm=matplotlib.colors.LogNorm())
# plt.show()
# point = Point(service,55, -40,  service.coverages['OCCCI_V3_monthly_chlor_a'],date="2006-06-01T00:00:00Z")

# print point.data


# print point.data


# pointTS = PointTimeSeries(service,55, -40, "2006-06-01T00:00:00Z","2006-10-01T00:00:00Z", service.coverages['OCCCI_V3_monthly_chlor_a'])
# print pointTS.data


# #ECMWF data test
# ecmwf_service = Service("http://earthserver.ecmwf.int/rasdaman/ows")

# ecwms_area = Area(ecmwf_service,-80, 80, -180, 179,   ecmwf_service.coverages['temp2m'],date="2012-01-01T06:00:00Z")
# print ecwms_area.data.shape
# print ecwms_area.data
# print np.min(ecwms_area.data)
# print np.max(ecwms_area.data)
# plt.imshow(np.flipud(np.rot90(ecwms_area.data)))
# plt.show()
# point = Point(ecmwf_service,50.347472, -4.217737, "2012-01-01T06:00:00Z", ecmwf_service.coverages['temp2m'])
# print point.data
# print point.data  - 273.15
# point = Point(ecmwf_service,50.347472, -4.217737, "2012-02-01T06:00:00Z", ecmwf_service.coverages['temp2m'])
# print point.data
# print point.data  - 273.15

# #ECMWF time series test
# point = PointTimeSeries(ecmwf_service,50.347472, -4.217737,  "2010-03-01T12:00:00Z", "2012-03-01T12:00:00Z", ecmwf_service.coverages['temp2m'])
# plt.plot([x - 273.15 for x in point.data][0::4])
# plt.show()


# jub_service = Service("http://access.planetserver.eu:8080/rasdaman/ows?")
# point = Point(jub_service, 562.6610837,298.2737483, jub_service.coverages['frt0000a0ac_07_if165l_trr3'])
# # print point.data

# meeo_service = Service('https://eodataservice.org/rasdaman/ows')

# print meeo_service.coverages['L8_RGB_32636_30']

# meeo_area = Area(meeo_service, 4902991, 4917275, 377983, 390000, meeo_service.coverages['L8_B5_32631_30'],date="2015-05-31T10:34:57Z" )
# print meeo_area.data.shape
# print meeo_area.data
# print np.min(meeo_area.data)
# print np.max(meeo_area.data)
# plt.imshow(meeo_area.data)
# plt.show()



