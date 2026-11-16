# IP Subnet Calculator

A simple Python-based command-line tool that calculates IPv4 subnet information from an IP address and CIDR prefix.

## Features

- Calculates the network address
- Identifies the subnet mask
- Calculates the broadcast address
- Displays the total number of IP addresses
- Calculates conventional usable host addresses
- Handles invalid IP address input

## Technologies Used

- Python 3
- Python `ipaddress` module

## How to Run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python subnet_calculator.py
```

4. Enter an IPv4 address with its CIDR prefix.

## Example

**Input:**
```text
192.168.10.70/26
```

**Output:**
```text
Network Address: 192.168.10.64
Subnet Mask: 255.255.255.192
Broadcast Address: 192.168.10.127
Total Addresses: 64
Usable Hosts: 62
```

## Limitations

The usable-host calculation follows the conventional IPv4 rule of subtracting two addresses. Special `/31` and `/32` networks are not yet handled separately.

## Learning Outcomes

This project helped me practise Python input handling, built-in modules, exception handling, and IPv4 subnet calculations.

## Future Improvements

- Support special IPv4 subnet cases
- Display the usable IP address range
- Add AWS-specific subnet calculations