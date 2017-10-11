# EarthServer Data Abstraction Library    



## Basic Info

The library allows the execution of WCPS without the need to understand WCPS. The basic interactions are pre-coded but the library can also act as a framework to create re-usable python code for more complex WCPS queries. You can find an example below in the `Complex Example` section.  The basic flow of a query is :
 * initialise a `Service` object with the base URL of a WCPS endpoint.
  * internally the library now issues a combination of GetCapabilities and DescirbeCoverage requests to get info about all coverages, this info is stored for future use using the md5 hash of the URL given
 * The service object is then passed into which ever query type is desired
 * The coverage to be used in the query is also accessed by the Service object
 * The query is then sent to the service with data being marshalled into the appropriate format for further analysis or visualisation.  

## Logging

The Library uses the builtin logging from the Python standard libs. We do not initialise the logger with a handler, e.g. log file. This is up to the user of the library to define. This allows greater freedom for the user as they can setup any log handler they choose. An example of a minimum setup can be found in `complex_query_example.py`

## Complex Example 

The library can act as a framework for creating complex WCPS queries. As an example we have create the RGB Landsat query.  The steps to creating a new query are :-

 * Create the WCPS template
 * Create a class that extends `Query`
 * Have that class run the WCPS query and attach output, formatted as you like, to the data attribute.


 ## Dependencies

  * OWSLib - [https://github.com/earthserver-eu/OWSLib/tree/olcl-wcs-200] branch from our repo until it is merged back into main library