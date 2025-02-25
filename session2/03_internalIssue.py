import logging
logging.basicConfig(filename="internal.txt",level=logging.DEBUG)
try:
    a=int(input("Enter first integer : "))
    b=int(input("Enter second integer : "))
    print(a/b)
except (ZeroDivisionError , ValueError) as message:
    print(message)
    logging.exception(message)


