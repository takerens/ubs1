import json
import logging
# import time

from flask import request
from flask import jsonify

from routes import app

logger = logging.getLogger(__name__)

@app.route('/the-clumsy-programmer', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    # start = time.time()
    result = []
    for jsonData in data:
        correctionDict = {}
        corrections = []
        dictionary = jsonData["dictionary"]
        mistypes = jsonData["mistypes"]

        def search(error, dictionary):
            differences = 0
            for string in dictionary:
                differences = 0
                if (len(error) == len(string)):
                    for i in range(len(string)):
                        if differences >= 2:
                            break
                        if string[i] != error[i]:
                            differences += 1
                if differences == 1:
                    return string

        for mistype in mistypes:
            corrections.append(search(mistype, dictionary))
        
        correctionDict["corrections"] = corrections
        result.append(correctionDict)

    # logging.info("efficiency :{}".format(result))
    # return jsonify(result)
    # end = time.time()
    # print(end - start)
    return result
