from pydantic import (BaseModel,
                      HttpUrl,
                      EmailStr)
from typing import (List,
                    Optional)


class Profile(BaseModel):
    network: str
    username: str
    url: Optional[HttpUrl] = None


class Location(BaseModel):
    postalCode: Optional[str] = None
    city: Optional[str] = None
    countryCode: Optional[str] = None
    region: Optional[str] = None


class Basics(BaseModel):
    name: str
    label: str
    image: Optional[str] = None
    email: EmailStr
    phone: Optional[str] = None
    url: Optional[HttpUrl] = None
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
    score: Optional[str] = None
    courses: List[str] = []


class Certificate(BaseModel):
    name: str
    date: str
    issuer: str
    url: Optional[HttpUrl] = None


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
    description: str
    highlights: List[str] = []
    github: str
    isActive: bool = False
    url: Optional[str] = None
