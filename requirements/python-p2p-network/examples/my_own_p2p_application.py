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
node_1 = MyOwnPeer2PeerNode("127.0.0.1", 9001, 1)
node_2 = MyOwnPeer2PeerNode("127.0.0.1", 9002, 2)
node_3 = MyOwnPeer2PeerNode("127.0.0.1", 9003, 3)

time.sleep(1)

node_1.start()
node_2.start()
node_3.start()

time.sleep(1)
import pudb; pu.db
node_1.connect_with_node('127.0.0.1', 9002)
node_2.connect_with_node('127.0.0.1', 9003)
node_3.connect_with_node('127.0.0.1', 9001)

time.sleep(2)

node_1.send_to_nodes("message: Hi there!")

time.sleep(2)

print("node 1 is stopping..")
node_1.stop()

time.sleep(5)

node_2.send_to_nodes("message: Hi there i am node 2!")
node_2.send_to_nodes("message: Hi there i am node 2!")
node_2.send_to_nodes("message: Hi there i am node 2!")
node_3.send_to_nodes("message: Hi there i am node 3!")
node_3.send_to_nodes("message: Hi there i am node 3!")
node_3.send_to_nodes("message: Hi there i am node 3!")

time.sleep(10)

time.sleep(5)

node_1.stop()
node_2.stop()
node_3.stop()

node_1.start()
node_2.start()
node_3.start()
print('end test')
