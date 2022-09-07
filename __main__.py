import re
import http.client
import urllib.request, json 
    
def main():
    listofipaddresses = {}
    with urllib.request.urlopen("https://account.protonvpn.com/api/vpn/logicals") as url:
        data = json.loads(url.read().decode())
        for element in data["LogicalServers"]:
            listofipaddresses[element['Servers'][0]['ExitIP']] = element['Name']

    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    s = str(conn.getresponse().read())
    ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', s)

    if ip[0] in listofipaddresses:
        x = listofipaddresses[ip[0]].split("#")
        print(f"{x[1]} - {listofipaddresses[ip[0]]}")
    else:
        print("Not connected to proton vpn")

if __name__ == "__main__":
    main()