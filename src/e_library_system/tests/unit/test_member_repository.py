import pytest
from uuid import uuid4
from e_library_system.models.member import Member
from e_library_system.services.member_service import MemberService


class MockMemberRepository:

    def __init__(self):
        self.members = []

    def create_member(self, member):
        self.members.append(member)
        return member

    def get_all(self):
        return self.members

    def get_by_id(self, member_id):
        for member in self.members:
            if member.id == member_id:
                return member
        return None

    def get_by_email(self, email):
        for member in self.members:
            if member.email == email:
                return member
        return None

    def update_member(self, member_id, member):
        for i, m in enumerate(self.members):
            if m.id == member_id:
                self.members[i] = member
                return member
        return None

    def delete_member(self, member_id):
        for i, member in enumerate(self.members):
            if member.id == member_id:
                self.members.pop(i)
                return True
        return False


class TestMemberService:

    def test_create_member_success(self):
        repo = MockMemberRepository()
        service = MemberService(repo)
        member = Member(name="Clem Nwafor", email="clem@ceo.com", phone="1234567890")

        result = service.create_member(member)

        assert result.name == "Clem Nwafor"
        assert result.email == "clem@ceo.com"
        assert len(repo.members) == 1

    def test_create_member_duplicate_email(self):
        repo = MockMemberRepository()
        service = MemberService(repo)
        member1 = Member(name="Clem", email="clem@ceo.com")
        member2 = Member(name="Kay", email="clem@ceo.com")
        service.create_member(member1)

        with pytest.raises(ValueError) as e:
            service.create_member(member2)
        assert "email already exists" in str(e.value)

    def test_get_all_members(self):
        repo = MockMemberRepository()
        service = MemberService(repo)
        member1 = Member(name="Clem", email="clem@ceo.com")
        member2 = Member(name="Kay", email="kay@jiji")
        service.create_member(member1)
        service.create_member(member2)

        result = service.get_all_members()

        assert len(result) == 2

    def test_get_member_by_id_success(self):
        repo = MockMemberRepository()
        service = MemberService(repo)
        member = Member(name="Kay", email="kay@jiji")
        created = service.create_member(member)

        result = service.get_member_by_id(created.id)

        assert result.id == created.id
        assert result.name == "Kay"

    def test_get_member_by_id_not_found(self):
        repo = MockMemberRepository()
        service = MemberService(repo)

        with pytest.raises(ValueError) as e:
            service.get_member_by_id(uuid4())
        assert "Member not found" in str(e.value)

    def test_get_member_by_email_success(self):
        repo = MockMemberRepository()
        service = MemberService(repo)
        member = Member(name="Kay", email="kay@jiji")
        service.create_member(member)

        result = service.get_member_by_email("kay@jiji")

        assert result.email == "kay@jiji"
        assert result.name == "Kay"

    def test_update_member_success(self):
        repo = MockMemberRepository()
        service = MemberService(repo)
        member = Member(name="Kay", email="kay@jiji")
        created = service.create_member(member)

        updated = Member(name="Kayode", email="kay@jiji.com")
        result = service.update_member(created.id, updated)

        assert result.name == "Kayode"
        assert result.email == "kay@jiji.com"

    def test_delete_member_success(self):
        repo = MockMemberRepository()
        service = MemberService(repo)
        member = Member(name="Kay", email="kay@jiji")
        created = service.create_member(member)

        result = service.delete_member(created.id)

        assert result is True
        assert len(repo.members) == 0

    def test_delete_member_not_found(self):
        repo = MockMemberRepository()
        service = MemberService(repo)

        with pytest.raises(ValueError) as e:
            service.delete_member(uuid4())
        assert "Member not found" in str(e.value)