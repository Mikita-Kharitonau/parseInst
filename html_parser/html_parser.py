import re
from selenium import (
    common,
    webdriver
)
from flask import (
    jsonify,
    abort
)


def get_parsed_location(post_url, config):
    driver = prepare_driver_with_url(post_url, config)
    try:
        location_dom = driver.find_element_by_class_name(config['location_html_class'])
        img_dom = driver.find_element_by_class_name(config['img_html_class'])
        try:
            location_details_url = location_dom.get_attribute("href")
            lat, lon = get_location_details(location_details_url, config)
            return jsonify(
                {
                    "id": get_location_id(location_details_url, config),
                    "place": location_dom.text,
                    "location": {
                        "lat": lat,
                        "lon": lon,
                    },
                    "photoSrc": img_dom.get_attribute("src")
                }
            )
        except:
            return jsonify({"place": "Can't get place info"})
    except common.exceptions.NoSuchElementException:
        return jsonify({ "place": "No place"})
    except:
        abort(500)
    finally:
        driver.quit()


def prepare_driver_with_url(url, config):
    driver = webdriver.PhantomJS(
        executable_path=config['phantomjs_exec_path']
    )
    driver.get(url)
    return driver


def get_location_id(location_details_url, config):
    return re.search(
        r'{prefix}(\d+)/\w*'.format(prefix=config['location_url_prefix']),
        location_details_url)\
        .group(1)


def get_location_details(location_details_url, config):
    driver = prepare_driver_with_url(location_details_url, config)

    lat = driver.find_element_by_xpath(
        "//meta[@property='{lat}']".format(lat=config['lat_property_value'])
    ).get_attribute("content")

    lon = driver.find_element_by_xpath(
        "//meta[@property='{lon}']".format(lon=config['lon_property_value'])
    ).get_attribute("content")

    driver.quit()
    return lat, lon


