import sys,os

sys.path.insert(0,os.getcwd())

from core.base.end_points import EndPoints


class TPLinkModemURLEndPoints(EndPoints):
    LOGIN = '/cgi/login'
    LOGOUT = '/login/login-logout.cgi'
    IP_INFORMATION = '/cgi?1&1&1&1&5&5&5&5&5&5&5&5&5&5&5'