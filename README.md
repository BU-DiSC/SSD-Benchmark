# Configuration of Flexible I/O Tester
Used for Testing NVMe SSD @BU-DiSC

[1] comp -> Computational NVMe SSD

[2] nvm -> Extra Samsung NVMe SSD

[3] nvm_sat -> Extra Samsung NVMe SSD tested when space are running out (~300 GB left out of 1.92 TB)

[4] comp -> Computational NVMe SSD tested when space are running out (~500GB left out of 3.84 TB)

[5] zns_1t -> ZNS SSD with 1 TB capacity

[6] zns_4t -> ZNS SSD with 4 TB capacity


"configs" directory contains all the configs used during the test.

"results" directory contains all the results collected.

"parser directory contains prototype python script to take interested stat out of raw result files. 

File formated as "blocksize_readwritemode_threads", for example: 8k_r_5 stands for read 8k blocks using 5 threads. seq_r_2.fio stands for sequential read uisng 2 threads.