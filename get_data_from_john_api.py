import thingspeak
import json
import os
import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


i = 0
while(True):
    raw_data_from_room = thingspeak.Channel(1044783).get()
    raw_data_from_garage = thingspeak.Channel(775156).get()
    dict_data_from_room = json.loads(raw_data_from_room)
    dict_data_from_garage = json.loads(raw_data_from_garage)
    data_from_room = pd.DataFrame().from_dict(dict_data_from_room['feeds'])
    data_from_garage = pd.DataFrame().from_dict(dict_data_from_garage['feeds'])
    data_from_room.to_excel('./data/room/raw_get_' + str(i) + '.xlsx')
    data_from_garage.to_excel('./data/garage/raw_get_' + str(i) + '.xlsx')
    print('data ' + str(i) + 'succesfully downloaded at ' + time.asctime(time.gmtime()))
    i += 1
    time.sleep(480)
