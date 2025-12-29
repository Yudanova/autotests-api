import pytest
from _pytest.fixtures import SubRequest



# @pytest.mark.parametrize("number", [1, 2, 3, -1])
# def test_numbers(number: int):
#     assert number > 0
#
# # python -m pytest -k "test_numbers" -s -v
#
# @pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
# # # In this case, a list of tuples is used as data
# def test_several_numbers(number: int, expected: int):
#     assert number ** 2 == expected
#
# # python -m pytest -k "test_several_numbers" -s -v
#
# @pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])  # Parameterize by operating system
# @pytest.mark.parametrize("host", [
#     "https://dev.company.com",
#     "https://stable.company.com",
#     "https://prod.company.com"
# ])  # Parameterize by hosts
# def test_multiplication_of_numbers(os: str, host: str):
#     assert len(os + host) > 0
# # python -m pytest -k "test_multiplication_of_numbers" -s -v
#
#
#
# @pytest.mark.parametrize("username, password", [
#     ("user1", "pass1"),
#     ("user2", "pass2"),
#     ("admin", "admin123")
# ])
# def test_login(username, password):
#     assert login(username, password) == "Success"
#
# @pytest.mark.parametrize("value", [
#     pytest.param(1),
#     pytest.param(2),
#     pytest.param(-1, marks=pytest.mark.skip(reason="Negative value")),
# ])
# def test_increment(value):
#     assert increment(value) > 0
#
# @pytest.fixture(params=[value1, value2, value3])
# def fixture_name(request):
#     return request.param
#
# def test_example(fixture_name):
#     assert <some condition>
#
#
#
#
# @pytest.fixture(params=[1000, 2000, 3000])
# def port(request):
#     return request.param
#
# def test_port(port):
#     assert port in [1000, 2000, 3000]
#
# @pytest.mark.parametrize("data", [
#     {"username": "user1", "password": "pass1"},
#     {"username": "user2", "password": "pass2"},
#     {"username": "admin", "password": "admin123"},
# ])
# def test_login(data):
#     assert login(data["username"], data["password"]) == "Success"
#
# @pytest.mark.parametrize("host", ["localhost", "example.com"])
# @pytest.mark.parametrize("port", [1000, 2000, 3000])
# def test_client(host, port):
#     assert client.run_test(host, port) == "Success"
#
# def host(request: SubRequest) -> str:
#     return request.param
#
#
# def test_host(host: str):
#     print(f"Running test on host: {host}")
#
#
# @pytest.mark.parametrize("user", ["Alice", "Zara"])
# class TestOperations:
#     def test_user_with_operations(self, user: str):
#         print(f"User with operations: {user}")
#
#     def test_user_without_operations(self, user: str):
#         print(f"User without operations: {user}")
#
#
# users = {
#     "+70000000011": "User with money on bank account",
#     "+70000000022": "User without money on bank account",
#     "+70000000033": "User with operations on bank account"
# }
#
#
# @pytest.mark.parametrize(
#     "phone_number",
#     users.keys(),
#     ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
# )
# def test_identifiers(phone_number: str):
#     pass
#
# @pytest.mark.parametrize("x", [10, 20])  # ids не указаны → сгенерируются автоматически
# def test_auto_ids(x):
#     pass
#
# @pytest.mark.parametrize("role", ["admin", "user"], ids=["ADMIN", "USER"])
# def test_roles(role):
#     pass
#
# @pytest.mark.parametrize("n", [0, 255], ids=("min", "max"))
# def test_bounds(n):
#     pass
#
# @pytest.mark.parametrize(
#     "params",
#     [(200, {"ok": True}), (400, {"error": "bad"})],
#     ids=lambda p: f"status={p[0]}"
# )
# def test_api(params):
#     ...
# @pytest.mark.parametrize("x", [0, 1, 2], ids=lambda v: "zero" if v == 0 else None)
# def test_mixed_ids(x):
#     ...
#
# @pytest.mark.parametrize(
#     "name",
#     [
#         pytest.param("", id="empty"),
#         pytest.param("x" * 255, id="max-len"),
#     ],
# )
# def test_name(name):
#     ...
#
#
# #User's permissions
# # Example endpoints
# ENDPOINTS = [
# ("GET", "/items"),
# ("POST", "/items"),
# ("DELETE", "/items"),
# ]
#
# # Example roles and expected statuses for actions
# # (you can adapt the logic to your API)
# ROLE_PERMISSIONS = {
# "admin": {"GET": 200, "POST": 201, "DELETE": 204},
# "editor": {"GET": 200, "POST": 201, "DELETE": 403},
# "viewer": {"GET": 200, "POST": 403, "DELETE": 403},
# }
#
# @pytest.mark.parametrize(
# "role,method,endpoint",
# [
# (role, method, endpoint)
# for role in ROLE_PERMISSIONS.keys()
# for method, endpoint in ENDPOINTS
# ]
# )
# def test_role_permissions(role, method, endpoint):
# """
# A general-purpose parameterized test
# that checks role access to various API endpoints.
# """
#
# # Simulate an API call (in reality, you'd use requests, aiohttp, etc.)
# # Here, we simply take the expected result from the dictionary
# expected_status = ROLE_PERMISSIONS[role][method]
#
# # This should be a real API call:
# #
# # response = client.request(method, endpoint, headers={"X-Role": role})
# # assert response.status_code == expected_status
# #
# # For example, we'll create a fake check:
#
# fake_api_status = expected_status # as if the response came like this
# assert fake_api_status == expected_status

# @pytest.mark.parametrize("x", [1, 2, 3])
# @pytest.mark.parametrize("y", [4, 5])
# def test_multiplication(x, y):
#     assert x * y

@pytest.mark.parametrize("user", ["Alice", "Bob"])
class TestUserOperations:
    def test_balance(self, user):
        pass

    @pytest.mark.parametrize("operation", ["deposit", "withdraw"])
    def test_operations(self, user, operation):
        pass

@pytest.mark.parametrize(
    "value",
    [1,
     pytest.param(2, marks=pytest.mark.skip(reason="Not supported")),
     3]
)
def test_example(value):
    pass

@pytest.mark.parametrize(
    "input_value",
    [
        pytest.param(1, marks=pytest.mark.xfail(reason="Known issue with 1")),
        2,
        pytest.param(3, marks=pytest.mark.skip(reason="Feature not implemented for 3")),
    ]
)
def test_function(input_value):
    assert input_value != 1