import pytest

# Fixture that will be automatically called for each test
@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Sending data to the analytics service")

# Fixture for initializing test settings at the session level
@pytest.fixture(scope='session')
def settings():
    print("[SESSION] Initializing test settings")

# Fixture for creating user data, executed once per test class
@pytest.fixture(scope='class')
def user():
    print("[CLASS] Creating user data once per test class")

# Fixture for initializing the API client, executed for each test
@pytest.fixture(scope='function')
def users_client():
    print("[FUNCTION] Creating API client for each test")

class TestUserFlow:
    def test_user_can_login(self, settings, user, users_client):
        pass

    def test_user_can_create_course(self, settings, user, users_client):
        pass

class TestAccountFlow:
    def test_user_account(self, settings, user, users_client):
        pass


# Fixture for initializing the client API, executed for each test
@pytest.fixture(scope='function')
def users_client():
    print("[FUNCTION] Creating an API client for each automated test")


class TestUserFlow:
    def test_user_can_login(self, settings, user, users_client):
        pass

    def test_user_can_create_course(self, settings, user, users_client):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, users_client):
        pass





@pytest.fixture(scope="session")
def session_fixture():
    print("\n[SETUP] session_fixture")
    yield
    print("\n[TEARDOWN] session_fixture")

@pytest.fixture(scope="module")
def module_fixture():
    print("\n[SETUP] module_fixture")
    yield
    print("\n[TEARDOWN] module_fixture")

@pytest.fixture(scope="function")
def function_fixture():
    print("\n[SETUP] function_fixture")
    yield
    print("\n[TEARDOWN] function_fixture")

def test_one(session_fixture, module_fixture, function_fixture):
    print("Executing test_one")

def test_two(session_fixture, module_fixture, function_fixture):
    print("Executing test_two")

class TestClass:
    def test_three(self, session_fixture, module_fixture, function_fixture):
        print("Executing test_three")

    def test_four(self, session_fixture, module_fixture, function_fixture):
        print("Executing test_four")

# python -m pytest -k "TestUserFlow or TestAccountFlow" -s -v


# @pytest.fixture(scope="function")
# def function_users_client():
#     print("This fixture will run for each test")
#
# @pytest.fixture(scope="class")
# def class_users_client():
#     print("This fixture will run for each test class")
#
# @pytest.fixture(scope="module")
# def module_users_client():
#     print("This fixture will run for each Python module")
#
# @pytest.fixture(scope="session")
# def session_users_client():
#     print("This fixture will run once for the entire test session")
#
#
# import pytest
#
# @pytest.fixture
# def setup_teardown():
#     # This is the Setup part — code that runs before the test
#     print("Setup: Initializing data or environment")
#     test_data = {"user": "testuser", "password": "testpass"}
#
#     # This is the Teardown part — code that runs after the test
#     yield test_data  # Here we return the data for the test
#
#     print("Teardown: Cleaning up data or environment")
#     # Here you can close connections, delete temporary files, etc.
#     # For example, remove created records from the database if any.
#
# def test_login(setup_teardown):
#     # Here setup_teardown will contain the data returned from the fixture
#     assert setup_teardown["user"] == "testuser"
#     assert setup_teardown["password"] == "testpass"
#
#
# import pytest
#
# @pytest.fixture
# # Initialize the fixture with settings. The first fixture prepares settings,
# # creates an object with settings (for example, a server address).
# def settings():
#     return new_settings()
#
# @pytest.fixture
# # the second fixture receives settings from the first one
# def users_client(settings):
#     return new_users_client(settings.host)
#
# # In the test, I use a ready-made users_client, which knows where it is connecting to.
# def test_create_user(users_client):
#     users_client.create_user()