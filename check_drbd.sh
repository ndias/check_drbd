#!/bin/bash

# check the status of a drdb device
# version 0.1 - 2022/01/21 - Nuno.Dias@gmail.com 

OK=0
#WARNING=1
CRITICAL=2
#UNKNOWN=3

DRBDADM="/usr/sbin/drbdadm"

STATUS=$($DRBDADM status | grep -E "disk:UpToDate|peer-disk:UpToDate" | tr -d "\n" | tr -s " ")

if [ "$STATUS" = " disk:UpToDate peer-disk:UpToDate" ]; then

  echo "DRBD Status OK"
  STATUS=$OK

else
  echo "DRBD Status ERROR"
  STATUS=$CRITICAL
fi

exit $STATUS
