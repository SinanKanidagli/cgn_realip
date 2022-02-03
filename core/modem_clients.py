from clients.zyxel.http_client import ZyxelModemHTTPClient
from clients.tp_link.TD_W9970.http_client import TPLinkModemHTTPClient

MODEM_CLIENTS : dict = {
    'ZYXEL[not usable]':ZyxelModemHTTPClient,
    'TP_LINK_TD-W9970':TPLinkModemHTTPClient,
}