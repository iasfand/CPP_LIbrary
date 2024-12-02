import boto3
from flask import session, current_app

class AirportProcessor:
    def __init__(self):
        pass

    def get_dynamodb_table(self):
        return current_app.dynamodb.Table("skyport_favs")

    def process_airports_data(self, airports):
        processed_data = []
        for airport in airports:
            _id = airport.get("_id")
            name = airport.get("name")
            country = airport.get("country")
            icaoCode = airport.get("icaoCode") or "-"
            coordinates = airport.get("geometry", {}).get("coordinates", [])
            google_maps_link = (
                f"https://www.google.com/maps/search/?api=1&query={coordinates[1]},{coordinates[0]}"
                if len(coordinates) == 2
                else None
            )
            total_runways = len(airport.get("runways", []))
            favorite_status = self.check_favorite_status(_id)
            processed_data.append(
                {
                    "id": _id,
                    "name": name,
                    "country": country,
                    "icaoCode": icaoCode,
                    "google_maps_link": google_maps_link,
                    "total_runways": total_runways,
                    "is_favorite": favorite_status,
                }
            )
        return processed_data

    def check_favorite_status(self, airport_id):
        is_favorite = False
        if not session.get("logged_in"):
            return is_favorite
        user_id = session["user_id"]
        try:
            table = self.get_dynamodb_table()
            response = table.get_item(Key={"user_id": user_id, "airport_id": airport_id})
            if "Item" in response:
                is_favorite = True
        except Exception as e:
            current_app.logger.error(f"Error checking favorite status: {e}")
        return is_favorite
