import requests
from .model import SkiPassDTO, visitorDTO
from typing import List, Dict, Any


class ResortClient:
    def __init__(self, base_url: str, timeout: int = 10, retry_count: int = 3):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.retry_count = retry_count
        
    def create_visitor(self, visitor: visitorDTO) -> visitorDTO:
        payload = {"name": visitor.name, "email": visitor.email}
        response = requests.post(
            f"{self.base_url}/visitors", 
            json=payload, 
            timeout=self.timeout
        )
        response.raise_for_status()
        return visitorDTO(**response.json())
    
    def get_all_visitors(self, page: int = 1, size: int = 3) -> List[visitorDTO]:
        params = {"page": page, "size": size}
        response = requests.get(
            f"{self.base_url}/visitors", 
            params=params, 
            timeout=self.timeout
        )
        response.raise_for_status()
        data = response.json()
        return [visitorDTO(**i) for i in data["data"]]
    
    def get_visitor(self, visitor_id: int) -> visitorDTO:
        response = requests.get(
            f"{self.base_url}/visitors/{visitor_id}", 
            timeout=self.timeout
        )
        response.raise_for_status()
        return visitorDTO(**response.json())
    

    
    def purchase_ski_pass(self, visitor_id: int, ski_pass_type: str) -> SkiPassDTO:
        payload = {"type": ski_pass_type}
        response = requests.post(
            f"{self.base_url}/visitors/{visitor_id}/ski-passes", 
            json=payload, 
            timeout=self.timeout
        )
        response.raise_for_status()
        return SkiPassDTO(**response.json())
    
    def get_visitor_ski_passes(self, visitor_id: int) -> List[SkiPassDTO]:
        response = requests.get(
            f"{self.base_url}/visitors/{visitor_id}/ski-passes",
            timeout=self.timeout
        )
        response.raise_for_status()
        return [SkiPassDTO(**i) for i in response.json()]