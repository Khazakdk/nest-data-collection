#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nest
from datetime import datetime

username = #Nest account username here
password = #Nest password here

napi = nest.Nest(username, password)

status = napi._status

csv = open("nest.csv", "a")

for structure in napi.structures:
    for device in structure.devices:
	csv.write(str(datetime.now())+",")
        print '        Device: %s' % device.name
	csv.write(device.name+",")
        print '        Where: %s' % device.where
	csv.write(device.where+",")
        print '            Mode     : %s' % device.mode
	csv.write(device.mode+",")
        print '            Fan      : %s' % device.fan
	csv.write(str(device.fan)+",")
        print '            Temp     : %0.1fC' % device.temperature
	csv.write(str(nest.utils.c_to_f(device.temperature))+",")
        print '            Humidity : %0.1f%%' % device.humidity
	csv.write(str(device.humidity)+",")
        print '            Target   : %0.1fC' % device.target
	csv.write(str(nest.utils.c_to_f(device.target))+",")
        print '            Away Heat: %0.1fC' % device.away_temperature[0]
	csv.write(str(nest.utils.c_to_f(device.away_temperature[0]))+",")
        print '            Away Cool: %0.1fC' % device.away_temperature[1]
	csv.write(str(nest.utils.c_to_f(device.away_temperature[1]))+",")

        print '            hvac_ac_state         : %s' % device.hvac_ac_state
	csv.write(str(device.hvac_ac_state)+",")
        print '            hvac_cool_x2_state    : %s' % device.hvac_cool_x2_state
        print '            hvac_heater_state     : %s' % device.hvac_heater_state
	csv.write(str(device.hvac_heater_state)+",")
        print '            hvac_aux_heater_state : %s' % device.hvac_aux_heater_state
        print '            hvac_heat_x2_state    : %s' % device.hvac_heat_x2_state
        print '            hvac_heat_x3_state    : %s' % device.hvac_heat_x3_state
        print '            hvac_alt_heat_state   : %s' % device.hvac_alt_heat_state
        print '            hvac_alt_heat_x2_state: %s' % device.hvac_alt_heat_x2_state
        print '            hvac_emer_heat_state  : %s' % device.hvac_emer_heat_state

        print '            online                : %s' % device.online
        print '            last_ip               : %s' % device.last_ip
        print '            local_ip              : %s' % device.local_ip
        print '            last_connection       : %s' % device.last_connection

        print '            error_code            : %s' % device.error_code
      	csv.write(str(device.error_code)+",")
	print '            battery_level         : %s' % device.battery_level
	csv.write(str(device.battery_level)+",")
	csv.write("\n")
	
print "Done @ " + str(datetime.now())
csv.close
