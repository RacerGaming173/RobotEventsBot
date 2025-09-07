import math

EARTH_RADIUS_IN_MI = 3959
AUSTIN_LATITUDE = math.radians(30.2672)
AUSTIN_LONGITUDE = math.radians(-97.7431)

def calculate_haversine(lat, long):
    rad_lat, rad_long = math.radians(lat), math.radians(long)
    hav_theta = (1 - math.cos(rad_lat - AUSTIN_LATITUDE) + math.cos(AUSTIN_LATITUDE) * math.cos(rad_lat) * (1 - math.cos(rad_long - AUSTIN_LONGITUDE)))/2   
    return 2 * EARTH_RADIUS_IN_MI * math.asin(math.sqrt(hav_theta))