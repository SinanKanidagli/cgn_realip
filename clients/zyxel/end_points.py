import sys,os

sys.path.insert(0,os.getcwd())

from core.base.end_points import EndPoints


class ZyxelModemURLEndPoints(EndPoints):
    LOGIN = '/login/login-page.cgi'
    LOGOUT = '/login/login-logout.cgi'
    IP_INFORMATION = '/pages/connectionStatus/GetDnsInfo.html'