def test_first_try():
    print("Hello, world")
    #python -m pytest -s -v  to print logs
# python -m pytest -s to print (print("Hello, world"))

def test_second_try():
    pass
# python -m pytest -s -v -k "test_second_try" to run only second test: collected 2 items / 1 deselected / 1 selected

class TestUserLogin:   # run class: python -m pytest -s -v -k "TestUserLogin"
    def test_one(self):
        pass
    def test_two(self):
        pass

# python -m pytest -s -v -k "first and one" - run all tests with the name contents words: first and one. Result: collected 4 items / 4 deselected / 0 selected

# python -m pytest -s -v -k "first or one" - result - collected 4 items / 2 deselected / 2 selected

# python -m pytest -s -v -k "first and not two"  - run all "first" tests except "two". collected 4 items / 3 deselected / 1 selected

def test_assert_positive():
    assert (1+1)==2
def test_assert_negative():
    x,y = 5, 2
    assert (1 + 1) == 5, "..."

# python -m pytest -s -v -k "assert" Res: tests/test_pytest.py::test_assert_positive PASSED
# tests/test_pytest.py::test_assert_negative FAILED
# FAILED tests/test_pytest.py::test_assert_negative - assert (1 + 1) == 5
