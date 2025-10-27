from pydantic import BaseModel, Field, ValidationError
from datetime import datetime, time
from typing import Optional

# class User(BaseModel):
#     id: int
#     name: str
#     email: str
#     is_active: bool = True
#
# user = User(id="1234", name="Alice", email="alice@example.com")
# print(user)
#
#
#
# class Event(BaseModel):
#     name: str
#     attendees: int = Field(..., gt=0)
#     price: float = Field(..., ge=0)
#     start_time: datetime
#     end_time: Optional[datetime]
#     duration: Optional[time]
#
# # Valid input
# try:
#     event = Event(
#         name="Python Meetup",
#         attendees=25,
#         price=0.0,
#         start_time="2025-10-25T18:00:00",
#         end_time="2025-10-25T20:00:00",
#         duration="02:00:00"
#     )
#     print(event)
# except ValidationError as e:
#     print(e)
#
#
# try:
#     bad_event = Event(
#         name="",
#         attendees=-5,
#         price=-10,
#         start_time="not-a-date"
#     )
# except ValidationError as e:
#     print(e.json(indent=2))

from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int

try:
    user = User(name="Alice")  # Missing 'age'
except ValidationError as e:
    print(e.errors())

