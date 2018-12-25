import os


HTML_PARSER_CONFIG = {
    "location_html_class": "O4GlU",
    "location_url_prefix": "/explore/locations/",
    "img_html_class": "FFVAD",
    "lat_property_value": "place:location:latitude",
    "lon_property_value": "place:location:longitude",
    "geckodriver_exec_path": os.path.join(
        os.path.dirname(__file__),
        "html_parser/geckodriver/geckodriver"
    ),
    "phantomjs_exec_path": os.path.join(
        os.path.dirname(__file__),
        "html_parser/phantomjs/phantomjs"
    )
}