# dpdk-wget
Fork from official wget-v1.17.1, and run on the dpdk user space TCP/IP stack(ANS).

Compile:
Flowing the step to get dpdk-wget (maybe ubuntu 16.04 is the best choice,cuz ans recommend this)

1)read the original README.checkout, and  make sure the complie environment is correct, such as autoconf , automake, flex ...

2)run the ./bootstrap

3)run with ./configure with_dpdkans=yes

before make wget, do : export RTE_ANS=/home/work/dpdk-ans
4)make clean;make

5)finally, the new wget is done in src/wget


Run:
1) first should run ans , you know the new wget is based on ans, ans is the tcp-ip stack of wget, and wget use the socket and epoll from ans

2) run the new wget ,such as ./wget 10.0.0.3

Change:
1) change some confiuration and makefile to comptiable for wget-ans;

2) change the original wget-select to wget-epoll (ans not support select yet)
