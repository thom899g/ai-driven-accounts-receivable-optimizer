import json
from rabbitmq import RabbitMQClient

class IntegrationMiddleware:
    def __init__(self):
        self.rabbitmq = RabbitMQClient()
        
    def transform_data(self, data, source):
        """
        Transforms data based on the source (Xero/QuickBooks).
        Args:
            data (dict): Raw data.
            source (str): Data source.
        Returns:
            dict: Standardized data.
        """
        if source == 'xero':
            return self._transform_xero_data(data)
        elif source == 'quickbooks':
            return self._transform_quickbooks_data(data)
        
    def _transform_xero_data(self, data):