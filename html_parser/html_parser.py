import re
from selenium import (
    common,
    webdriver
)
from flask import (
    jsonify,
    abort,
    make_response
)
from urllib import request
from bs4 import BeautifulSoup


def get_parsed_location(post_url, config):
    try:
        driver = prepare_driver_with_url(post_url, config)
    except:
        return make_response(jsonify({"error": "Can't initialize webdriver"}), 500)
    try:
        location_dom = driver.find_element_by_class_name(config['location_html_class'])
        try:
            location_details_url = location_dom.get_attribute('href')
            lat, lon, location_img_url = get_location_details(location_details_url, config)
            return jsonify(
                {
                    "id": get_location_id(location_details_url, config),
                    "place": location_dom.text,
                    "location": {
                        "lat": lat,
                        "lon": lon,
                    },
                    "photoSrc": location_img_url
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

    location_img_url = driver.find_element_by_class_name(
        config['location_img_html_class']).get_attribute("src")

    driver.quit()
    return lat, lon, location_img_url


def get_location_details_with_urllib(location_details_url, config):
    response = request.urlopen(location_details_url)
    html = response.read()
    soup = BeautifulSoup(html)
    lat = soup.find("meta", property=config['lat_property_value']).get('content', 0)
    lon = soup.find("meta", property=config['lon_property_value']).get('content', 0)
    # location_img_url = soup.findAll("img", class_=config['location_img_html_class'])[0].get('src', 'No value')
    return lat, lon




