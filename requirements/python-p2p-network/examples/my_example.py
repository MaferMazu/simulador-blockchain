#######################################################################################################################
# Author: Maurice Snoeren                                                                                             #
# Version: 0.1 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# This example show how to derive a own Node class (MyOwnPeer2PeerNode) from p2pnet.Node to implement your own Node   #
# implementation. See the MyOwnPeer2PeerNode.py for all the details. In that class all your own application specific  #
# details are coded.                                                                                                  #
#######################################################################################################################

import sys
import time
sys.path.insert(0, '..') # Import the files where the modules are located

from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode
import pudb; pu.db
node_1 = MyOwnPeer2PeerNode("127.0.0.1", 9001, 1)
node_2 = MyOwnPeer2PeerNode("127.0.0.1", 9002, 2)
node_3 = MyOwnPeer2PeerNode("127.0.0.1", 9003, 3)
node_4 = MyOwnPeer2PeerNode("127.0.0.1", 9004, 4)
node_5 = MyOwnPeer2PeerNode("127.0.0.1", 9005, 5)
node_6 = MyOwnPeer2PeerNode("127.0.0.1", 9006, 6)

time.sleep(1)

node_1.start()
node_2.start()
node_3.start()
node_4.start()
node_5.start()

time.sleep(1)

node_1.connect_with_node('127.0.0.1', 9002)
node_1.connect_with_node('127.0.0.1', 9003)
node_1.connect_with_node('127.0.0.1', 9004)
node_1.connect_with_node('127.0.0.1', 9005)

time.sleep(2)

node_1.send_to_nodes("message: Hi there i am node 1!")

time.sleep(2)


time.sleep(20)

node_2.send_to_node(node_1,"message: Hi there i am node 2!")
node_3.send_to_node(node_1,"message: Hi there i am node 3!")
node_4.send_to_node(node_1,"message: Hi there i am node 4!")
node_5.send_to_node(node_1,"message: Hi there i am node 5!")

time.sleep(10)

time.sleep(5)

node_1.stop()
node_2.stop()
node_3.stop()
node_4.stop()
node_5.stop()

print('end test')
