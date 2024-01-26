# Data Link Layer
Layer 2
- Runs over Layer 1 (Physical Layer) and builds over it.
- Layer 2 network can run on different types of Layer 1 networks and provide same capabilities

Frames Concept
- Format for sending info over layer 2 network
- Introduces MAC Address (Unique Identifier) that is 48 bits in hex for manufacturer
- MAC Address is uniquely attached to specific piece of hardware
    - 2 parts:
        1. OUI (Organizationally Unique Identifier)
            - assigned to companies who manufacture network devices
        2. NIC (Network Interface Controller)
            - together with OUI should mean MAC address is globally unique
- Layer 2 can be transmitted onto shared physical medium by layer 1 (light is sent across shared medium)