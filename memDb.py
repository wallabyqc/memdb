########################################################################################################################################
#
# Class memDb, python exercise to simulate a in memory DBMS database system with transaction/commit/rollback features
#
# Author : Martin Gagne
#
# Email : martin.gagneqc@gmail.com
#
# Note : More verbose comments is intended to explain the code for the purpose of the technical exercise
#
########################################################################################################################################

from datetime import datetime


class memDb:
    # Class memDb initialization

    dataDict = dict()
    transactionMaster = dict()

    # Method to insert data into the database
    def put(key, value, transactionId=None):
        try:
            if transactionId != None:

                if transactionId in memDb.transactionMaster:
                    transactionHeader = "trx_" + str(transactionId) + ";"
                    transactionKey = transactionHeader + str(key)
                    memDb.dataDict[transactionKey] = [value, datetime.now()]
                else:
                    raise Exception("This transaction doesn't exist")

            else:
                memDb.dataDict[key] = [value, datetime.now()]

            return None

        except Exception as error:
            print("An error occured while affecting the data record: " + str(error))

    # Method to retrieve data from the database
    def get(key, transactionId=None):
        try:
            if transactionId != None:
                if transactionId in memDb.transactionMaster:
                    transactionHeader = "trx_" + str(transactionId) + ";"
                    transactionKey = transactionHeader + str(key)
                    if transactionKey in memDb.dataDict:
                        return memDb.dataDict[transactionKey][0]
                    else:
                        return memDb.dataDict[key][0]
                else:
                    raise Exception("This transaction doesn't exist")

            return memDb.dataDict[key][0]

        except Exception as error:
            print("An error occured while retrieving the data record: " + str(error))

    # Method to delete data from the database
    def delete(key, transactionId=None):
        try:
            if transactionId != None:
                if transactionId in memDb.transactionMaster:
                    transactionHeader = "trx_" + str(transactionId) + ";"
                    transactionKey = transactionHeader + str(key)
                    del memDb.dataDict[transactionKey]
                else:
                    raise Exception("This transaction doesn't exist")

            del memDb.dataDict[key]

            return None

        except Exception as error:
            print("An error occured while deleting the data record: " + str(error))

    # Method to initialize a new transaction
    def createTransaction(transactionId):
        try:
            if transactionId in memDb.transactionMaster:
                raise Exception("This transaction id is already being used")
            memDb.transactionMaster[transactionId] = datetime.now()

            return None

        except Exception as error:
            print("An error occured while creating the transaction: " + str(error))

    # Method to rollback a transaction
    def rollbackTransaction(transactionId):

        transactionHeader = "trx_" + str(transactionId) + ";"

        try:

            if transactionId in memDb.transactionMaster:

                for key in list(memDb.dataDict.keys()):

                    if transactionHeader in str(key):
                        del memDb.dataDict[key]

                del memDb.transactionMaster[transactionId]

            else:

                raise Exception("This transaction doesn't exist")

            return None

        except Exception as error:
            print("An error occured while rolling back the transaction: " + str(error))

    # Method to commit a transaction
    def commitTransaction(transactionId):

        transactionHeader = "trx_" + str(transactionId) + ";"

        try:
            if transactionId in memDb.transactionMaster:

                # Loop all transaction related records and check if current stored data was altered after transaction was started.

                for key in list(memDb.dataDict.keys()):
                    if transactionHeader in str(key):
                        originalKey = str(key).replace(transactionHeader, '')
                        if originalKey in memDb.dataDict:
                            if memDb.dataDict[originalKey][1] > memDb.transactionMaster[transactionId]:
                                raise Exception(
                                    "The transaction commit failed because one or more records was altered after transaction was initiated")

                # Loop all transaction related records and update stored data from transaction records

                for key in list(memDb.dataDict.keys()):
                    if transactionHeader in str(key):
                        originalKey = str(key).replace(transactionHeader, '')
                        memDb.dataDict[originalKey] = [
                            memDb.dataDict[key][0], datetime.now()]
                        del memDb.dataDict[key]
                del memDb.transactionMaster[transactionId]
            else:
                raise Exception(
                    "The transaction commit failed because the transaction doesn't exist")
            return None

        except Exception as error:
            print("An error occured while commiting transaction: " + str(error))
