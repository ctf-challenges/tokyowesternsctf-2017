import re
import string


def urlsanitize(s):
    goodchars = string.ascii_letters + string.digits
    goodchars += "/:."
    return "".join([c for c in s if c in goodchars])

def htmlsanitize(s):
    while True:
        m = re.match(r'.*(script).*', s, re.IGNORECASE)
        if not m:
            break
        s = s.replace(m.group(1), '')
    while True:
        m = re.match(r'.*(on.+=).*', s, re.IGNORECASE)
        if not m:
            break
        s = s.replace(m.group(1), '')
    return s
