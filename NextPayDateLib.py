
import datetime
from dateutil import relativedelta

CUR_DATE = datetime.datetime.now()

NextPay = CUR_DATE + relativedelta.relativedelta(months=1, day=1) #stackoverflow.com - I love this library, it's so cool


#-----------------------

import datetime
CUR_DATE = datetime.datetime.now()
while True:

    def NextPayment(CURDATE):
        #calculate payment date as the first of the next month
        CurYear = CURDATE.year
        CurMonth = CURDATE.month
        CurDay = CURDATE.day

        if CurDay >= 25:
            CurMonth += 1

        if CurMonth == 12:
            PayDate = datetime.datetime(CurYear + 1, 1, 1)
        else:
            PayDate = datetime.datetime(CurYear, CurMonth + 1, 1)

        return PayDate
    break
PayDate = NextPayment(CUR_DATE)

print(PayDate)

# -------------------------

import re

def PNumS(PhoneStr):
    digits = re.sub(r'\D', '', PhoneStr)

    if len(digits) != 10:
        return "Invalid Phone Number"
    
    PhoneFormat = f'{digits[0:3]}-{digits[3:6]}-{digits[6:]}'
    return PhoneFormat
