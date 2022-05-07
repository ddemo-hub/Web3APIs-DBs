import requests
import json

import PG
import Constants

def min15_to_hour1(candles):
    beginIndex = 0
    endIndex = 3
    
    mergedData = [[0 for i in range(5)] for j in range((int(len(candles) / 4)))]
    mergedIndex = 0
    
    while endIndex <= (len(candles) - 1):
        mergedData[mergedIndex][0] = candles[beginIndex][0]
        mergedData[mergedIndex][1] = candles[beginIndex][1]
        mergedData[mergedIndex][2] = max(candles[beginIndex][2], candles[beginIndex+1][2], candles[beginIndex+2][2], candles[beginIndex+3][2])
        mergedData[mergedIndex][3] = min(candles[beginIndex][3], candles[beginIndex+1][3], candles[beginIndex+2][3], candles[beginIndex+3][3])
        mergedData[mergedIndex][4] = candles[endIndex][4]

        mergedIndex = mergedIndex + 1
        beginIndex = beginIndex + 4
        endIndex = endIndex + 4

    return mergedData
         

def get_dataframe(symbol, interval):
    parameters = {'symbol': symbol, 'interval': interval}    
    
    frame = json.loads(requests.get(Constants.url, params= parameters).text)
    
    return frame    

    
def main():
    symbol = "ETHUSDT"
    interval = "15m"

    data = get_dataframe(symbol, interval)
    PG.insertData(data, "min_15")
    
    mergedData = min15_to_hour1(data)
    PG.insertData(mergedData, "hour_1")
    


main()

if(PG.connection):
    PG.cursor.close()
    PG.connection.close()
    print("Disconnected from PostgreSQL Server")
