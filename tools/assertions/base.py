from typing import Any

def assert_status_code(actual: int, expected: int):
    """
    Verifies that the actual response status code matches the expected one.

    :param actual: The actual response status code.
    :param expected: The expected status code.
    :raises AssertionError: If the status codes do not match
    """
    assert actual == expected, (
        f'Incorrect response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}'
    )


def assert_equal(actual: Any, expected: Any, name: str):
    """
    Verifies that the actual value is equal to the expected value.

    :param name: Name of the value being checked.
    :param actual: The actual value.
    :param expected: The expected value.
    :raises AssertionError: If the actual value does not match the expected value.
    """
    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected value: {expected}. '
        f'Actual value: {actual}'
    )

def assert_is_true(actual: Any, name: str):
    """
    Verifies that the actual value is true.

    :param name: Name of the value being checked.
    :param actual: The actual value.
    :raises AssertionError: If the actual value is false.
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )