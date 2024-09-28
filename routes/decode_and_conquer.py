import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)


@app.route('/ub5-flags', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    result = {
  "sanityScroll": {
    "flag": "UB5{w3lc0m3_70_c7f_N0ttyB01}"
  },
  "openAiExploration": {
    "flag": "FLAG_CONTENT_HERE"
  },
  "dictionaryAttack": {
    "flag": "UB5{FLAG_CONTENT_HERE}",
    "password": "PASSWORD_HERE"
  },
  "pictureSteganography": {
    "flagOne": "UB5-1{1_am_d3f_n0t_old}",
    "flagTwo": "UB5-2{FLAG_TWO_CONTENTS_HERE}"
  },
  "reverseEngineeringTheDeal": {
    "flag": "FLAG_CONTENT_HERE",
    "key": "KEY_HERE"
  }
}

    logging.info("instructions :{}".format(result))
    return json.dumps(result)


