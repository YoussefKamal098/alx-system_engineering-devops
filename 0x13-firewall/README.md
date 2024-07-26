## IPTables and UFW Documentation

### Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
   - [IPTables Installation](#iptables-installation)
   - [UFW Installation](#ufw-installation)
3. [Basic Concepts](#basic-concepts)
   - [IPTables Tables and Chains](#iptables-tables-and-chains)
   - [UFW Overview](#ufw-overview)
4. [Basic Commands](#basic-commands)
   - [IPTables Commands](#iptables-basic-commands)
   - [UFW Commands](#ufw-basic-commands)
5. [Example Commands](#example-commands)
   - [IPTables Examples](#iptables-example-commands)
   - [UFW Examples](#ufw-examples)
6. [Explanation of Options](#explanation-of-options)
   - [IPTables Options](#iptables-explanation-of-options)
   - [UFW Options](#ufw-explanation-of-options)
7. [Explanation of Targets](#explanation-of-targets)
8. [Additional Features](#additional-features)
   - [IPTables Connection Tracking](#iptables-connection-tracking)
   - [IPTables Marking Packets](#iptables-marking-packets)
   - [IPTables Logging](#iptables-logging)
   - [UFW Configuration Files](#ufw-configuration-files)
9. [UFW vs IPTables](#ufw-vs-iptables)
10. [Video Tutorials](#video-tutorials)
11. [References](#references)

### Introduction
`iptables` and `ufw` are tools for configuring the Linux kernel firewall. `iptables` provides detailed control over network traffic and packet filtering, while `ufw` (Uncomplicated Firewall) offers a simplified interface for managing firewall rules.

### Installation

#### IPTables Installation
To install `iptables` on a Debian-based system:
```bash
sudo apt-get update
sudo apt-get install iptables
```

#### UFW Installation
To install `ufw` on a Debian-based system:
```bash
sudo apt-get update
sudo apt-get install ufw
```

### Basic Concepts

#### IPTables Tables and Chains

- **Tables:**
  - **Filter Table:** Default table used for packet filtering.
  - **NAT Table:** Used for network address translation.
  - **Mangle Table:** Used for packet alteration.
  - **Raw Table:** Used for configuration of exemptions from connection tracking.
  - **Security Table:** Used for Mandatory Access Control (MAC) networking.

- **Chains:**
  - **INPUT:** Handles incoming packets destined for the local system.
  - **OUTPUT:** Handles outgoing packets originating from the local system.
  - **FORWARD:** Handles packets being routed through the system.
  - **PREROUTING:** Alters packets as they arrive before routing.
  - **POSTROUTING:** Alters packets as they leave after routing.

#### UFW Overview
`ufw` (Uncomplicated Firewall) is designed to simplify managing a netfilter firewall. It provides an easier interface to configure firewall rules compared to `iptables`. It is suitable for basic firewall setups and is user-friendly.

### Basic Commands

#### IPTables Commands
- **List All Rules:**
  ```bash
  sudo iptables -L
  ```

- **Allow Traffic on a Port (e.g., SSH on port 22):**
  ```bash
  sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
  ```

- **Block Traffic on a Port (e.g., HTTP on port 80):**
  ```bash
  sudo iptables -A INPUT -p tcp --dport 80 -j REJECT
  ```

- **Save the Rules:**
  ```bash
  sudo iptables-save > /etc/iptables/rules.v4
  ```

- **Flush All Rules:**
  ```bash
  sudo iptables -F
  ```

- **Set Default Policy:**
  ```bash
  sudo iptables -P INPUT DROP
  sudo iptables -P FORWARD DROP
  sudo iptables -P OUTPUT ACCEPT
  ```

#### UFW Commands
- **Enable UFW:**
  ```bash
  sudo ufw enable
  ```

- **Disable UFW:**
  ```bash
  sudo ufw disable
  ```

- **Check the Status:**
  ```bash
  sudo ufw status
  ```

- **Allow a Port (e.g., SSH on port 22):**
  ```bash
  sudo ufw allow 22/tcp
  ```

- **Deny a Port (e.g., HTTP on port 80):**
  ```bash
  sudo ufw deny 80/tcp
  ```

- **Allow a Port for a Specific IP (e.g., allow SSH from 192.168.1.100):**
  ```bash
  sudo ufw allow from 192.168.1.100 to any port 22
  ```

- **Deny a Port for a Specific IP (e.g., deny HTTP from 192.168.1.100):**
  ```bash
  sudo ufw deny from 192.168.1.100 to any port 80
  ```

- **Allow a Range of Ports (e.g., allow ports 6000-6005):**
  ```bash
  sudo ufw allow 6000:6005/tcp
  ```

- **Deny a Range of Ports (e.g., deny ports 6000-6005):**
  ```bash
  sudo ufw deny 6000:6005/tcp
  ```

- **Allow a Subnet (e.g., allow all traffic from 192.168.1.0/24):**
  ```bash
  sudo ufw allow from 192.168.1.0/24
  ```

- **Deny a Subnet (e.g., deny all traffic from 192.168.1.0/24):**
  ```bash
  sudo ufw deny from 192.168.1.0/24
  ```

- **Reset UFW:**
  ```bash
  sudo ufw reset
  ```

### Example Commands

#### IPTables Examples
- **Allow Incoming HTTP (port 80) Traffic:**
  ```bash
  sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
  ```

- **Allow Incoming HTTPS (port 443) Traffic:**
  ```bash
  sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
  ```

- **Allow SSH Traffic Only from a Specific IP (e.g., 192.168.1.100):**
  ```bash
  sudo iptables -A INPUT -p tcp -s 192.168.1.100 --dport 22 -j ACCEPT
  ```

- **Block All Incoming Traffic Except SSH, HTTP, and HTTPS:**
  ```bash
  sudo iptables -P INPUT DROP
  sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
  sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
  sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
  sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
  ```

- **Redirect Traffic from Port 8080 to Port 80:**
  ```bash
  sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
  ```

- **NAT Example (SNAT):**
  ```bash
  sudo iptables -t nat -A POSTROUTING -o eth0 -j SNAT --to-source 192.168.1.1
  ```

- **NAT Example (DNAT):**
  ```bash
  sudo iptables -t nat -A PREROUTING -p tcp -d 203.0.113.1 --dport 80 -j DNAT --to-destination 192.168.1.100:80
  ```

- **Masquerading (useful for internet connection sharing):**
  ```bash
  sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
  ```

- **Marking Packets (Mangle Table):**
  ```bash
  sudo iptables -t mangle -A PREROUTING -p tcp --dport 22 -j MARK --set-mark 1
  ```

- **Rate Limiting (e.g., limit SSH connections to 5 per minute):**
  ```bash
  sudo iptables -A INPUT -p tcp --dport 22 -m limit --limit 5/minute -j ACCEPT
  ```

#### UFW Examples
- **Allow Incoming SSH (port 22):**
  ```bash
  sudo ufw allow 22
  ```

- **Allow Incoming HTTP (port 80):**
  ```bash
  sudo ufw allow 80
  ```

- **Allow Incoming HTTPS (port 443):**
  ```bash
  sudo ufw allow 443
  ```

- **Allow Incoming Traffic from a Specific IP (e.g., 192.168.1.100) for SSH:**
  ```bash
  sudo ufw allow

  from 192.168.1.100 to any port 22
  ```

- **Block All Incoming Traffic Except SSH, HTTP, and HTTPS:**
  ```bash
  sudo ufw default deny incoming
  sudo ufw allow 22
  sudo ufw allow 80
  sudo ufw allow 443
  ```

- **Redirect Traffic from Port 8080 to Port 80 (UFW doesn’t support this directly; use IPTables for complex rules):**
  ```bash
  # Use IPTables for redirection
  ```

- **Allow Traffic from a Subnet (e.g., 192.168.1.0/24):**
  ```bash
  sudo ufw allow from 192.168.1.0/24
  ```

- **Allow a Range of Ports (e.g., 6000-6005):**
  ```bash
  sudo ufw allow 6000:6005/tcp
  ```

### Explanation of Options

#### IPTables Options
- **-A (Append):** Adds a rule to the end of a chain.
  - **Example:** `-A INPUT -p tcp --dport 22 -j ACCEPT`
  
- **-D (Delete):** Removes a specific rule from a chain.
  - **Example:** `-D INPUT -p tcp --dport 22 -j ACCEPT`
  
- **-I (Insert):** Inserts a rule at a specific position in a chain.
  - **Example:** `-I INPUT 1 -p tcp --dport 22 -j ACCEPT`
  
- **-R (Replace):** Replaces a rule at a specific position in a chain.
  - **Example:** `-R INPUT 1 -p tcp --dport 22 -j ACCEPT`
  
- **-L (List):** Lists all rules in a chain.
  - **Example:** `-L INPUT`
  
- **-F (Flush):** Clears all rules from a chain.
  - **Example:** `-F INPUT`
  
- **-Z (Zero):** Resets the packet and byte counters in all chains.
  - **Example:** `-Z INPUT`
  
- **-N (New Chain):** Creates a new user-defined chain.
  - **Example:** `-N MYCHAIN`
  
- **-X (Delete Chain):** Deletes a user-defined chain.
  - **Example:** `-X MYCHAIN`
  
- **-P (Policy):** Sets the default policy for a chain.
  - **Example:** `-P INPUT DROP`
  
- **-p (Protocol):** Specifies the protocol (tcp, udp, icmp).
  - **Example:** `-p tcp`
  
- **-s (Source):** Specifies the source IP address.
  - **Example:** `-s 192.168.1.0/24`
  
- **-d (Destination):** Specifies the destination IP address.
  - **Example:** `-d 192.168.1.100`
  
- **--sport (Source Port):** Specifies the source port.
  - **Example:** `--sport 22`
  
- **--dport (Destination Port):** Specifies the destination port.
  - **Example:** `--dport 80`
  
- **-j (Jump):** Specifies the target of the rule (ACCEPT, REJECT, DROP, etc.).
  - **Example:** `-j ACCEPT`
  
- **-t (Table):** Specifies the table to use (filter, nat, mangle, raw, security).
  - **Example:** `-t nat`
  
- **-m (Match):** Specifies extended packet matching options (conntrack, state, limit, etc.).
  - **Example:** `-m state --state ESTABLISHED,RELATED`
  
- **--ctstate (Connection Tracking State):** Matches connection tracking states (NEW, ESTABLISHED, RELATED).
  - **Example:** `--ctstate ESTABLISHED`
  
- **--conntrack (Connection Tracking):** Uses connection tracking for matches.
  - **Example:** `--conntrack STATE`
  
- **--set-mark (Set Mark):** Sets a mark value on packets.
  - **Example:** `--set-mark 1`

#### UFW Options
- **allow/deny:** Allows or denies traffic for a specific port or IP.
  - **Example:** `sudo ufw allow 22/tcp`, `sudo ufw deny 80/tcp`
  
- **from/to:** Specifies source or destination IP addresses.
  - **Example:** `sudo ufw allow from 192.168.1.100 to any port 22`
  
- **proto:** Specifies the protocol (tcp, udp).
  - **Example:** `sudo ufw allow proto tcp`
  
- **port/range:** Specifies the port or port range.
  - **Example:** `sudo ufw allow 6000:6005/tcp`
  
- **route:** Specifies routing rules for UFW.
  - **Example:** `sudo ufw route allow proto tcp from any to any port 8080`
  
- **reset:** Resets all UFW rules to default.
  - **Example:** `sudo ufw reset`

### Explanation of Targets

- **ACCEPT:** Allows the packet through.
  - **Example:** `-j ACCEPT`
  
- **REJECT:** Rejects the packet and sends an error response.
  - **Example:** `-j REJECT`
  
- **DROP:** Drops the packet silently without response.
  - **Example:** `-j DROP`
  
- **REDIRECT:** Redirects the packet to a different port on the local machine.
  - **Example:** `-j REDIRECT --to-port 80`
  
- **SNAT (Source NAT):** Changes the source address of outgoing packets.
  - **Example:** `-j SNAT --to-source 192.168.1.1`
  
- **DNAT (Destination NAT):** Changes the destination address of incoming packets.
  - **Example:** `-j DNAT --to-destination 192.168.1.100:80`
  
- **MASQUERADE:** Automatically uses the IP address of the outgoing interface as the source address. Useful for internet sharing.
  - **Example:** `-j MASQUERADE`

### Additional Features

#### IPTables Connection Tracking
`iptables` supports connection tracking, which allows the firewall to keep track of the state of network connections and apply rules based on that state.
- **Example:** `-m conntrack --ctstate ESTABLISHED,RELATED` matches packets that are part of an existing connection or related to an existing connection.

#### IPTables Marking Packets
Packets can be marked with specific values to apply further processing or routing decisions.
- **Example:** `-t mangle -A PREROUTING -p tcp --dport 22 -j MARK --set-mark 1` sets a mark value of 1 for incoming TCP packets on port 22.

#### IPTables Logging
`iptables` can log packets that match certain rules.
- **Example:** `-A INPUT -p tcp --dport 22 -j LOG --log-prefix "SSH Access: "` logs all incoming TCP packets on port 22 with the prefix "SSH Access: ".

#### UFW Configuration Files
- **/etc/ufw/after.init:** Scripts to run after initializing the firewall.
- **/etc/ufw/applications.d:** Application-specific rules.
- **/etc/ufw/after.rules:** IPv4 rules to apply after the firewall is initialized.
- **/etc/ufw/after6.rules:** IPv6 rules to apply after the firewall is initialized.
- **/etc/ufw/before.init:** Scripts to run before initializing the firewall.
- **/etc/ufw/before.rules:** IPv4 rules to apply before the firewall is initialized.
- **/etc/ufw/before6.rules:** IPv6 rules to apply before the firewall is initialized.
- **/etc/ufw/sysctl.conf:** Custom sysctl settings for UFW.
- **/etc/ufw/ufw.conf:** Main configuration file for UFW.
- **/etc/ufw/user.rules:** User-defined IPv4 rules.
- **/etc/ufw/user6.rules:** User-defined IPv6 rules.

### UFW vs IPTables

**UFW:**
- **Pros:**
  - User-friendly, easy to set up.
  - Ideal for simple use cases and beginners.
  - Good for basic firewall configurations.

- **Cons:**
  - Limited flexibility compared to iptables.
  - Lacks advanced features and fine-grained control.

**IPTables:**
- **Pros:**
  - More complex and powerful.
  - Greater control over network traffic.
  - Suitable for advanced configurations and experienced users.

- **Cons:**
  - More difficult to learn and use.
  - Configuration can be complex and require more expertise.

Both tools are effective for managing firewall rules, but the choice depends on the user's needs and expertise level. For beginners or those who need simple configurations, UFW is recommended. For advanced users requiring detailed control, IPTables is more appropriate.

### Video Tutorials
- [IPTables Basics Tutorial](https://youtu.be/6Ra17Qpj68c?si=_A3AC2lm7bMkwUP3)
- [Advanced IPTables Tutorial](https://youtu.be/NAdJojxENEU?si=HL8UNLQ_FDMBMZxK)
- [UFW Tutorial](https://youtu.be/lt2itMlreQo?si=Mek4tA6ZvujRN8GO)

### References
- [IPTables Manual](https://linux.die.net/man/8/iptables)
- [UFW Manual](https://manpages.ubuntu.com/manpages/bionic/man8/ufw.8.html)
- [UFW Documentation](https://help.ubuntu.com/community/UFW)
