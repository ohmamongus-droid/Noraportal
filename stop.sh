#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root: sudo ./stop.sh"
  exit 1
fi

echo "Resetting Noraportal firewall rules..."
iptables -t nat -F PREROUTING
iptables -F FORWARD

echo "Noraportal stopped. Normal hotspot traffic restored."
