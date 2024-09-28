import json
import logging

from flask import request
from flask import jsonify

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
            
            # monsterValues = monsters["monsters"]
            # low = monsterValues[len(monsterValues) - 1]
            # efficiency = 0

            # for i in range(len(monsterValues) - 2, -1, -1):
            #     if monsterValues[i] < low:
            #         efficiency += low
            #         efficiency -= monsterValues[i]
            #         low = monsterValues[i]
            #     elif monsterValues[i] > low:
            #         i -= 1
            #         low = monsterValues[i]
            #         continue
            efficiency = 0
            efficiencyList = []
            track(monsters["monsters"], efficiency, 0, 'c', efficiencyList)
            result.append({"efficiency": max(efficiencyList)})

    # logging.info("efficiency :{}".format(result))
    return jsonify(result)

def track(list, value, index, task, efficiency):
        if index == len(list):
            efficiency.append(value)
            return
        elif task == 'a':
            value += list[index]
            track(list, value, index + 1, 'o', efficiency)
        elif task == 'w':
            track(list, value, index + 1, 'a', efficiency)
            track(list, value, index + 1, 'w', efficiency)
        elif task == 'c':
            track(list, value - list[index], index + 1, 'a', efficiency)
            track(list, value - list[index], index + 1, 'w', efficiency)
        elif task == 'o':
            track(list, value, index + 1, 'o', efficiency)
            track(list, value, index + 1, 'c', efficiency)