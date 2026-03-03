def is_valid_url(url):
    # Check basic conditions
    if url is None:
        return False

    url = url.strip()
    if url == "":
        return False
    if " " in url:
        return False

    # Must contain scheme://
    pos = url.find("://")
    if pos == -1:
        return False

    scheme = url[:pos]
    rest = url[pos+3:]

    if scheme not in ["http", "https", "ftp"]:
        return False
    if rest == "":
        return False

    # Hostname ends at first '/', '?', or '#'
    end = len(rest)
    slash = rest.find("/")
    qmark = rest.find("?")
    hashpos = rest.find("#")

    if slash != -1 and slash < end:
        end = slash
    if qmark != -1 and qmark < end:
        end = qmark
    if hashpos != -1 and hashpos < end:
        end = hashpos

    hostname = rest[:end]
    if hostname == "":
        return False

    # Basic hostname checks
    if hostname[0] == "." or hostname[-1] == ".":
        return False
    if ".." in hostname:
        return False
    if "." not in hostname:
        return False

    # Allowed characters (based only on what we learned)
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.~:/?#&="

    # Check hostname characters
    for ch in hostname:
        if ch not in allowed:
            return False

    # Check rest of URL (path/query/fragment)
    tail = rest[end:]
    for ch in tail:
        if ch not in allowed:
            return False

    return True

url = "https://www.google.com"
print(is_valid_url(url))