from dataclasses import dataclass


@dataclass
class RequestError:
    parameter: str
    """Which input to the request caused an the error"""

    message: str
    """Further detail on the error"""
