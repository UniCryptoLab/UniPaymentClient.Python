from dataclasses import dataclass

from dataclasses_json import dataclass_json
from enum import Enum
from typing import Optional


class BeneficiaryType(Enum):
    INDIVIDUAL = "INDIVIDUAL"
    COMPANY = "COMPANY"
    CORPORATE = "CORPORATE"
    UNKNOWN = "UNKNOWN"


class Relationship(Enum):
    BRANCHOFFICE = "BRANCHOFFICE"
    SPOUSE = "SPOUSE"
    BUSINESSPARTNER = "BUSINESSPARTNER"
    PARENT = "PARENT"
    FRIEND = "FRIEND"
    HOLDINGCOMPANY = "HOLDINGCOMPANY"
    SUPPLIER = "SUPPLIER"
    EXSPOUSE = "EXSPOUSE"
    CHILDREN = "CHILDREN"
    FRANCHISEE = "FRANCHISEE"
    NOTRELATED = "NOTRELATED"
    SELF = "SELF"
    CUSTOMER = "CUSTOMER"
    EMPLOYEE = "EMPLOYEE"
    SUBSIDIARYCOMPANY = "SUBSIDIARYCOMPANY"
    CREDITOR = "CREDITOR"
    DEBTOR = "DEBTOR"
    SIBLING = "SIBLING"
    RELATIVE = "RELATIVE"


@dataclass_json
@dataclass
class Beneficiary:
    name: str
    address: Optional[str] = None
    email: Optional[str] = None
    type: Optional[BeneficiaryType] = None
    relationship: Optional[Relationship] = None
    id: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zip_code: Optional[str] = None
