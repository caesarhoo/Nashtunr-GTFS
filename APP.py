from google.transit import gtfs_realtime_pb2
import urllib

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('http://transitdata.nashvillemta.org/TMGTFSRealTimeWebService/tripupdate/tripupdates.pb')
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print entity.trip_update.trip.trip_id,entity.trip_update.trip.route_id
    for stop_time_update in entity.trip_update.stop_time_update:
      print stop_time_update.stop_id
      if stop_time_update.HasField('departure'):
        print "Departure:", stop_time_update.departure
      if stop_time_update.HasField('arrival'):
        print "Arrival:", stop_time_update.arrival