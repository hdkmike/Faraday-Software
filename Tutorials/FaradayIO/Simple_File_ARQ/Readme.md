
# Tutorial - Simple File ARQ

This tutorial utilizes the simple file transfer program that is completely unreliable (no error detection or correction/retry) and implements a basic ARQ (automatic retry request) functionality. ARQ functionality will ensure 100% reliable transfer at the cost of retrying corrupt/lost transmissions over a longer time.

##Application Goals



*  **Minimalist protocol**
	*  Reliable operation (Error detection and automatic retry-request "ARQ")
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



## Troubleshooting

**No reception of transmitted data**

*  Make sure the units have properly connected
*  Verify that the antennas are installed on both units
*  Ensure that the units are seperated as far apart as possible (due to possible desensing of the RF front end when close and high power)
*  Reduce transmit power of the transmitting Faraday device to ~10 (PATable)