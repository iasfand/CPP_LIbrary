import unittest
from airport_processor.processor import AirportProcessor

class TestAirportProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = AirportProcessor()

    def test_process_airports_data(self):
        airports = [
            {
                "_id": "1",
                "name": "Test Airport",
                "country": "Testland",
                "icaoCode": "TEST",
                "geometry": {"coordinates": [100, 50]},
                "runways": [{"length": 3000}],
            }
        ]
        result = self.processor.process_airports_data(airports)
        self.assertEqual(len(result), 1)
        self.assertIn("google_maps_link", result[0])
        self.assertEqual(result[0]["total_runways"], 1)

if __name__ == "__main__":
    unittest.main()
