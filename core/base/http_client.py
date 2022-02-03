from requests.models import Response
from abc import ABC,abstractmethod

class ModemHttpClient(ABC):
    @abstractmethod
    def login() -> Response:
        pass
    @abstractmethod
    def logout(self) -> Response:
        pass
    @abstractmethod
    def get_public_ip(self) -> str:
        pass
