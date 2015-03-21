#!/bin/python
#-*- coding:utf-8 -*-

import gpxpy
import gpxpy.gpx

def gen_gpx(list):
    gpx = gpxpy.gpx.GPX()
    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)

    # Create first segment in our GPX track:
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    # Create points:
    for i in list:
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(i["y"], i["x"]))
    print gpx.to_xml()


def gen_gpx_(list):
    gpx = gpxpy.gpx.GPX()
    for i in list:
        w = gpxpy.gpx.GPXWaypoint(i["y"], i["x"], "")
        gpx.waypoints.append(w)
    print gpx.to_xml()
