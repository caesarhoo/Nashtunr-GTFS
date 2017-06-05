from google.transit import gtfs_realtime_pb2
import urllib
from datetime import datetime

feed = gtfs_realtime_pb2.FeedMessage()
# Nashville MTA proto buffer file
response = urllib.urlopen('http://transitdata.nashvillemta.org/TMGTFSRealTimeWebService/tripupdate/tripupdates.pb')
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
    # print out a certain bus stop realtime schedule with its trip_id and route_id
    for stop_time_update in entity.trip_update.stop_time_update:
        if stop_time_update.stop_id == '8AVUNINN' and stop_time_update.HasField('departure'):
            # Use route_id for bus name, and trip_id to get trip_headsign from GTFS database
            # The time should be converted to central time for Nashville
            print 'trip_id:' + entity.trip_update.trip.trip_id,'route_id:' + entity.trip_update.trip.route_id
            print 'stop_id:' + stop_time_update.stop_id
            if stop_time_update.departure.delay == 0:
                time  = stop_time_update.departure.time
                # convert unix time to readable time
                x = datetime.fromtimestamp(time)
                print "Departure:", x
            else:
                # Check result
                # print stop_time_update.departure

                # If there is a delay, add to the departure time
                time  = stop_time_update.departure.time + stop_time_update.departure.delay
                x = datetime.fromtimestamp(time)
                print "Departure:", x

        # Every last stop of a trip will only have arrival
        if stop_time_update.stop_id == '8AVUNINN' and stop_time_update.HasField('arrival'):
            print 'trip_id:' + entity.trip_update.trip.trip_id,'route_id:' + entity.trip_update.trip.route_id
            print 'stop_id:' + stop_time_update.stop_id
            if stop_time_update.arrival.delay == 0:
                time  = stop_time_update.arrival.time
                x = datetime.fromtimestamp(time)
                print "Arrival:", x
            else:
                print stop_time_update.departure
                time  = stop_time_update.arrival.time + stop_time_update.arrival.delay
                x = datetime.fromtimestamp(time)
                print "Arrival:", x

