#!/bin/sh

qemu-system-x86_64 -cdrom ${HOME}/Downloads/iso/debian-12.5.0-amd64-netinst.iso -M accel=hvf --cpu host --smp 4 -m 8192 mysql.img -net user,hostfwd=tcp::33006-:3306,hostfwd=tcp::10022-:22 -net nic &
