
# Realiza un programa que muestre la fecha actual, y la fecha de mañana

from datetime import *
from dateutil.relativedelta import *

now = datetime.now()
print(now)
now = now + relativedelta(months=1, weeks=1, hour=10)
print(now)
