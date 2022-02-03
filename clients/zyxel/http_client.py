import sys,os
sys.path.insert(0,os.getcwd())

from requests import Session
from requests.models import Response

from .end_points import ZyxelModemURLEndPoints

from core.base.http_client import ModemHttpClient


class ZyxelModemHTTPClient(ModemHttpClient):
    def __init__(self,url : str, username : str, password : str) -> None:
        self.url = url
        self.session = Session()
        
    def login(self) -> Response:
        URL = self.url + ZyxelModemURLEndPoints.LOGIN
        params = {'AuthName':'admin','AuthPassword':'ttnet'}
        response = self.session.post(URL,params)
        return response
    
    def logout(self) -> Response:
        URL = self.url + ZyxelModemURLEndPoints.LOGOUT
        response = self.session.get(URL)
        return response
    
    def get_dns_info(self) -> Response:
        URL = self.url + ZyxelModemURLEndPoints.IP_INFORMATION
        response = self.session.post(URL)
        return response
    
    def get_public_ip(self) -> str:
        return self.get_dns_info().text.split('|')[6]
    
