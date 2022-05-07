import Constants as keys
import MongoQuery as query

from web3 import Web3
import requests
import json
import re

web3 = Web3(Web3.HTTPProvider(keys.BSC_NODE_PROVIDER))

def getSourceCode(address):
    parameters = {'module': 'contract', 'action': 'getsourcecode', 'address': address}
    
    response = json.loads(requests.get(keys.url, params=parameters).text)
    
    return response['result']

def analyzeSourceCode(sourceCode):
    patterns = ['nonpayable', 'payable']
    
    modifiedCode = re.sub(patterns[0], '', sourceCode)
    
    if (re.search(patterns[1], modifiedCode) == None):
        return "Not_Payable"
    else:
        return "Payable"
    
def calculateBNBinBlock(blockID):
    totalBNB = 0
    for x in range(web3.eth.get_block_transaction_count(17594522)):
        totalBNB = totalBNB + web3.eth.get_transaction_by_block(17594522, x)['value']
    
    return totalBNB

def main():
    contractHash = "0xd2A9DeF12A9B7181227504F1E5CACceb7104C688"
    code = str(getSourceCode(contractHash))
    isPayable = analyzeSourceCode(code)
    postPayable = {'Contract_Hash': contractHash, 'payable': isPayable}
    
    blockID = 17594522
    totalBNB = calculateBNBinBlock(blockID)
    postTotalBNB = {'Block_ID': blockID, 'Total_BNB_Transacted': totalBNB}
    
    query.insertToPayable_Check(postPayable)
    query.insertToBNB_by_Block(postTotalBNB)
    
    
main()
