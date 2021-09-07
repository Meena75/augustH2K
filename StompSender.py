import stomp

host = "localhost"
port = 61613
dest = "/queue/SEDAP.MANUAL.CHECK"
conn = stomp.Connection(host_and_ports = [(host, port)])
conn.connect()
data = "Meenakshi sending 1st message of the day {}"
for i in range(1, 10):
    conn.send(destination=dest, body=data.format(i), persistent='true')
print("Done!")
conn.disconnect()