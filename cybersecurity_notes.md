# Cybersecurity and Networking Notes

## Introduction

These notes contain foundational cybersecurity and networking concepts learned during my BTech Cyber Security studies. Topics include networking fundamentals, reconnaissance tools, Linux basics, and security-related concepts.

---

# Networking Fundamentals

## OSI Model

The OSI (Open Systems Interconnection) Model contains 7 layers:

1. Physical Layer
2. Data Link Layer
3. Network Layer
4. Transport Layer
5. Session Layer
6. Presentation Layer
7. Application Layer

The OSI model explains how data travels through a network from sender to receiver.

---

## DNS (Domain Name System)

DNS converts domain names into IP addresses.

Example:

google.com → IP address

DNS helps users access websites using names instead of numerical IP addresses.

---

## Port Numbers and Types

Ports are communication endpoints used by network services.

### Common Ports

- Port 20/21 → FTP
- Port 22 → SSH
- Port 23 → Telnet
- Port 25 → SMTP
- Port 53 → DNS
- Port 80 → HTTP
- Port 443 → HTTPS

### Types of Ports

- Well-known ports
- Registered ports
- Dynamic/private ports

---

## IP Addressing

An IP address identifies devices connected to a network.

### Types

- IPv4
- IPv6

### IP Address Classes

- Class A
- Class B
- Class C
- Class D
- Class E

---

# Reconnaissance Tools

Reconnaissance is the process of collecting information about a target system or network.

---

## WHOIS

WHOIS is used to obtain domain registration details.

Information collected includes:
- Domain owner
- Registrar
- Registration dates
- Expiry dates

Example:
whois google.com

---

## NSLOOKUP

NSLOOKUP is used to query DNS records.

It helps identify:
- Domain IP address
- DNS server information

Example:
nslookup google.com

---

## Nmap

Nmap is a network scanning tool used for:
- Host discovery
- Port scanning
- Service detection

Example:
nmap 192.168.1.1

---

## Traceroute

Traceroute identifies the path packets travel across a network.

It helps analyze:
- Network delays
- Routing paths

Example:
traceroute google.com

---

## Telnet

Telnet is a remote communication protocol.

It allows remote access to systems over a network.

Example:
telnet 192.168.1.1

---

## Shodan

Shodan is a search engine for internet-connected devices.

Used for:
- Device discovery
- Security analysis
- Exposure identification

---

# Kali Linux Basics

Kali Linux is a Linux distribution designed for cybersecurity and penetration testing.

## Linux Commands

- pwd → Present working directory
- ls → List files
- cd → Change directory
- mkdir → Create directory
- rm → Remove files
- touch → Create file
- cat → Display file contents
- clear → Clear terminal

---

# Cybersecurity Concepts

## Network Security

Protecting networks from unauthorized access, attacks, and misuse.

---

## Reconnaissance

The first phase of cybersecurity assessment where information about a target is collected.

---

## Ethical Hacking

Authorized security testing performed to identify vulnerabilities in systems and networks.

---

# Learning Outcome

Through these topics and tools, I gained foundational knowledge in:
- Networking
- Linux systems
- Reconnaissance techniques
- Basic cybersecurity concepts
- Security tools and commands
