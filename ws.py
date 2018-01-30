from websocket import create_connection
import json

ws = create_connection("ws://192.168.3.35:8080/ws/groups/websoc/json")
x = 14
while True:
	print "Receiving..."
	result =  ws.recv()
	result = json.loads(result)
	print "Received '%s'" % result

	devaddr = result['devaddr']

	if devaddr == '15000014':
		print "devaddr:" + devaddr
		
		data = {"fields":{"data":[254, 254, 254, 254, 104, 16, 34, 16, 38, 135, 0, 17, 17, 4, 4, 23, 160, 1, 153, 1, 22, 0, 0],"port":"2"}}
		print data
		
		ws.send(
			json.dumps(data)
			)
	if devaddr == '57A9926D':
		print "devaddr:" + devaddr
		
		data = {"fields":{"data":[x],"port":"2"}}
		print data
		
		ws.send(
			json.dumps(data)
			)
ws.close()