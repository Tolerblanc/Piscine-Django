import sys
import antigravity


def get_geohash(latitude: float, longitude: float, datedow: str) -> str:
    try:
        if not isinstance(latitude, float) or not isinstance(longitude, float):
            raise ValueError("Latitude and longitude must be floats")
        if not isinstance(datedow, str):
            raise ValueError("Date must be a string")
        if len(datedow) != 10 or datedow[4] != "-" or datedow[7] != "-":
            raise ValueError("Date must be in YYYY-MM-DD format")
        return antigravity.geohash(latitude, longitude, datedow.encode())
    except Exception as e:
        print(e, file=sys.stderr)
        return None


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python geohashing.py <latitude> <longitude> <date in YYYY-MM-DD format>")
        sys.exit(1)
    print(get_geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3]))
