import requests

class EarthquakesApiClient:
    def __init__(self, base_url: str, method: str):
        #self.base_url = "https://earthquake.usgs.gov/fdsnws/event/1"
        self.base_url = base_url
        self.method = method
    

    def get_data(
        self, start_time: str, end_time: str, layer_name: str     
    ) -> list[dict]:
        """
        This method retrives data from the earthquake.ugs api

        Args:
            start_time: start time in YYYY-MM-DD format
            end_time: end time in YYYY-MM-DD format
            layer_name: specify capture layer in api; needs be a list[dict]
            
        Returns:
            A list of earth quakes for a specified period.
        
        Raises:
            Exception if the response code is not 200.
        """

        url = f"{self.base_url}"
        print(url)
        params = { "format": self.method, "starttime": start_time, "endtime": end_time }

        response = requests.get(url=url, params=params)

        if response.status_code == 200 and response.json().get(f"{layer_name}"):
            return response.json().get(f"{layer_name}")
        else:
            raise Exception(
                f"Failed to extract data from Earthquake API. Status Code: {response.status_code}. Response: {response.text}"
            )
