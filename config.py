import os


HTML_PARSER_CONFIG = {
    "location_html_class": "O4GlU",
    "location_url_prefix": "/explore/locations/",
    "post_img_html_class": "FFVAD",
    "location_img_html_class": "ECCnW",
    "lat_property_value": "place:location:latitude",
    "lon_property_value": "place:location:longitude",
    "phantomjs_exec_path": os.path.join(
        os.path.dirname(__file__),
        "html_parser/phantomjs/phantomjs"
    )
}