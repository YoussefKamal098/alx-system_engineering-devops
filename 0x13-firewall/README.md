### UFW (Uncomplicated Firewall)

#### Installation
```bash
sudo apt-get update
sudo apt-get install ufw
```

#### Basic Commands
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

#### Video Tutorial
- [UFW Tutorial](https://youtu.be/lt2itMlreQo?si=Mek4tA6ZvujRN8GO)

#### Man Page
For more detailed information, you can refer to the manual by running:
```bash
man ufw
```

### IPTables

#### Installation
```bash
sudo apt-get update
sudo apt-get install iptables
```

#### Basic Concepts
- **Tables:** Filter (default), NAT, Mangle, Raw, and Security.
- **Chains:** INPUT, OUTPUT, FORWARD, PREROUTING, POSTROUTING.

#### Basic Commands
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

#### Example Commands

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

#### Explanation of Options

- **-A:** Append a rule to a chain.
- **-D:** Delete a rule from a chain.
- **-L:** List all rules in a chain.
- **-p:** Specify the protocol (tcp, udp, icmp).
- **--dport:** Specify the destination port.
- **-j:** Jump to a target (ACCEPT, REJECT, DROP, REDIRECT, SNAT, DNAT).

#### Video Tutorials
- [IPTables Basics Tutorial](https://youtu.be/6Ra17Qpj68c?si=_A3AC2lm7bMkwUP3)
- [Advanced IPTables Tutorial](https://youtu.be/NAdJojxENEU?si=HL8UNLQ_FDMBMZxK)

### UFW vs IPTables

**UFW:**
- **Pros:**
  - User-friendly, easy to set up.
  - Ideal for simple use cases and beginners.
  - Good for basic firewall configurations.

- **Cons:**
  - Limited flexibility compared to iptables.

**IPTables:**
- **Pros:**
  - More complex and powerful.
  - Greater control over network traffic.
  - Suitable for advanced configurations and experienced users.

- **Cons:**
  - More difficult to learn and use.

Both tools are effective for managing firewall rules, but the choice depends on the user's needs and expertise level. For beginners or those who need simple configurations, UFW is recommended. For advanced users requiring detailed control, IPTables is more appropriate.
