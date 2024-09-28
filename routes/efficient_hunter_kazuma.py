import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)


@app.route('/efficient-hunter-kazuma', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    monsterList = data
    result = []
    for monsters in monsterList:
        if len(monsters["monsters"]) <= 1:
            result.append({"efficiency": 0})
        else:
            monsterValues = monsters["monsters"]
            low = monsterValues[0]
            efficiency = 0

            for i in range(1, len(monsterValues)):
                # if monsters[i] <= low:
                #     efficiency += high - low
                #     low = monsters[i]
                #     high = 0
            
                # if monsters[i] > high:
                #     high = monsters[i]

                # if monsters[i] < low:
                #     low = monsters[i]

                if monsterValues[i] > low:
                    efficiency -= low
                    efficiency += monsterValues[i]
                    low = monsterValues[i]
                elif monsterValues[i] < low:
                    low = monsterValues[i]
                
            result.append({"efficiency": efficiency})

    # logging.info("efficiency :{}".format(result))
    return json.dumps(result)
