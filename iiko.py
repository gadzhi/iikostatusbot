import requests
from lxml import etree
from io import StringIO
import lxml.html


def get_info(server):
    try:
        req = requests.get('https://' + server + "/resto/get_server_info.jsp?encoding=UTF-8").text
        req2 = requests.get('https://' + server + "/resto/service/evoservices/testConnection.jsp").text
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







