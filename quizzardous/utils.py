import unicodedata
import re

def slugify(value):
    value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = re.sub(' ', '-', re.sub('[^\w\s-]', '', value).strip().lower())
    value = unicode(re.sub('-+', '-', value))
    # slugs should be a maximum of fifty characters long
    return value[:50]
