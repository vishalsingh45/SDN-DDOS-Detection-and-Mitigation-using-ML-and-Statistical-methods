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

      h1   h2   h3  h4   h5  h6  h7  h8  h9 h10  h11 h12  h13  h14  h15  h16  h17  h18 h19  h20  h21  h22  h23  h24  h25

'''

TEST_TIME = 300 #seconds
TEST_TYPE = "manual"
#normal, attack, manual

class SingleSwitchTopo(Topo):
    "Single switch connected to 25 hosts."
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
        h11 = self.addHost('h11', ip='10.1.1.11/24', mac="00:00:00:00:00:11", defaultRoute="via 10.1.1.10")
        h12 = self.addHost('h12', ip='10.1.1.12/24', mac="00:00:00:00:00:12", defaultRoute="via 10.1.1.10")
        h13 = self.addHost('h13', ip='10.1.1.13/24', mac="00:00:00:00:00:13", defaultRoute="via 10.1.1.10")
        h14 = self.addHost('h14', ip='10.1.1.14/24', mac="00:00:00:00:00:14", defaultRoute="via 10.1.1.10")
        h15 = self.addHost('h15', ip='10.1.1.15/24', mac="00:00:00:00:00:15", defaultRoute="via 10.1.1.10")
        h16 = self.addHost('h16', ip='10.1.1.16/24', mac="00:00:00:00:00:16", defaultRoute="via 10.1.1.10")
        h17 = self.addHost('h17', ip='10.1.1.17/24', mac="00:00:00:00:00:17", defaultRoute="via 10.1.1.10")
        h18 = self.addHost('h18', ip='10.1.1.18/24', mac="00:00:00:00:00:18", defaultRoute="via 10.1.1.10")
        h19 = self.addHost('h19', ip='10.1.1.19/24', mac="00:00:00:00:00:19", defaultRoute="via 10.1.1.10")
        h20 = self.addHost('h20', ip='10.1.1.20/24', mac="00:00:00:00:00:20", defaultRoute="via 10.1.1.10")
        h21 = self.addHost('h21', ip='10.1.1.21/24', mac="00:00:00:00:00:21", defaultRoute="via 10.1.1.10")
        h22 = self.addHost('h22', ip='10.1.1.22/24', mac="00:00:00:00:00:22", defaultRoute="via 10.1.1.10")
        h23 = self.addHost('h23', ip='10.1.1.23/24', mac="00:00:00:00:00:23", defaultRoute="via 10.1.1.10")
        h24 = self.addHost('h24', ip='10.1.1.24/24', mac="00:00:00:00:00:24", defaultRoute="via 10.1.1.10")
        h25 = self.addHost('h25', ip='10.1.1.25/24', mac="00:00:00:00:00:25", defaultRoute="via 10.1.1.10")


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
        self.addLink(h11, s1, cls=TCLink, bw=5)
        self.addLink(h12, s1, cls=TCLink, bw=5)
        self.addLink(h13, s1, cls=TCLink, bw=5)
        self.addLink(h14, s1, cls=TCLink, bw=5)
        self.addLink(h15, s1, cls=TCLink, bw=5)
        self.addLink(h16, s1, cls=TCLink, bw=5)
        self.addLink(h17, s1, cls=TCLink, bw=5)
        self.addLink(h18, s1, cls=TCLink, bw=5)
        self.addLink(h19, s1, cls=TCLink, bw=5)
        self.addLink(h20, s1, cls=TCLink, bw=5)
        self.addLink(h21, s1, cls=TCLink, bw=5)
        self.addLink(h22, s1, cls=TCLink, bw=5)
        self.addLink(h23, s1, cls=TCLink, bw=5)
        self.addLink(h24, s1, cls=TCLink, bw=5)
        self.addLink(h25, s1, cls=TCLink, bw=5)

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

        h11 = net.get('h11')
        cmd1 = "bash normal.sh &"
        h11.cmd(cmd1)

        h12 = net.get('h12')
        cmd1 = "bash normal.sh &"
        h12.cmd(cmd1)

        h13 = net.get('h13')
        cmd1 = "bash normal.sh &"
        h13.cmd(cmd1)

        h14 = net.get('h14')
        cmd1 = "bash normal.sh &"
        h14.cmd(cmd1)

        h15 = net.get('h15')
        cmd1 = "bash normal.sh &"
        h15.cmd(cmd1)

        h16 = net.get('h16')
        cmd1 = "bash normal.sh &"
        h16.cmd(cmd1)

        h17 = net.get('h17')
        cmd1 = "bash normal.sh &"
        h17.cmd(cmd1)

        h18 = net.get('h18')
        cmd1 = "bash normal.sh &"
        h18.cmd(cmd1)

        h19 = net.get('h19')
        cmd1 = "bash normal.sh &"
        h19.cmd(cmd1)

        h20 = net.get('h20')
        cmd1 = "bash normal.sh &"
        h20.cmd(cmd1)

        h21 = net.get('h21')
        cmd1 = "bash normal.sh &"
        h21.cmd(cmd1)

        h22 = net.get('h22')
        cmd1 = "bash normal.sh &"
        h22.cmd(cmd1)

        h23 = net.get('h23')
        cmd1 = "bash normal.sh &"
        h23.cmd(cmd1)

        h24 = net.get('h24')
        cmd1 = "bash normal.sh &"
        h24.cmd(cmd1)

        h25 = net.get('h25')
        cmd1 = "bash normal.sh &"
        h25.cmd(cmd1)

        sleep(TEST_TIME)
        net.stop()
    elif TEST_TYPE == "attack":
        print "Generating ATTACK Traffic......."
        h1 = net.get('h1')
        cmd1 = "bash attack.sh &"
        h1.cmd(cmd1)

        sleep(TEST_TIME)
        net.stop()


    elif TEST_TYPE =="manual":
        CLI(net)
        net.stop()
