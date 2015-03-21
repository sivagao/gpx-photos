#!/bin/python
#-*- coding:utf-8 -*-

from photo import get_geo_from_photo
from gpx import gen_gpx

import os, sys

if os.path.exists(sys.argv[1]):
    info_list = []
    for f in os.listdir(sys.argv[1]):
        if os.path.splitext(f)[1].lower() == ".jpg":
            fp = os.path.join(sys.argv[1], f)
            try:
                gpsinfo = get_geo_from_photo(fp)
                if(gpsinfo.get("x", "") and gpsinfo.get("y", "")):
                    info_list.append(gpsinfo)
            except:
                pass

    gen_gpx(info_list)