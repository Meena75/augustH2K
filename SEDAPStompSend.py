import stomp

host =  "localhost"
port=  61613
dest = "/queue/SEDAP.MANUAL.CHECK"
conn = stomp.Connection(host_and_ports=[(host,port)])
conn.connect()
data="{}"
path = "C:/Users/sarav/OneDrive/Desktop/SEDAP/tempdir/Customer_CorrectWatchTime.csv"
file = open(path)

conn.send(destination=dest, body = data.format(file.read()), persistant = 'true')
print("Done")
conn.disconnect()