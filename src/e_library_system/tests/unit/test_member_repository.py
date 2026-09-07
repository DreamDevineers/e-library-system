import pytest
from uuid import uuid4

from e_library_system.models.member import MemberStatus
from e_library_system.dtos.create_member_request import CreateMemberRequest
from e_library_system.services.member_service import MemberService
from mock_member_repository import MockMemberRepository


class TestMemberService:

    def test_register_success(self):
        repo = MockMemberRepository()
        service = MemberService(repo)

        request = CreateMemberRequest(
            first_name="Clem",
            last_name="Nwafor",
            email="clem@ceo.com",
            phone="1234567890",
            password="password123",
            address="Lagos"
        )

        result = service.register(request)

        assert result.first_name == "Clem"
        assert result.last_name == "Nwafor"
        assert result.email == "clem@ceo.com"
        assert len(repo.members) == 1

    def test_register_duplicate_email(self):
        repo = MockMemberRepository()
        service = MemberService(repo)

        request1 = CreateMemberRequest(
            first_name="Clem",
            last_name="Nwafor",
            email="clem@ceo.com",
            phone="1234567890",
            password="password123",
            address="Lagos"
        )

        request2 = CreateMemberRequest(
            first_name="Kay",
            last_name="Olukayode",
            email="clem@ceo.com",
            phone="0987654321",
            password="password123",
            address="Ibadan"
        )

        service.register(request1)

        with pytest.raises(ValueError) as e:
            service.register(request2)

        assert "email already exists" in str(e.value)

    def test_get_all(self):
        repo = MockMemberRepository()
        service = MemberService(repo)

        request1 = CreateMemberRequest(
            first_name="Clem",
            last_name="Nwafor",
            email="clem@ceo.com",
            phone="1234567890",
            password="password123",
            address="Lagos"
        )

        request2 = CreateMemberRequest(
            first_name="Kay",
            last_name="Olukayode",
            email="kay@jiji.com",
            phone="0987654321",
            password="password123",
            address="Ibadan"
        )

        service.register(request1)
        service.register(request2)

        result = service.get_all()

        assert len(result) == 2

    def test_get_by_id_success(self):
        repo = MockMemberRepository()
        service = MemberService(repo)

        request = CreateMemberRequest(
            first_name="Kay",
            last_name="Olukayode",
            email="kay@jiji.com",
            phone="1234567890",
            password="password123",
            address="Lagos"
        )

        created = service.register(request)

        result = service.get_by_id(created.id)

        assert result.id == created.id
        assert result.first_name == "Kay"
        assert result.last_name == "Olukayode"

    def test_get_by_id_not_found(self):
        repo = MockMemberRepository()
        service = MemberService(repo)

        with pytest.raises(ValueError) as e:
            service.get_by_id(uuid4())

        assert "Member not found" in str(e.value)

    def test_get_by_email_success(self):
        repo = MockMemberRepository()
        service = MemberService(repo)

        request = CreateMemberRequest(
            first_name="Kay",
            last_name="Olukayode",
            email="kay@jiji.com",
            phone="1234567890",
            password="password123",
            address="Lagos"
        )

        service.register(request)

        result = service.get_by_email("kay@jiji.com")

        assert result.email == "kay@jiji.com"
        assert result.first_name == "Kay"

    def test_update_success(self):
        repo = MockMemberRepository()
        service = MemberService(repo)

        request = CreateMemberRequest(
            first_name="Kay",
            last_name="Olukayode",
            email="kay@jiji.com",
            phone="1234567890",
            password="password123",
            address="Lagos"
        )

        created = service.register(request)

        updated_request = CreateMemberRequest(
            first_name="Kayode",
            last_name="Olukayode",
            email="kayode@jiji.com",
            phone="0987654321",
            password="newpassword",
            address="Ibadan"
        )

        result = service.update(created.id, updated_request)

        assert result.first_name == "Kayode"
        assert result.last_name == "Olukayode"
        assert result.email == "kayode@jiji.com"
        assert result.phone == "0987654321"
        assert result.address == "Ibadan"

    def test_disable_member(self):
        repo = MockMemberRepository()
        service = MemberService(repo)

        request = CreateMemberRequest(
            first_name="Kay",
            last_name="Olukayode",
            email="kay@jiji.com",
            phone="1234567890",
            password="password123",
            address="Lagos"
        )

        created = service.register(request)
        service.disable(created.id)
        assert created.status == MemberStatus.DISABLED

    def test_enable_member(self):
        repo = MockMemberRepository()
        service = MemberService(repo)

        request = CreateMemberRequest(
            first_name="Kay",
            last_name="Olukayode",
            email="kay@jiji.com",
            phone="1234567890",
            password="password123",
            address="Lagos"
        )

        created = service.register(request)

        service.disable(created.id)
        service.enable(created.id)

        assert created.status == MemberStatus.ACTIVE

    def test_is_active(self):
        repo = MockMemberRepository()
        service = MemberService(repo)

        request = CreateMemberRequest(
            first_name="Kay",
            last_name="Olukayode",
            email="kay@jiji.com",
            phone="1234567890",
            password="password123",
            address="Lagos"
        )

        created = service.register(request)

        assert service.is_active(created.id) is True
        service.disable(created.id)
        assert service.is_active(created.id) is False