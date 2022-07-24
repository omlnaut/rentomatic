from dataclasses import dataclass


@dataclass
class RequestError:
    """
    Generic class for collecting errors that happen during requests
    """

    parameter: str
    """Which input to the request caused an the error"""

    message: str
    """Further detail on the error"""
