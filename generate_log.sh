#!/bin/bash
sec=$1
echo $sec

for i in {1..100}
    do echo '127.0.0.1 192.168.0.1 - [28/Feb/2013:12:00:00 +0900] "GET / HTTP/1.1" 200 777 "-" "Opera/12.0" -'
    sleep $sec
done 2>&1 > log_$sec.txt
