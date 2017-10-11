# EarthServer Data Abstraction Library    


## Basic Info

The library allows the execution of WCPS without the need to understand WCPS. The basic interactions are pre-coded but the library can also act as a framework to create re-usable python code for more complex WCPS queries. You can find an example below in the `Complex Example` section

## Logging

The Library uses the builtin logging from the Python standard libs. We do not initialise the logger with a handler, e.g. log file. This is up to the user of the library to define. This allows greater freedom for the user as they can setup any log handler they choose. An example of a minimum setup can be found in `example.py`

## Complex Example 

The library can act as a framework for creating complex WCPS queries. As an example we have create the RGB Landsat query.  The steps to creating a new query are :-

 * Create the WCPS template
 * Create a class that extends `Query`
 * Have that class run the WCPS query and attach output, formatted as you like, to the data attribute.