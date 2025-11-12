#def test_check_math():
#   assert 7 * 7 == 49

#def test_check_78():
#    assert 7 * 8 == 56

# ---- will be: 2 passed 1 failed:----
#class User:
#    def __init__ (self) ->None:
#       self.name = 'Ira'
#       self.second_name = 'Matukhno'

#user = User()

#def test_remove_name():
#    user.name = ''
#    assert user.name == ''
#def test_name():
#    assert user.name == 'Ira'

#def test_second_name():
#    assert user.second_name == 'Matukhno'

# -------- Fixture for example above -------
#import pytest
#class User:
#    def __init__(self) ->None:
#        self.name = 'Ira'
#        self.second_name = 'Matukhno'

#@pytest.fixture
#def user():
#    yield User()
#   --code above - to remove: class User and fixture user, because it was added to conftest file (tests) and class User - in 'test_fixtures.py' file
import pytest

@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''

@pytest.mark.check
def test_name(user):
    assert user.name == 'Ira'

@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Matukhno'

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('matukhnoira')
    assert r['message'] == 'Not Found'
# --------------------------

#import pytest
#class User:
#    def __init__ (self) -> None:
#        self.name = None
#        self.second_name = None

#    def create(self):
#        self.name = 'Ira'
#        self.second_name = 'Matukhno'

#    def remove(self):
#        self.name = ''
#        self.second_name = ''

#    def test_change_name():
#        user = User()
#        user.create()

#        assert user.name == 'Ira'
#        user.remove()

#    def test_change_second_name():
#        user = User()
#        user.create()

#        assert user.second_name == 'Ja'
#        user.remove()

# Only TESTS inside the test, a stvorennia i vydalennia - faktyczno ZA testowym scenariem

# import pytest
# class User:
#     def __init__ (self) -> None:
#         self.name = None
#         self.second_name = None

#     def create(self):
#         self.name = 'Ira'
#         self.second_name = 'Ja'

#     def remove(self):
#         self.name = ''
#         self.second_name = ''

# @pytest.fixture
# def user():
#     user = User()
#     user.create()

#     yield user #YIELD - vse, sho DO - wykonaetsia DO testu. Vse, sho PISLIA - wykonaetsia PISLIA testu

#     user.remove()

# def test_change_name(user):
#     assert user.name == 'Ira'

# def test_change_second_name(user):
#     assert user.second_name == 'Ja'