#reset before write
cd 1t
# blkzone reset /dev/nvme2n2
# fio seq_w_1.fio --output=/usr/local/bench/zns_1t/seq_w_1.txt
# blkzone reset /dev/nvme2n2
# fio seq_w_2.fio --output=/usr/local/bench/zns_1t/seq_w_2.txt
# blkzone reset /dev/nvme2n2
# fio seq_w_3.fio --output=/usr/local/bench/zns_1t/seq_w_3.txt
# blkzone reset /dev/nvme2n2
# fio seq_w_4.fio --output=/usr/local/bench/zns_1t/seq_w_4.txt
# blkzone reset /dev/nvme2n2
# fio seq_w_5.fio --output=/usr/local/bench/zns_1t/seq_w_5.txt
# blkzone reset /dev/nvme2n2
# fio seq_w_6.fio --output=/usr/local/bench/zns_1t/seq_w_6.txt
# blkzone reset /dev/nvme2n2
# fio seq_w_7.fio --output=/usr/local/bench/zns_1t/seq_w_7.txt
# blkzone reset /dev/nvme2n2
# fio seq_w_8.fio --output=/usr/local/bench/zns_1t/seq_w_8.txt
# blkzone reset /dev/nvme2n2
# fio seq_w_9.fio --output=/usr/local/bench/zns_1t/seq_w_9.txt
# blkzone reset /dev/nvme2n2
# fio seq_w_10.fio --output=/usr/local/bench/zns_1t/seq_w_10.txt
# blkzone reset /dev/nvme2n2
# fio rand_w_1.fio --output=/usr/local/bench/zns_1t/rand_w_1.txt
# blkzone reset /dev/nvme2n2
# fio rand_w_2.fio --output=/usr/local/bench/zns_1t/rand_w_2.txt
# blkzone reset /dev/nvme2n2
# fio rand_w_3.fio --output=/usr/local/bench/zns_1t/rand_w_3.txt
# blkzone reset /dev/nvme2n2
# fio rand_w_4.fio --output=/usr/local/bench/zns_1t/rand_w_4.txt
# blkzone reset /dev/nvme2n2
# fio rand_w_5.fio --output=/usr/local/bench/zns_1t/rand_w_5.txt
# blkzone reset /dev/nvme2n2
# fio rand_w_6.fio --output=/usr/local/bench/zns_1t/rand_w_6.txt
# blkzone reset /dev/nvme2n2
# fio rand_w_7.fio --output=/usr/local/bench/zns_1t/rand_w_7.txt
# blkzone reset /dev/nvme2n2
# fio rand_w_8.fio --output=/usr/local/bench/zns_1t/rand_w_8.txt
# blkzone reset /dev/nvme2n2
# fio rand_w_9.fio --output=/usr/local/bench/zns_1t/rand_w_9.txt
# blkzone reset /dev/nvme2n2
# fio rand_w_10.fio --output=/usr/local/bench/zns_1t/rand_w_10.txt
# blkzone reset /dev/nvme2n2
##write prepare before each test
# fio write_prepare.fio
# fio seq_r_1.fio --output=/usr/local/bench/zns_1t/seq_r_1.txt
# blkzone reset /dev/nvme2n2
# fio write_prepare.fio
# fio seq_r_2.fio --output=/usr/local/bench/zns_1t/seq_r_2.txt
# blkzone reset /dev/nvme2n2
# fio write_prepare.fio
# fio seq_r_3.fio --output=/usr/local/bench/zns_1t/seq_r_3.txt
# blkzone reset /dev/nvme2n2
# fio write_prepare.fio
# fio seq_r_4.fio --output=/usr/local/bench/zns_1t/seq_r_4.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio seq_r_5.fio --output=/usr/local/bench/zns_1t/seq_r_5.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio seq_r_6.fio --output=/usr/local/bench/zns_1t/seq_r_6.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio seq_r_7.fio --output=/usr/local/bench/zns_1t/seq_r_7.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio seq_r_8.fio --output=/usr/local/bench/zns_1t/seq_r_8.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio seq_r_9.fio --output=/usr/local/bench/zns_1t/seq_r_9.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio seq_r_10.fio --output=/usr/local/bench/zns_1t/seq_r_10.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio rand_r_1.fio --output=/usr/local/bench/zns_1t/rand_r_1.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio rand_r_2.fio --output=/usr/local/bench/zns_1t/rand_r_2.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio rand_r_3.fio --output=/usr/local/bench/zns_1t/rand_r_3.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio rand_r_4.fio --output=/usr/local/bench/zns_1t/rand_r_4.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio rand_r_5.fio --output=/usr/local/bench/zns_1t/rand_r_5.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio rand_r_6.fio --output=/usr/local/bench/zns_1t/rand_r_6.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio rand_r_7.fio --output=/usr/local/bench/zns_1t/rand_r_7.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio rand_r_8.fio --output=/usr/local/bench/zns_1t/rand_r_8.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio rand_r_9.fio --output=/usr/local/bench/zns_1t/rand_r_9.txt
blkzone reset /dev/nvme2n2
fio write_prepare.fio
fio rand_r_10.fio --output=/usr/local/bench/zns_1t/rand_r_10.txt
blkzone reset /dev/nvme2n2
cd ../4t
#reset before write
blkzone reset /dev/nvme3n2
fio seq_w_1.fio --output=/usr/local/bench/zns_4t/seq_w_1.txt
blkzone reset /dev/nvme3n2
fio seq_w_2.fio --output=/usr/local/bench/zns_4t/seq_w_2.txt
blkzone reset /dev/nvme3n2
fio seq_w_3.fio --output=/usr/local/bench/zns_4t/seq_w_3.txt
blkzone reset /dev/nvme3n2
fio seq_w_4.fio --output=/usr/local/bench/zns_4t/seq_w_4.txt
blkzone reset /dev/nvme3n2
fio seq_w_5.fio --output=/usr/local/bench/zns_4t/seq_w_5.txt
blkzone reset /dev/nvme3n2
fio seq_w_6.fio --output=/usr/local/bench/zns_4t/seq_w_6.txt
blkzone reset /dev/nvme3n2
fio seq_w_7.fio --output=/usr/local/bench/zns_4t/seq_w_7.txt
blkzone reset /dev/nvme3n2
fio seq_w_8.fio --output=/usr/local/bench/zns_4t/seq_w_8.txt
blkzone reset /dev/nvme3n2
fio seq_w_9.fio --output=/usr/local/bench/zns_4t/seq_w_9.txt
blkzone reset /dev/nvme3n2
fio seq_w_10.fio --output=/usr/local/bench/zns_4t/seq_w_10.txt
blkzone reset /dev/nvme3n2
fio rand_w_1.fio --output=/usr/local/bench/zns_4t/rand_w_1.txt
blkzone reset /dev/nvme3n2
fio rand_w_2.fio --output=/usr/local/bench/zns_4t/rand_w_2.txt
blkzone reset /dev/nvme3n2
fio rand_w_3.fio --output=/usr/local/bench/zns_4t/rand_w_3.txt
blkzone reset /dev/nvme3n2
fio rand_w_4.fio --output=/usr/local/bench/zns_4t/rand_w_4.txt
blkzone reset /dev/nvme3n2
fio rand_w_5.fio --output=/usr/local/bench/zns_4t/rand_w_5.txt
blkzone reset /dev/nvme3n2
fio rand_w_6.fio --output=/usr/local/bench/zns_4t/rand_w_6.txt
blkzone reset /dev/nvme3n2
fio rand_w_7.fio --output=/usr/local/bench/zns_4t/rand_w_7.txt
blkzone reset /dev/nvme3n2
fio rand_w_8.fio --output=/usr/local/bench/zns_4t/rand_w_8.txt
blkzone reset /dev/nvme3n2
fio rand_w_9.fio --output=/usr/local/bench/zns_4t/rand_w_9.txt
blkzone reset /dev/nvme3n2
fio rand_w_10.fio --output=/usr/local/bench/zns_4t/rand_w_10.txt
blkzone reset /dev/nvme3n2
#write prepare before each test
fio write_prepare.fio
fio seq_r_1.fio --output=/usr/local/bench/zns_4t/seq_r_1.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio seq_r_2.fio --output=/usr/local/bench/zns_4t/seq_r_2.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio seq_r_3.fio --output=/usr/local/bench/zns_4t/seq_r_3.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio seq_r_4.fio --output=/usr/local/bench/zns_4t/seq_r_4.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio seq_r_5.fio --output=/usr/local/bench/zns_4t/seq_r_5.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio seq_r_6.fio --output=/usr/local/bench/zns_4t/seq_r_6.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio seq_r_7.fio --output=/usr/local/bench/zns_4t/seq_r_7.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio seq_r_8.fio --output=/usr/local/bench/zns_4t/seq_r_8.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio seq_r_9.fio --output=/usr/local/bench/zns_4t/seq_r_9.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio seq_r_10.fio --output=/usr/local/bench/zns_4t/seq_r_10.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio rand_r_1.fio --output=/usr/local/bench/zns_4t/rand_r_1.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio rand_r_2.fio --output=/usr/local/bench/zns_4t/rand_r_2.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio rand_r_3.fio --output=/usr/local/bench/zns_4t/rand_r_3.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio rand_r_4.fio --output=/usr/local/bench/zns_4t/rand_r_4.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio rand_r_5.fio --output=/usr/local/bench/zns_4t/rand_r_5.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio rand_r_6.fio --output=/usr/local/bench/zns_4t/rand_r_6.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio rand_r_7.fio --output=/usr/local/bench/zns_4t/rand_r_7.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio rand_r_8.fio --output=/usr/local/bench/zns_4t/rand_r_8.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio rand_r_9.fio --output=/usr/local/bench/zns_4t/rand_r_9.txt
blkzone reset /dev/nvme3n2
fio write_prepare.fio
fio rand_r_10.fio --output=/usr/local/bench/zns_4t/rand_r_10.txt
blkzone reset /dev/nvme3n2
