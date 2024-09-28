def evaluate(n):    
    # Initialize variables:
        # freeze_profit (f) - profit of the day before cooldown
        # sell_profit (f0) - profit after selling the stock
        # hold_profit (f1) - profit after buying the stock or holding onto the stock bought previously
        freeze_profit, sell_profit, hold_profit = 0, 0, -n[0]

        # Iterate through the stock prices, starting from the second day
        for current_price in n[1:]:
            # Update profits for the current day
            # freeze_profit remains as the sell_profit from the previous day
            # sell_profit is the maximum of either keeping the previous sell_profit or selling stock today (hold_profit + current_price)
            # hold_profit is the max of either keeping the stock bought previously or buying new stock after cooldown (freeze_profit - current_price)
            freeze_profit, sell_profit, hold_profit = (
                sell_profit, 
                max(sell_profit, hold_profit + current_price),
                max(hold_profit, freeze_profit - current_price)
            )

        # The maximum profit will be after all trades are done, which means no stock is being held, hence sell_profit
        return sell_profit

if __name__ == "__main__":
    print(evaluate([1,100,340,210,1,4,530]))
    print(evaluate([1,4,5,0,4]))




#     for monsters in monsterList:
#         if len(monsters["monsters"]) <= 1:
#             result.append({"efficiency": 0})
#         else:
            
#             # monsterValues = monsters["monsters"]
#             # low = monsterValues[len(monsterValues) - 1]
#             # efficiency = 0

#             # for i in range(len(monsterValues) - 2, -1, -1):
#             #     if monsterValues[i] < low:
#             #         efficiency += low
#             #         efficiency -= monsterValues[i]
#             #         low = monsterValues[i]
#             #     elif monsterValues[i] > low:
#             #         i -= 1
#             #         low = monsterValues[i]
#             #         continue
#             efficiency = 0
#             efficiencyList = []
#             track(monsters["monsters"], efficiency, 0, 'c', efficiencyList)
#             answer = max(efficiencyList)
#             if (answer < 0):
#                 answer = 0
#             result.append({"efficiency": answer})

#     # logging.info("efficiency :{}".format(result))
#     return jsonify(result)

# def track(list, value, index, task, efficiency):
#         if index == len(list):
#             efficiency.append(value)
#             return
#         elif task == 'a':
#             value += list[index]
#             track(list, value, index + 1, 'o', efficiency)
#         elif task == 'w':
#             track(list, value, index + 1, 'a', efficiency)
#             track(list, value, index + 1, 'w', efficiency)
#         elif task == 'c':
#             track(list, value - list[index], index + 1, 'a', efficiency)
#             track(list, value - list[index], index + 1, 'w', efficiency)
#         elif task == 'o':
#             track(list, value, index + 1, 'o', efficiency)
#             track(list, value, index + 1, 'c', efficiency)