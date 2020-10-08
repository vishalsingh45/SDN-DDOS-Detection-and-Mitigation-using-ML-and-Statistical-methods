#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet, Host
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.link import TCLink
from time import sleep
import random

'''
                      s1

      h1      h2      h3     h4     h5   h6      h7      h8     h9        h10

'''

TEST_TIME = 300 #seconds
TEST_TYPE = "attack"
#normal, attack, manual

class SingleSwitchTopo(Topo):
    "Single switch connected to 10 hosts."
    def build(self):
        s1 = self.addSwitch('s1')
        h1 = self.addHost('h1', ip='10.1.1.1/24', mac="00:00:00:00:00:01", defaultRoute="via 10.1.1.10")
        h2 = self.addHost('h2', ip='10.1.1.2/24', mac="00:00:00:00:00:02", defaultRoute="via 10.1.1.10")
        h3 = self.addHost('h3', ip='10.1.1.3/24', mac="00:00:00:00:00:03", defaultRoute="via 10.1.1.10")
        h4 = self.addHost('h4', ip='10.1.1.4/24', mac="00:00:00:00:00:04", defaultRoute="via 10.1.1.10")
        h5 = self.addHost('h5', ip='10.1.1.5/24', mac="00:00:00:00:00:05", defaultRoute="via 10.1.1.10")
        h6 = self.addHost('h6', ip='10.1.1.6/24', mac="00:00:00:00:00:06", defaultRoute="via 10.1.1.10")
        h7 = self.addHost('h7', ip='10.1.1.7/24', mac="00:00:00:00:00:07", defaultRoute="via 10.1.1.10")
        h8 = self.addHost('h8', ip='10.1.1.8/24', mac="00:00:00:00:00:08", defaultRoute="via 10.1.1.10")
        h9 = self.addHost('h9', ip='10.1.1.9/24', mac="00:00:00:00:00:09", defaultRoute="via 10.1.1.10")
        h10 = self.addHost('h10', ip='10.1.1.10/24', mac="00:00:00:00:00:10", defaultRoute="via 10.1.1.10")

        self.addLink(h1, s1, cls=TCLink, bw=5)
        self.addLink(h2, s1, cls=TCLink, bw=5)
        self.addLink(h3, s1, cls=TCLink, bw=5)
        self.addLink(h4, s1, cls=TCLink, bw=5)
        self.addLink(h5, s1, cls=TCLink, bw=5)
        self.addLink(h6, s1, cls=TCLink, bw=5)
        self.addLink(h7, s1, cls=TCLink, bw=5)
        self.addLink(h8, s1, cls=TCLink, bw=5)
        self.addLink(h9, s1, cls=TCLink, bw=5)
        self.addLink(h10, s1, cls=TCLink, bw=5)

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()

    if TEST_TYPE == "normal":
        print "Generating NORMAL Traffic......."
        h1 = net.get('h1')
        cmd1 = "bash normal.sh &"
        h1.cmd(cmd1)

        h2 = net.get('h2')
        cmd1 = "bash normal.sh &"
        h2.cmd(cmd1)

        h3 = net.get('h3')
        cmd1 = "bash normal.sh &"
        h3.cmd(cmd1)

        h4 = net.get('h4')
        cmd1 = "bash normal.sh &"
        h4.cmd(cmd1)

        h5 = net.get('h5')
        cmd1 = "bash normal.sh &"
        h5.cmd(cmd1)

        h6 = net.get('h6')
        cmd1 = "bash normal.sh &"
        h6.cmd(cmd1)

        h7 = net.get('h7')
        cmd1 = "bash normal.sh &"
        h7.cmd(cmd1)

        h8 = net.get('h8')
        cmd1 = "bash normal.sh &"
        h8.cmd(cmd1)

        h9 = net.get('h9')
        cmd1 = "bash normal.sh &"
        h9.cmd(cmd1)

        h10 = net.get('h10')
        cmd1 = "bash normal.sh &"
        h10.cmd(cmd1)

        sleep(TEST_TIME)
        net.stop()
    elif TEST_TYPE == "attack":
        print "Generating ATTACK Traffic......."
        h1 = net.get('h1')
        cmd1 = "bash attack.sh &"
        h1.cmd(cmd1)

        sleep(TEST_TIME)
        net.stop()


    elif TEST_TYPE == "manual":
        CLI(net)
        net.stop()
