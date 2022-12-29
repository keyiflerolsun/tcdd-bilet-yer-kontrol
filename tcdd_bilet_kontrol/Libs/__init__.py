# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from ..Libs.TCDD_Selenium import TCDD
from notifypy             import Notify
from os                   import name as sistem
from pathlib              import Path

def bildirim(baslik:str, icerik:str):

    # calisma_dizini = Path(__file__).parent.resolve()

    calisma_dizini = Path(__file__).parents[1]
    ayrac          = "/" if sistem != "nt" else "\\"
    logo_yolu      = f"{calisma_dizini}{ayrac}Assets{ayrac}Logo.png"

    _bildirim = Notify()
    _bildirim._notification_application_name = "TCDD | @KekikAkademi"
    _bildirim._notification_icon             = logo_yolu

    if sistem == "nt":
        _bildirim.icon = logo_yolu

    _bildirim.title   = baslik
    _bildirim.message = icerik

    _bildirim.send(block=False)