# Noraportal

A lightweight, zero-dependency Python captive portal designed for Lubuntu/Ubuntu NetworkManager Wi-Fi hotspots, documented for the Acer Nitro 7 / TP-Link Ethernet setup. For complete installation and firewall configuration details, please refer to your local setup scripts.

## Recommended / Tested Hardware
* **Laptop:** Acer Nitro 7 (Intel Core i7 9th Gen)
* **OS:** Lubuntu (Ubuntu-based LXQt)
* **Internet Source (WAN):** TP-Link Extender via Ethernet (`enp7s0`)
* **Hotspot Interface (LAN):** Built-in Wi-Fi (`wlp8s0`)
* **Tested Client Device:** iPhone 11 (iOS Captive Network Assistant)

## Setup & Usage

1. Turn on your built-in Lubuntu Wi-Fi hotspot.
2. Check your Wi-Fi and internet interface names using `nmcli device status` (defaults are `wlp8s0` and `enp7s0`).
3. Apply the `iptables` redirect rules and start **Noraportal**:

```bash
sudo iptables -t nat -F PREROUTING
sudo iptables -F FORWARD
sudo iptables -t nat -I PREROUTING 1 -i wlp8s0 -p tcp --dport 80 -j DNAT --to-destination 10.42.0.1:80
sudo iptables -I INPUT 1 -i wlp8s0 -p tcp --dport 80 -j ACCEPT
sudo iptables -I FORWARD 1 -i wlp8s0 -o enp7s0 -p udp --dport 53 -j ACCEPT
sudo iptables -I FORWARD 2 -i wlp8s0 -o enp7s0 -p tcp --dport 53 -j ACCEPT
sudo iptables -I FORWARD 3 -i wlp8s0 -o enp7s0 -j DROP
sudo python3 portal.py
```

## Stop & Reset Firewall

Press `Ctrl + C` in the terminal, then run:

```bash
sudo iptables -t nat -F PREROUTING
sudo iptables -F FORWARD
```

