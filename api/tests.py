import pytest

from api.models import User

@pytest.mark.django_db
def test_my_user():
	count_users = User.objects.all().count()
	assert count_users == 0
