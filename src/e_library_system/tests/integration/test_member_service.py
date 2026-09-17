import pytest

from e_library_system.models.member import MemberStatus
from e_library_system.dtos.create_member_request import CreateMemberRequest
from e_library_system.dtos.login_request import LoginRequest
from e_library_system.services.member_service import MemberService
from e_library_system.repositories.member_repository_impl import MemberRepositoryImpl


@pytest.fixture
def service():
    repo = MemberRepositoryImpl()
    return MemberService(repo)


@pytest.fixture(autouse=True)
def cleanup(service):
    yield
    for member in service.repository.find_all():
        service.repository.db.cursor.execute(
            "DELETE FROM members WHERE id = %s", (str(member.id),)
        )
        service.repository.db.connection.commit()


def make_request(email: str = "kayode@kay.com") -> CreateMemberRequest:
    return CreateMemberRequest(
        first_name="Kayode",
        last_name="Kay",
        email=email,
        phone="1234567890",
        password="password123",
        address="Lagos"
    )


class TestMemberServiceIntegration:

    def test_register_saves_member_to_database(self, service):
        result = service.register(make_request())

        fetched = service.get_by_id(result.id)

        assert fetched is not None
        assert fetched.email == "kayode@kay.com"
        assert fetched.first_name == "Kayode"

    def test_register_duplicate_email_raises_error(self, service):
        service.register(make_request())

        with pytest.raises(ValueError) as e:
            service.register(make_request())

        assert "email already exists" in str(e.value)

    def test_get_all_returns_all_registered_members(self, service):
        service.register(make_request("clement@nwafor.com"))
        service.register(make_request("gbemi@martyg.com"))

        result = service.get_all()

        assert len(result) == 2

    def test_authenticate_with_correct_credentials(self, service):
        service.register(make_request())

        result = service.authenticate(
            LoginRequest(email="kayode@kay.com", password="password123")
        )

        assert result.email == "kayode@kay.com"

    def test_authenticate_with_wrong_password_raises_error(self, service):
        service.register(make_request())

        with pytest.raises(ValueError) as e:
            service.authenticate(
                LoginRequest(email="kayode@kay.com", password="wrongpassword")
            )

        assert "Invalid email or password" in str(e.value)

    def test_disable_and_enable_member_persists_to_database(self, service):
        member = service.register(make_request())

        service.disable(member.id)
        disabled = service.get_by_id(member.id)
        assert disabled.status == MemberStatus.DISABLED

        service.enable(member.id)
        enabled = service.get_by_id(member.id)
        assert enabled.status == MemberStatus.ACTIVE
