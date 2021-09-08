import time

import stomp

host= "localhost"
port= 61613
dest = "/queue/SEDAP.MANUAL.CHECK"


class SEDAPStompReceive:

    def __init__(self,conn):
        self.Connection = conn
        self.count=0

    def on_error(self,message):
        print("Received an error {}".format(message))

    def on_message(self, message):
        print(message.body)
        print(message.headers.get('message-id'))

conn = stomp.Connection(host_and_ports = [(host, port)])
listener = SEDAPStompReceive(conn)
conn.connect()
conn.set_listener('MeenaListener', listener)
conn.subscribe(destination=dest, id=1, ack='auto')
print("Done!")
print("Waiting for messages...")
while 1:
    time.sleep(10)