import requests
from lxml import etree
from io import StringIO
import lxml.html

_HTTP = "http://"
_HTTPS = "https://"


def get_info(server):
    try:
        if requests.get(_HTTP + server, timeout=4).status_code == 200:
            protocol = 'http://'
        else:
            protocol = 'https://'

        req = requests.get(protocol + server + "/resto/get_server_info.jsp?encoding=UTF-8", timeout=4).text
        req2 = requests.get(protocol + server + "/resto/service/evoservices/testConnection.jsp", timeout=4).text
        tree = etree.parse(StringIO(req))
        tree2 = lxml.html.fromstring(req2)

        table = tree2.xpath('//tr[3]/td[3]//text()')
        crmid = ''.join([str(a) for a in table])

        name = ''.join(tree.xpath(r'//serverName/text()'))
        version = ''.join(tree.xpath(r'//version/text()'))
        compname = ''.join(tree.xpath(r'//computerName/text()'))
        status = ''.join(tree.xpath(r'//serverState/text()'))
        info = "Name: " + name + "\nVersion: " + version + "\nPC-name: " + compname + "\nStatus: " + status + "\nCRMID: " + crmid

        return info

    except Exception as e:
        return "Wrong url server"
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)
