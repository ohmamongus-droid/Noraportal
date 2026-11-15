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

## Quick Start

```bash
git clone https://github.com
cd Noraportal
chmod +x start.sh stop.sh
sudo ./start.sh
```

## Stop & Reset Firewall

```bash
sudo ./stop.sh
```
*(Or press `Ctrl + C` in the terminal to stop the server before running the script).*
