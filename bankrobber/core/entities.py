"""
Domain objects used by Bankrobber app
"""
from dataclasses import dataclass


class Entity:
    @classmethod
    def from_dict(cls, adict):
        raise NotImplementedError


@dataclass
class BankAccount(Entity):
    iban: str
    currency: str
    balance: str

    @classmethod
    def from_dict(cls, adict):
        return cls(
            iban=adict.get("iban"),
            currency=adict.get("currency"),
            balance=adict.get("availableBalance"),
        )
