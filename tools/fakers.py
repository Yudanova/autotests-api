import time
from faker import Faker


class Fake:
    """
    A class for generating random test data using the Faker library.
    """

    def __init__(self, faker: Faker):
        """
        :param faker: An instance of the Faker class to be used for data generation.
        """
        self.faker = faker

    def text(self) -> str:
        """
        Generates random text.

        :return: Random text.
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Generates a random UUID4.

        :return: Random UUID4.
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Generates a random email.
        :param domain: like "example.com"
        :return: Random email.
        """
        return self.faker.email(domain=domain)

    def sentence(self) -> str:
        """
        Generates a random sentence.

        :return: Random sentence.
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Generates a random password.

        :return: Random password.
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Generates a random last name.

        :return: Random last name.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Generates a random first name.

        :return: Random first name.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Generates a random middle name.

        :return: Random middle name.
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        Generates a string representing estimated time (e.g., "2 weeks").

        :return: Estimated time string.
        """
        return f"{self.integer(1, 10)} weeks"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Generates a random integer within the specified range.

        :param start: Start of the range (inclusive).
        :param end: End of the range (inclusive).
        :return: Random integer.
        """
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """
        Generates a random maximum score between 50 and 100.

        :return: Random score.
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Generates a random minimum score between 1 and 30.

        :return: Random score.
        """
        return self.integer(1, 30)


# Create an instance of the Fake class using Faker
fake = Fake(faker=Faker())


# def fake.email() -> str:   # replaced to fake
#     return f"test.{time.time()}@example.com"
# # print(time.time())
"""
Scalability: Easily configure the random data generator for different languages and providers by passing a different instance of Faker to the constructor.
Resilience: If the logic for data generation changes or needed to be switch to a different library, it only need to update the code in the Fake class, not throughout the entire project.
Code clarity and readability: The wrapper makes the code cleaner and easier to understand, since all calls to the Faker library are centralized in one place.

"""