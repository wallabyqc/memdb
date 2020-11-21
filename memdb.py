
class memDb:
    # Class memDb is storing values in a dictionary with support for transactions and commits

    DataDict = dict()

    def put(key, value, transactionId=0):
        try:
            memDb.DataDict[key] = value
            return
        except:
            print("An error occured")
        

    def get(key, transactionId=0):
        try:
            return memDb.DataDict[key]
        except:
            print("An error occured")

        

    def delete(key, transactionId=0):
        try:
            del memDb.DataDict[key]
            return
        except:
            print("An error occured")

    def createTransaction(transactionId):
        try:
            #code here
            return
        except:
            print("An error occured while executing ")

    def rollbackTransaction(transactionId):
        try:
            #code here
            return
        except:
            print("An error occured")

    def commitTransaction(transactionId):
        try:
            #code here
            return
        except:
            print("An error occured")
