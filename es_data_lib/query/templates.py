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
,"png")
"""
