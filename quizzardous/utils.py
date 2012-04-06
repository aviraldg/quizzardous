import unicodedata
import re

def slugify(value):
    value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub(' ', '-', re.sub('[^\w\s-]', '', value).strip().lower()))
    return value
