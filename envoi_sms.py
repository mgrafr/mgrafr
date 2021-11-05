#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import time,serial;

phone=serial.Serial(port="COM7",baudrate=115200,timeout=2);
# envoi de +++ et une commande AT dans le délai de 3 secondes
phone.write(b'+++');
time.sleep(2);
phone.write(b'AT+VER\r\n');
time.sleep(1);
phone.write(b'AT+SMSSEND=06xxxxxxxxx,super\r\n')
