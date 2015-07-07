#!/bin/bash

cat dnsmasq.log | ./dnsmasq_filter -ru http://dmr.local/dns/message -bs 2

