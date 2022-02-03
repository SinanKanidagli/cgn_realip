# cgn_realip

## Provides port forwarding for ip addresses in the cgn pool

CGN is a network address translator. With IPv4, the ip address is exhausted. That's why internet service providers switched to the CGN system. [What is CGN?](https://en.wikipedia.org/wiki/Carrier-grade_NAT)

Due to CGN, internet slowness, not being able to open ports and privacy problems emerged. This tool, on the other hand, accesses the web interface of the modem, sends the real ip address to a DDNS service and makes port forwarding available.

Using ssh or telnet could be simpler, but most internet service providers require root privileges for ssh or telnet access on modems. That's why I parse the data on the modem's web page and access the real IP.

It can be used for 2 modem models at the moment. For more, you can PR and support. Use the abstract classes I created for new clients

|Flag                 |Description                          
|---------------------|-------------------------------
|`-h` `--help`.       | show help text             
|`-u` `--username`    | modem username
|`-p` `--password`    | modem password
|`--duckdns`          | enable update duck dns
|`-t` `--token`       | duckdns token          
|`-d` `--domain`      | duckdns domain     


## Example usage

    $ python3 cgn_realip.py -u admin -p admin --duckdns -d mydomainname -t cbb9abcf-5a3f-4b67-98f3-c1e878b05b56

    select a modem

    [0] ZYXEL
    [1] TP_LINK_TD-W9970

    option: 1

    [?] logging in
    [?] fetching ip address
    [+] ip addr: (10.82.94.231)
    [?] updating duckdns
    [02-03-2022 17:59:24]	OK 10.82.94.231  UPDATED
    [02-03-2022 18:04:24]	OK 10.82.94.231  NOCHANGE

## CLI

    $ python3 cgn_realip.py -h
    usage: cgn_realip.py [-h] -u USERNAME -p PASSWORD [--duckdns] [-t TOKEN]
                        [-d DOMAIN]

    Provides port forwarding for ip addresses in the cgn pool

    optional arguments:
    -h, --help            show this help message and exit
    -u USERNAME, --username USERNAME
                            username
    -p PASSWORD, --password PASSWORD
                            password
    --duckdns             enable update duckdns ip
    -t TOKEN, --token TOKEN
                            duckdns token - You have to give the —-duckdns parameter to
                            be able to use
    -d DOMAIN, --domain DOMAIN
                            duckdns domain - You have to give the —-duckdns parameter
                            to be able to use

    




