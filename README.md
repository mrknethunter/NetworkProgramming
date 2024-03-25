# NetworkProgramming
Implementation of the main communication protocols such as TCP and UDP

## Brief overview of those protocols

### TCP (Transmission Control Protocol)
TCP is a connection-oriented network protocol that prefer reliability instead of pure efficiency. TCP ensure that every packet is delivered in the correct order as the sender want and it has an error management mechanism.

### UDP (User Datagram Protocol)
UDP, unlike TCP, is a connection-less network protocol that prefer efficiency of the transmission instead of reliability by default. It doesn't establish a connection between hosts before transmitting data, making it, as mentioned, fast but not reliable. However, UDP is still used where the performances are crucial (with custom control mechanisms) in softwares like real-time chat, online games and in the Internet backbone such as DNS and DHCP.
