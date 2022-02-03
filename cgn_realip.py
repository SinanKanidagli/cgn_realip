import sys
from core.base.http_client import ModemHttpClient
import netifaces
import argparse
from core.modem_clients import MODEM_CLIENTS
import requests,os,time,datetime

modems = ['select a modem\n\n']
modems += [f"[{[*MODEM_CLIENTS.keys()].index(i)}] " + i +"\n" for i in MODEM_CLIENTS.keys()] 

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Provides port forwarding for ip addresses in the cgn pool')
    parser.add_argument('-u','--username',required=True, help='username')
    parser.add_argument('-p','--password',required=True, help='password')
    parser.add_argument('--duckdns',help='enable update duckdns ip',action='store_true')
    parser.add_argument('-t','--token',help='duckdns token - You have to give the —-duckdns parameter to be able to use')
    parser.add_argument('-d','--domain',help='duckdns domain - You have to give the —-duckdns parameter to be able to use')
    
    return parser.parse_args()


def main(args: argparse.Namespace, duckdns : bool = False) -> None:
    print(*modems,sep="")
    selected_modem = input("option: ")
    try:
        selected_modem = int(selected_modem)
    except ValueError:
        print("[!] please just type a integer")
        return
    
    TOKEN = args.token if args.token else os.environ.get("DUCKDNS_TOKEN")
    DOMAIN = args.domain if args.domain else os.environ.get("DUCKDNS_DOMAIN")
    
    gateway : str = get_gateway_ip()
    
    client : ModemHttpClient = list(MODEM_CLIENTS.values())[selected_modem]
    client : ModemHttpClient = client(url='http://' + gateway,username=args.username,password=args.password)
    
    print()
    print("[?] logging in")
    
    response = client.login() 
    
    if response.status_code != 200:
        raise Exception()
    
    
    print(f"[?] fetching ip address")
    
    ip_addr = client.get_public_ip()
    
    if ip_addr == None:
        raise Exception()
    
    
    print(f"[+] ip addr: ({ip_addr})")
    
    TIME_INTERVAL : int = 5
    
    if duckdns:
        print(f"[?] updating duckdns ({TIME_INTERVAL} minutes)")
        print()
        while True:
            
            time_now = datetime.datetime.now().strftime("[%m-%d-%Y %H:%M:%S]\t")
            
            response_ddns = duckdns_update(args.domain,args.token,ip_addr)
            
            print(time_now + response_ddns)
            
            time.sleep(TIME_INTERVAL * 60)
    return

def get_gateway_ip() -> str :
    gateways = netifaces.gateways()
    default_gateway = gateways['default'][netifaces.AF_INET][0]
    return default_gateway

def duckdns_update(domain, token, ip, verbose=False):
    params = {
        "domains": domain if domain else os.environ.get("DUCKDNS_DOMAINS"),
        "token": token if token else os.environ.get("DUCKDNS_TOKEN"),
        "ip": ip,
        "verbose": verbose
    }
    r = requests.get("https://www.duckdns.org/update", params)
    return r.text.strip().replace('\n', ' ')

if __name__ == '__main__':
    args = get_args()
    if args.duckdns:
        if not args.token:
            if not os.environ.get("DUCKDNS_TOKEN"):
                raise Exception("please provide a token")
        elif not args.domain:
            if not os.environ.get("DUCKDNS_DOMAIN"):
                raise Exception("please provide a domain")
        main(args,duckdns=True)
        
    main(args)
        
    
