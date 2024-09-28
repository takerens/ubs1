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
            monstersArray = monsters["monsters"]
            # State: charging or attacking
            # if charge: i + 1
            # if attack: i + 2
            dp = {} # key = (i, charging) val = max_profit

            def dfs(index, charging):
                if index >= len(monstersArray):
                    return 0
                if (index, charging) in dp:
                    return dp[(index, charging)]
                
                if charging:
                    charge = dfs(index + 1, not charging) - monstersArray[index]
                    rest = dfs(index + 1, charging)
                    dp[(index, charging)] = max(charge, rest)
                else:
                    attack = dfs(index + 2, not charging) + monstersArray[index]
                    rest = dfs(index + 1, charging)
                    dp[(index, charging)] = max(attack, rest)
                return dp[(index, charging)]
            result.append({"efficiency": dfs(0, True)})

    # logging.info("efficiency :{}".format(result))
    return jsonify(result)