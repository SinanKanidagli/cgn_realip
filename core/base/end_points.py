from abc import ABC,abstractmethod

class EndPoints(ABC):
    
    @property
    @abstractmethod
    def LOGIN(self) -> str:
        pass
    
    @property
    @abstractmethod
    def LOGOUT(self) -> str:
        pass
    
    @property
    @abstractmethod
    def IP_INFORMATION(self) -> str:
        pass