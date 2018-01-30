# python-webocket-and-hex-converter
it is two files one for concerting large hex number to decimal
ws.py is a socketclient for getting mote data from lorawan-server.
go to https://github.com/gotthardp/lorawan-server/blob/stable/doc/WebSockets.md to see how line 4 of web.py file should be configured
convert.py shows how to reverswe the hex data required by the downlink fuhn expression for it to be passed to the mote. This is useful when
dealing with large hex data like a water meter
