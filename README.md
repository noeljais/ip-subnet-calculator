# IP Subnet Calculator

A simple Python-based command-line tool that calculates IPv4 subnet information using an IP address and CIDR prefix.

## Features

- Calculates the network address
- Identifies the subnet mask
- Calculates the broadcast address
- Displays the total number of IP addresses
- Calculates the number of usable host addresses
- Identifies the first usable IP address
- Identifies the last usable IP address
- Handles invalid input using exception handling

## Technologies Used

- Python 3
- Python `ipaddress` module
- Git and GitHub

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/noeljais/ip-subnet-calculator.git
```

**2. Navigate to the project folder**

```bash
cd ip-subnet-calculator
```

**3. Run the program**

```bash
python subnet_calculator.py
```

**4. Enter an IPv4 address with its CIDR prefix.**

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
First Usable IP: 192.168.10.65
Last Usable IP: 192.168.10.126
```

## How It Works

The program uses Python's built-in `ipaddress` module to process an IPv4 address and CIDR prefix.

It identifies the network address, subnet mask, broadcast address, and total number of addresses. It then calculates the conventional usable host count by excluding the network and broadcast addresses.

The first usable IP is calculated by adding one to the network address, while the last usable IP is calculated by subtracting one from the broadcast address.

The program supports conventional IPv4 subnet calculations from `/0` to `/30`. Special `/31` and `/32` networks are not supported.

## Learning Outcomes

This project helped me understand:

- IPv4 addressing and subnetting
- CIDR notation and subnet masks
- Network and broadcast addresses
- Usable IP address ranges
- Python variables, input and output
- Python's built-in `ipaddress` module
- Exception handling using `try` and `except`
- Version control using Git and GitHub

## Future Improvements

- Support special `/31` and `/32` IPv4 networks
- Add AWS-specific subnet address calculations
- Develop a graphical user interface
