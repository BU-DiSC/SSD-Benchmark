#!/bin/sh
rm -f out.txt

a=1
a_max=10

while [ $a -le $a_max ]
do
	fio --name=randread1 --filename=testfile --ioengine=libaio --iodepth=1 --rw=randread --bs=4k --direct=1 --numjobs=$a --runtime=300 --group_reporting >> out_r4.txt
   	a=`expr $a + 1`
done

sleep 10

a=1
a_max=10

while [ $a -le $a_max ]
do
	fio --name=randread2 --filename=testfile --ioengine=libaio --iodepth=1 --rw=randread --bs=8k --direct=1 --numjobs=$a --runtime=300 --group_reporting >> out_r8.txt
   	a=`expr $a + 1`
done

sleep 10

a=1
a_max=10

while [ $a -le $a_max ]
do
	fio --name=randwrite1 --filename=testfile --ioengine=libaio --iodepth=1 --rw=randwrite --bs=4k --direct=1 --numjobs=$a --runtime=300 --group_reporting >> out_w4.txt
   	a=`expr $a + 1`
done

sleep 10

a=1
a_max=10

while [ $a -le $a_max ]
do
	fio --name=randwrite2 --filename=testfile --ioengine=libaio --iodepth=1 --rw=randwrite --bs=4k --direct=1 --numjobs=$a --runtime=300 --group_reporting >> out_w8.txt
   	a=`expr $a + 1`
done