import geocoder

def get_location_from_ip() -> str:
    g = geocoder.ip('me')
    return g.address