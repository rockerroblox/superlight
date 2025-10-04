import socket
import os
import threading
import socketserver
from dnspython import dns


IMPERO_TARGET_PORTS = [55282, 30016, 64001, 50142]
LIGHTSPEED_TARGET_PORTS = [3455, 3456, 6544, 62312, 49669, 56909, 59172, 59173, 59174]
ALL_PORTS = [55282, 30016, 64001, 50142, 3455, 3456, 6544, 62312, 49669, 56909, 59172, 59173, 59174]

BLOCKLIST = [
    
                    "lsrelay-extensions-production.s3.amazonaws.com"
                    "devices.filter.relay.school"
                    "production-gc.lsfilter.com"
                    "lightspeedsystems.app",
                    "stagingls.io",
                    "developmentls.io",
                    "lsrelayaccess.com",
                    "lsurl.me",
                    "lsmdm-production.s3.amazonaws.com",
                    "devices.lsclassroom.com",
                    "lsorchestration-production.amazonaws.com",
                    "lsaccess.me",
                    "login.i-ready.com",
                    "gm4nyg31l2.execute-api.us-west-2.amazonaws.com",
                    "5rw61tcrl5.execute-api.us-west-2.amazonaws.com",
                    "wsmfcvajyf.execute-api.us-west-1.amazonaws.com",
                    "development.lsclassroom.com",
                    "staging-preview.lsclassroom.com",
                    "preview.lsclassroom.com",
                    "hosted186.renlearn.com",
                    "z40.renlearn.com",
                    "z40.renlearnrp.com",
                    "z46.renlearn.com",
                    "z46.renlearnrp.com",
                    "hosted298.renlearn.com",
                    "realtime.ably.io",
                    "z05.renlearn.com",
                    "z05.renlearnrp.com",
                    "hosted88.renlearn.com",
                    "gce-beacons.gcp.gvt2.com",
                    "gce-beacons.gcp.gvt3.com",
                    "lightspeed-realtime.ably.io",
                    "a-fallback-lightspeed.ably.io",
                    "b-fallback-lightspeed.ably.io",
                    "c-fallback-lightspeed.ably.io",
                    "staging-bp-01.lsfilter.com"
]
class WebSocket:
    def occupy(port, host='localhost'):
        try:
            blocker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            blocker.bind((host, port))
            blocker.listen(1)
            print(f"Occupied port {port}")
            while True:
                conn, addr = blocker.accept()
                conn.close()
        except Exception as e:
            print(f"Failed to occupy port {port}: {e}")

for port in ALL_PORTS:
    thread = threading.Thread(target=WebSocket.occupy, args=(port,))
    thread.daemon = True
    thread.start()


class WebBlock(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0]
        socket = self.request[1]

        try:
            request = dns.message.from_wire(data)
            question = request.question[0]
            qname = question.name.to_text()

            if self.should_block(qname):
                # return NXDOMAIN
                response = dns.message.make_response(request)
                response.set_rcode(dns.rcode.NXDOMAIN)
                socket.send(response.to_wire(), self.client_address)
        except Exception as e:
            print(f"Error handling query: {e}")
    
    def should_block(self, domain):
        domain = domain.lower().rstrip('.')
        for blocked_domain in BLOCKLIST:
            if domain == blocked_domain or domain.endswith('.' + blocked_domain):
                return True
        return False

HOST, PORT = "127.0.0.1", 5353
server = socketserver.UDPSerer((HOST, PORT), WebBlock)
print(f"Running")
server.serve_forever()
