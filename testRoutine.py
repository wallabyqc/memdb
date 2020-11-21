########################################################################################################################################
#
# testRoutine.py - A simple python routine to perform tests cases of memDb class
#
# Author : Martin Gagne
#
# Email : martin.gagneqc@gmail.com
#
########################################################################################################################################

from memDb import memDb

# Main function


def main():
    myDb = memDb

    # Here is an example request sequence without transactions:

    myDb.put("example", "foo")

    myDb.get("example")  # returns “foo”

    myDb.delete("example")

    myDb.get("example")  # returns null

    myDb.delete("example")

    # Here is an example request sequence:

    myDb.createTransaction("abc")

    myDb.put("a", "foo", "abc")

    myDb.get("a", "abc")  # returns "foo"

    myDb.get("a")  # returns null

    myDb.createTransaction("xyz")

    myDb.put("a", "bar", "xyz")

    myDb.get("a", "xyz")  # returns "bar"

    myDb.commitTransaction("xyz")

    myDb.get("a")  # returns "bar"

    myDb.commitTransaction("abc")  # failure

    myDb.get("a")  # returns "bar"

    myDb.createTransaction("abc")

    myDb.put("a", "foo", "abc")

    myDb.get("a")  # returns "bar"

    myDb.rollbackTransaction("abc")

    myDb.put("a", "foo", "abc")  # failure

    myDb.get("a")  # returns "bar"

    myDb.createTransaction("def")

    myDb.put("b", "foo", "def")

    myDb.get("a", "def")  # returns "bar"

    myDb.get("b", "def")  # returns "foo"

    myDb.rollbackTransaction("def")

    myDb.get("b")  # returns null

    # Don't forget to look for the Ohana


# Invoke main on execution
if __name__ == "__main__":
    main()
