from datetime import datetime

str_date = '11/07/2018'

date = datetime.strptime(str_date, '%d/%m/%Y').date()

print(date)

# Python3 code to demonstrate working of
# Validate String date format
# Using dateutil.parser.parse

# from dateutil import parser
 
# # initializing string
# test_str = '30/01/1997'
 
# # printing original string
# print("The original string is : " + str(test_str))
 
# # initializing format
# format = "%d-%m-%Y"
 
# # checking if format matches the date
# res = True
 
# # using try-except to check for truth value
# try:
#     res = bool(parser.parse(test_str))
# except ValueError:
#     res = False
 
# # printing result
# print("Does date match format? : " + str(res))
