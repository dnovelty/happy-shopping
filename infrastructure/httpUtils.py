import requests

def status_ok(resp):
    if resp.status != requests.codes.OK:
        print('Status: %u, Url: %s' % (resp.status_code, resp.url))
        return False
    return True