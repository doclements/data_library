# pylint: disable=W0311

point_extraction = """
for c in ({coverage})
return
encode (
   c[{y_label}({lat}), {x_label}({lon}), {time_label}("{date}")], "csv"
)
"""

point_extraction_no_date = """
for c in ({coverage})
return 
encode (
   c[{y_label}({lat}), {x_label}({lon})], "csv"
)
"""
area_extraction_no_date = """
for c in ({coverage})
return
encode (
   c[{y_label}({lat1}:{lat2}), {x_label}({lon1}:{lon2})], "{output}"
)
"""

area_extraction = """
for c in ({coverage})
return
encode (
   c[{y_label}({lat1}:{lat2}), {x_label}({lon1}:{lon2}), {time_label}("{date}")], "{output}"
)
"""
point_extraction_timeseries = """
for c in ({coverage})
return 
encode (
   c[{y_label}({lat}), {x_label}({lon}), {time_label}("{date1}":"{date2}")], "csv"
)
"""
area_timeseries_extraction = """
for c in ({coverage})
return
encode (
   c[{y_label}({lat1}:{lat2}), {x_label}({lon1}:{lon2}), {time_label}("{date1}":"{date2}")], "{output}"
)"""

landsat_rgb_area = """
for r in (L8_B6_{swath_id}), g in (L8_B5_{swath_id}), b in (L8_B4_{swath_id})
return 
encode ( {{
red:   ( (r * 0.00002) - 0.1 ) * 255;
green: ( (g * 0.00002) - 0.1 ) * 255;
blue:  ( (b * 0.00002) - 0.1 ) * 255
}}
[{y_label}({south}:{north}), {x_label}({west}:{east}), {time_label}("{date}")]
,"{png}")
"""

ndvi = """
for R in (L8_B4_{swath_id}), NIR in (L8_B5_{swath_id})
return 
encode( 
(
   ( (NIR*0.00002) - 0.1  ) - ( (R*0.00002) - 0.1 )  /
   ( (NIR*0.00002)  - 0.1 ) + ( (R*0.00002) - 0.1 ) 
)
[{y_label}({south}:{north}), {x_label}({west}:{east}), {time_label}("{date}")] * 200
, "png")
"""


ndwi_gao = """
for NIR in (L8_B5_32631_30), SWIR in (L8_B6_32631_30)
return 
encode( (
(
    255 * (NIR - SWIR) /
          (NIR + SWIR)
)
[E(377983:390000),N(4902991:4917275),unix(1433068497)] )
, "{output}")
"""


ndwi_mcfeeters = """
for NIR in (L8_B3_32631_30), SWIR in (L8_B5_32631_30)
return 
encode( (
(
    (NIR - SWIR) /
          (NIR + SWIR)
)
[E(377983:390000),N(4902991:4917275),unix(1433068497)] )
, "{output}")
"""

l8_cloudmask = """
for r in (L8_B6_{swath_id}), g in (L8_B5_{swath_id}), b in (L8_B4_{swath_id}), bq in (L8_BQA_{swath_id})
return 
encode ( {
red:   ( (r*(bq < 24576) * 0.00002) - 0.1 ) * 255;
green: ( (g*(bq < 24576) * 0.00002) - 0.1 ) * 255;
blue:  ( (b*(bq < 24576) * 0.00002) - 0.1 ) * 255
}
[E(377983:390000),N(4902991:4917275),unix(1433068497)]
,"{output}")
"""



ecmwf_1 = """
for c in (temp2m) 
return 
encode(
    (condense + over 
    $x x(imageCrsDomain(c[Lat(30.000000:50.000000), Long(5.000000:20.000000), ansi("2000-01-31T21:00":"2002-01-31T21:00")], ansi)) 
    using c[ansi($x)]/4)-273.15, "csv")
"""