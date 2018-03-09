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
[{y_label}({south}:{north}), {x_label}({west}:{east}), {time_label}("{date}")] )
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
[{y_label}({south}:{north}), {x_label}({west}:{east}), {time_label}("{date}")] )
, "{output}")
"""

l8_cloudmask = """
for r in (L8_B6_{swath_id}), g in (L8_B5_{swath_id}), b in (L8_B4_{swath_id}), bq in (L8_BQA_{swath_id})
return 
encode ( {{
red:   ( (r*(bq < 24576) * 0.00002) - 0.1 ) * 255;
green: ( (g*(bq < 24576) * 0.00002) - 0.1 ) * 255;
blue:  ( (b*(bq < 24576) * 0.00002) - 0.1 ) * 255
}}
[{y_label}({south}:{north}), {x_label}({west}:{east}), {time_label}("{date}")]
,"{output}")
"""



ecmwf_1 = """
for c in (temp2m) 
return 
encode(
    (coverage rainfall over 
    $x x(imageCrsDomain(c[{y_label}({south}:{north}), {x_label}({west}:{east}), {time_label}("{date1}":"{date2}")], ansi)) 
    values( avg(c[{y_label}({south}:{north}), {x_label}({west}:{east}),ansi($x)] - 273.15)) ), "csv")
    
"""

rrs_ratio = """
for a in (OCCCI_V3_monthly_rrs_{band1}), b in (OCCCI_V3_monthly_rrs_{band2})
return
encode (

((a[{y_label}({south}:{north}), {x_label}({west}:{east}), {time_label}("{date}")] < 100) * a[{y_label}({south}:{north}), {x_label}({west}:{east}), {time_label}("{date}")] ) / 
((b[{y_label}({south}:{north}), {x_label}({west}:{east}), {time_label}("{date}")] < 100) * b[{y_label}({south}:{north}), {x_label}({west}:{east}), {time_label}("{date}")] )
, "{output}", "nodata=9.96921e+36" )
"""