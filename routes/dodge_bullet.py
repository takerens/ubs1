import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)


@app.route('/dodge', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    rowVal = 0
    colVal = 0
    for row in data:
        for col in row:
            if data[row][col] == '*':
                rowVal = row
                colVal = col
    up = colVal - 1
    down = colVal + 1
    left = rowVal - 1
    right = rowVal + 1
    check(data, data[row][col], up, down, left, right)

    logging.info("instructions :{}".format(result))
    return json.dumps(result)

def check(data, positions, up, down, left, right):
    if 


def preCheck(pre, node):
