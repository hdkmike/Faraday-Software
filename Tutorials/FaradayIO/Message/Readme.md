
# Tutorial - Message

This tutorial implements a basic version of the core messaging application using the command application experimental RF packet forward functionality. The goal is to provide a simple keyboard to keyboard text chat using an extreamly simple application layer protocol between two Faraday devices transmitting data over RF.

##Application Goals

This tutorial application with provide an example of a text messaging application that implements packet fragmentation and reassembly to allow transfer of data larger than the MTU (minimum transmissible unit) of the network path. This will allow unrestricted message length but is unreliable and thus not error detected/corrected. This program also forms the basis for generic data tranfer.

*  **Minimalist protocol**
	*  Unreliable operation (No error detection, no automatic retry-request "ARQ")
	*  Simple packet fragmentation and reassembly (START, DATA, END packet types)
	*  Utlize the "Experimentatal RF Packet Forwarding" command to trade speed/optimization for easy python only programming

*  **Program Operation**
	*  A core set of transmit/receive "objects" that provide tx/rx functionality
	*  TX and RX can be independent programs



## Tutorial Operation

To operate the tutorial follow these steps.

1. Connect two Faraday devices to your computer USB
2. Start the Proxy application. Ensure that the proxy configuration is configured to connect to both units properly and allocate the correct callsign-ID.
3. Start the Proxy application
4. Configure the "A_Test_Rx.py" script to connect to the first (A) Faraday device by configuring "local_device_callsign" and "local_device_node_id" properly
5. Start the "A_Test_Rx.py" program
6. Configure the "B_Test_Tx_User_Input.py" script to connect to the second (B) Faraday device by configuring "local_device_callsign" and "local_device_node_id" properly
7. Start the "B_Test_Tx_User_Input.py" program
8. In the "B_Test_Tx_User_Input.py" window prompt type a message to send to the A Faraday device and press enter to transmit.
9. Verify proper transmission and reception in the A Faraday device


## Troubleshooting

**No reception of transmitted data**

*  Make sure the units have properly connected
*  Verify that the antennas are installed on both units
*  Ensure that the units are seperated as far apart as possible (due to possible desensing of the RF front end when close and high power)
*  Reduce transmit power of the transmitting Faraday device to ~10 (PATable)