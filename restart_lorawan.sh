#!/bin/bash
# get the last log of the 
while :

do
	{

X=$(tail -n 1 /var/log/lorawan-server/debug.log)
T=$(date +"%H:%M")
#echo $T

#print variable on a screen
echo $X

IFS=' '
ary=($X)
for key in "${!ary[@]}"; 

	do 
			if [ $key = 1 ]; then

				#echo "Time is: ${ary[$key]} as of $T"
				
				IFS=":." read -r h m s  <<<"${ary[$key]}"
				#echo $m
				IFS=":." read -r H M   <<<"$T"
				logmillis=$((h*3600 + m*60 ))
				timemillis=$((H*3600 + M*60 ))
				echo "current sec is $timemillis-$logmillis"
				dif=$(((timemillis-logmillis)/60))
				echo $dif

				if [ $dif -gt 10 ]; then
					echo "The server has been dead for A LONG TIME"
					systemctl restart lorawan-server.service
				else
					echo "All is well with lorawan-server"
				fi
				
			fi 
	done
sleep 600
	}
done

  