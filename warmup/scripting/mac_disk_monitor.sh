#!/bin/bash

timestamp=$(date +"%F-%H:%M")
log_file="mac_disk_monitor.log"

disk_usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
echo "$timestamp - $disk_usage% de uso do disco" >> "$log_file"