#!/bin/bash
for i in {1..10000}
do
   echo "Welcome $i times"
   sleep $((RANDOM%20))
   ping -c1 10.1.1.1
   #sleep ${RANDOM:0:1}
   sleep $((RANDOM%20))
   ping -c1 10.1.1.2
   sleep $((RANDOM%20))
   ping -c1 10.1.1.3
   sleep $((RANDOM%20))
   ping -c1 10.1.1.4
   sleep $((RANDOM%20))
   ping -c1 10.1.1.5
   sleep $((RANDOM%20))
   ping -c1 10.1.1.6
   sleep $((RANDOM%20))
   ping -c1 10.1.1.7
   sleep $((RANDOM%20))
   ping -c1 10.1.1.8
   sleep $((RANDOM%20))
   ping -c1 10.1.1.9
   sleep $((RANDOM%20))
   ping -c1 10.1.1.10
   sleep $((RANDOM%20))
done
