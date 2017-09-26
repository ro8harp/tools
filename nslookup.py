#!/usr/bin/env python

import socket

def lookup(ip):
    try:
        return socket.gethostbyaddr(ip)
    except socket.gaierror:
        return None
    except socket.error:
        return None

with open('lookup') as f:
    for ip in f.read().splitlines():
        addr = lookup(ip)
        print(addr)
