import requests
from datetime import datetime, timedelta

class DataIngestor:
    def __init__(self):
        self.api_key = 'your_api_key'  # Replace with actual API key
        self.base_url = 'https://api.xero.com/api/v2'
        
    def fetch_data(self, endpoint):
        """
        Fetches data from Xero API.
        Args:
            endpoint (str): The specific endpoint to call.
        Returns:
            dict: Response data.
        """
        try:
            headers = {'Authorization': f'Bearer {self.api_key}'}
            response = requests.get(f'{self.base_url}/{endpoint}', headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.log_error(f"API request failed: {str(e)}")
            raise
            
    def log_error(self, message):
        """Logs errors with a timestamp."""
        with open('data_ingestion_errors.log', 'a') as f:
            f.write(f"{datetime.now()}: {message}\n")