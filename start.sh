#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root: sudo ./start.sh"
  exit 1
fi

INTERFACE="wlp8s0"
WAN="enp7s0"
GATEWAY_IP="10.42.0.1"

echo "Turning off Wi-Fi power saving on $INTERFACE..."
iw dev $INTERFACE set power_save off 2>/dev/null

echo "Applying Noraportal firewall rules..."
iptables -t nat -F PREROUTING
iptables -F FORWARD

iptables -t nat -I PREROUTING 1 -i $INTERFACE -p tcp --dport 80 -j DNAT --to-destination $GATEWAY_IP:80
iptables -I INPUT 1 -i $INTERFACE -p tcp --dport 80 -j ACCEPT
iptables -I FORWARD 1 -i $INTERFACE -o $WAN -p udp --dport 53 -j ACCEPT
iptables -I FORWARD 2 -i $INTERFACE -o $WAN -p tcp --dport 53 -j ACCEPT
iptables -I FORWARD 3 -i $INTERFACE -o $WAN -j DROP

echo "Starting Noraportal (Press Ctrl+C to stop)..."
python3 "$(dirname "$0")/portal.py"
