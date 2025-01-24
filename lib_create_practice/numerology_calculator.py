import magicnumber as mn
import datetime as dt
import time

yourdate = input('Please enter the desired birth date to calculate a life path number.')
conv_date = dt.date(int(yourdate[4:]),int(yourdate[2:4]),int(yourdate[:2]))
yd = int(yourdate)
result = mn.lifepath(yd)
print('Congratulations, the life path number for' + conv_date.strftime(" %A %d. %B %Y ") + f'is {result}!')

choice = input('Do you wish to learn more about this life path number? Enter Y/N')
if choice == 'Y':
    pass
if choice == 'N':
    print('Thank you for using numerology calculator!')
    time.sleep(3)
exit()  # optional: add rerun (with choice) to calculate more numbers

# step by step requirements to complete this program:

# magicnumber: calculate addition by DD MM and YYYY separately before adding all together
# magicnumber: return only single digit result, UNLESS 11 or 22 in final addition

# calculator: handle input regardless of convention, i.e. year first or last, 2 or 4 digit, DD-MM or MM-DD
# calculator: treat . / - the same for determining DD MM and YYYY
# calculator: direct to website with more info based on userinput Y/N -- find appropriate package to install

# DONE print result from magicnumber in calculator
# DONE calculator: if magicnumber ran successfully : print Congrats & ask if they want to learn more