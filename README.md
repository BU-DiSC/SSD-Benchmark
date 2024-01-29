# Configuration of Flexible I/O Tester
Used for Testing NVMe SSD @BU-DiSC

1. `comp` -> Computational NVMe SSD
2. `nvm` -> Extra Samsung NVMe SSD
3. `nvm_sat` -> Extra Samsung NVMe SSD tested when space are running out (~300 GB left out of 1.92 TB)
4. `nvm_legacy` -> Extra Samsung NVMe SSD tested when space are running out with legacy config.
5. `comp_sat` -> Computational NVMe SSD tested when space are running out (~500 GB left out of 3.84 TB)
6. `comp_legacy` -> COmputational NVMe SSD tested when space are running out with legacy config.
7. `zns_1t` -> ZNS SSD with 1 TB capacity
8. `zns_4t` -> ZNS SSD with 4 TB capacity
9. `optane` -> Intel Optane P4800X with 375 GB capacity. Tested when space are running out (~50 GB left out of 375 GB)
10. `optane_legacy` -> Intel Optane P4800X tested when space are running out with legacy config.
11. `p4510` -> Intel DC P4510 with 1 TB capacity. Tested when space are running out (~60 GB left out of 1 TB)
12. `p4510_legacy` -> Intel DC P4510 tested when space are running out with legacy config.



`configs` directory contains all the configs used during the test.

`results` directory contains all the results collected.

`parser` directory contains simple python script to take interested stats out of raw result files. 

`legacy_configs` directory contains configuration and script previously used in the Damon paper.

File formated as `blocksize_readwritemode_threads`, for example: 8k_r_5 stands for read 8k blocks using 5 threads, and seq_r_2 stands for sequential read uisng 2 threads.