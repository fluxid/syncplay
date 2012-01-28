#coding:utf8

import sys

from twisted.internet import reactor

from syncplay import client
from syncplay.players import mplayer

if __name__ == '__main__':
    args = sys.argv[1:]
    host = args.pop(0)
    name = args.pop(0)
    if ':' in host:
        host, port = host.split(':', 1)
        port = int(port)
    else:
        port = 8999

    args.append('-slave')
    args.append('-quiet')

    manager = client.Manager(host, port, name)
    manager.start()
    mplayer.run_mplayer(manager, 'mplayer', args)
    reactor.run()
