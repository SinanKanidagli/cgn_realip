import sys,os
sys.path.insert(0,os.getcwd())

from requests import Session
from requests.models import Response

import js2py
import base64

from .end_points import TPLinkModemURLEndPoints
from .get_data_text_content import content_data

from core.base.http_client import ModemHttpClient


class TPLinkModemHTTPClient(ModemHttpClient):
    def __init__(self,url : str, username : str, password : str) -> None:
        self.url = url
        self.username = username
        self.password = password
        self.session = Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'Referer':self.url
        }
        
    def login(self) -> Response:
        username, password = self.get_encrypted_values().values()
        
        URL = self.url + TPLinkModemURLEndPoints.LOGIN
        params = {'UserName':username,'Passwd':password,'Action':'1','LoginStatus':'0'}
        response = self.session.post(URL,params=params,headers=self.headers)
        return response
    
    def logout(self) -> Response:
        URL = self.url + TPLinkModemURLEndPoints.LOGOUT
        response = self.session.get(URL)
        return response
    
    def get_dns_info(self) -> Response:
        URL = self.url + TPLinkModemURLEndPoints.IP_INFORMATION
        
        header = self.headers
        header['Content-Type'] = "text/plain; charset=utf-8"
        
        response = self.session.post(URL,data=content_data,headers=header)
        return response
    
    def get_public_ip(self) -> str:
        lines =  self.get_dns_info().text.splitlines()
        for i in lines:
            if "externalIPAddress" in i:
                if i.split('=')[1][0] != "0":
                    return i.split("=")[1]
        return None
    
    def get_encrypted_values(self):
        URL = self.url + "/cgi/getParm"
        
        response = self.session.post(URL,headers=self.headers)
        
        ee = response.text.split('\n')[0].split('"')[1]
        nn = response.text.split('\n')[1].split('"')[1]
        
        with open('utils/js/rsa.js','r') as f:
            encryptJs = f.read()
        
        encryptJs_password = encryptJs + f"rsaEncrypt('{base64.b64encode(self.password.encode()).decode()}','{nn}','{ee}');\n"
        encryptJs_username = encryptJs + f"rsaEncrypt('{self.username}','{nn}','{ee}');"
        
        encrypted_username = js2py.eval_js(encryptJs_username)
        encrypted_password = js2py.eval_js(encryptJs_password)
        
        return {'username':encrypted_username,'password':encrypted_password}
        
    
