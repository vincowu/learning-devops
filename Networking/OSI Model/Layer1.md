# Physical Layer
- Physical medium between device and a **shared** medium (Copper, Fibre, Wifi)
- Layer 1 specifications define the transmission and reception of raw bit streams between a device and a shared physical medium. It defines things like volatge levels, timing, rates, distances, modulation and connector type on each end of cable
- Layer 1 device only understands level 1, but layer 3 device understands layer 1, 2 and 3
- Layer 1 has standards for transmitting and receiving onto medium

Hub
- Connects devices together
- Anything a hub receives on **any of its ports is retransmitted to all other ports** including errors or collisions

At Layer 1
- No individual device addresses (uniquely identifiable devices)
- One laptop cannot address traffic directly from other
- Broadcast medium, everything else receives it which is a limitation of layer 1
- 2 devices might try to transmit at once which can cause collision (corrupts transmission)
- If multiple things transmit on same layer 1 physical medium, info is rendered useless

Media Access Control
- No Media Access Control (no method of controlling which devices transmit)
- Collisions are almost guarenteed
- Layer 1 is not able to detect when collisions occur

Layer 1 does not scale well but is fundamental to networking
- For it to be used practically, layer 2 is needed 
