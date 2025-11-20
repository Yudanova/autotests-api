from faker import Faker
import requests


fake = Faker()

print(fake.name())         # Output: John Doe
print(fake.address())      # Output: 1234 Elm St, Springfield, IL
print(fake.email())        # Output: j.doe@example.com

fake = Faker()

user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "address": fake.address()
}

print(user_data)


fake = Faker()

# Generate fake data
user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=18, max=100)
}

# Send a POST request with the fake data
response = requests.post("https://api.example.com/users", json=user_data)

# Check that the request was successful
assert response.status_code == 201
# This domain is just example:  api.example.com is a placeholder.
# Need to using environment variables or config files to manage base URLs for different environments (dev, staging, prod).


#draft for HW
class CreateExerciseRequestSchema(BaseModel):
    """
    Description of the request structure for creating an exercise.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)






