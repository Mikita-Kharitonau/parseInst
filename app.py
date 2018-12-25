import os

from flask import (
    Flask,
    jsonify,
    request,
    abort,
    make_response
)
from html_parser import get_parsed_location
from config import HTML_PARSER_CONFIG


app = Flask(__name__)


@app.route('/api/location', methods=['POST'])
def get_location():
    if not request.json or not 'post_url' in request.json:
        abort(400)
    location = get_parsed_location(request.json['post_url'], HTML_PARSER_CONFIG)
    return location


@app.errorhandler(400)
def bad_request(e):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(500)
def internal_server_error(e):
    return make_response(jsonify({'error': 'Internal server error'}), 500)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
