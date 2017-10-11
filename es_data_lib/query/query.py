# pylint: disable=W0311

class Query(object):
    def __init__(self, service, coverage):
        super(Query, self).__init__()
        self.service = service
        self.wcps_url = service.wcps_url
        self.coverage = coverage['name']
        self.coverage_time = str(coverage['time_axis_name'])
        self.x_name = str(coverage['X_axis_name'])
        self.y_name = str(coverage['Y_axis_name'])

        self._data = None
       