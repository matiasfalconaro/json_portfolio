from pydantic import (BaseModel,
                      HttpUrl,
                      EmailStr)
from typing import (List,
                    Optional)


class Profile(BaseModel):
    network: str
    username: str
    url: Optional[HttpUrl]


class Location(BaseModel):
    postalCode: Optional[str]
    city: Optional[str]
    countryCode: Optional[str]
    region: Optional[str]


class Basics(BaseModel):
    name: str
    label: str
    image: Optional[str]
    email: EmailStr
    phone: Optional[str]
    url: Optional[HttpUrl]
    summary: str
    location: Location
    profiles: List[Profile]


class Work(BaseModel):
    name: str
    position: str
    url: Optional[HttpUrl] = None
    startDate: str
    endDate: str
    summary: str
    highlights: List[str]


class Education(BaseModel):
    institution: str
    url: Optional[HttpUrl] = None 
    area: str
    studyType: str
    startDate: str
    endDate: str
    score: Optional[str]


class Certificate(BaseModel):
    name: str
    date: str
    issuer: str
    url: Optional[HttpUrl]


class Skill(BaseModel):
    name: str
    level: str
    keywords: List[str]


class Language(BaseModel):
    language: str
    fluency: str


class Interest(BaseModel):
    name: Optional[str]
    keywords: List[Optional[str]]


class Reference(BaseModel):
    name: Optional[str]
    reference: Optional[str]


class Project(BaseModel):
    name: str
    role: str
    isActive: bool
    description: str
    highlights: List[str]
    url: Optional[HttpUrl]
    github: Optional[str]
