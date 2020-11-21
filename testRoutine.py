####################################################################
#
# Memdb - A simple python exercise of in memory DBMS simulation
#
# Author : Martin Gagne
#
# Email : martin.gagneqc@gmail.com
#
####################################################################

from memDb import memDb


def main():
    myDb = memDb

    myDb.put("example", "foo") 

    myDb.get("example")

    myDb.delete("example") 

    myDb.get("example")

    myDb.delete("example") 


if __name__ == "__main__":
    main()
