# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'site-packages'))

from flask import Flask, request, make_response
import json

api = Flask(__name__)

@api.route('/coyote', methods=['GET'])
def get_cards():
    cards = {
        "20": 1,
        "15": 2,
        "10": 3,
        "5": 4,
        "4": 4,
        "3": 4,
        "2": 4,
        "1": 4,
        "0": 3,
        "0 CLEAR": 1,
        "-5": 2,
        "-10": 1,
        "x2": 1,
        "MAX->0": 1,
        "?": 1,
    }
    used_cards = json.loads(request.args.get('cards', ''))

    for key in used_cards:
        cards[key] = cards[key] - used_cards[key]

    total_cards = 0
    for key in cards:
        total_cards+=cards[key]

    rate = {}
    for key in cards:
        rate[key] = cards[key] / total_cards * 100


    return make_response(rate)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8080)
