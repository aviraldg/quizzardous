import unicodedata
import re
from datetime import datetime

def slugify(value):
    value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = re.sub('[^\w-]', '', re.sub(' ', '-', value.strip().lower()))
    value = unicode(re.sub('-+', '-', value))
    # slugs should be a maximum of fifty characters long
    return value[:50]

def get_current_month_datetime():
    # get the current year and month, but set the day as the first of the month
    (year, month, day) = datetime.now().timetuple()[:2] + (1,)
    return datetime(year, month, day)
