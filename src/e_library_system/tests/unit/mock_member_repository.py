from e_library_system.models.member import MemberStatus


class MockMemberRepository:

    def __init__(self):
        self.members = []

    def save(self, member_id, data):
        for index, member in enumerate(self.members):
            if str(member.id) == str(data.id):
                self.members[index] = data
                return data

        self.members.append(data)
        return data

    def find_all(self):
        return self.members

    def find_by_id(self, member_id):
        for member in self.members:
            if str(member.id) == str(member_id):
                return member
        return None

    def find_by_email(self, email):
        for member in self.members:
            if member.email == email:
                return member
        return None

    def find_by_status(self, status):
        return [
            member for member in self.members
            if member.status.value == status
        ]

    def disable(self, member_id):
        member = self.find_by_id(member_id)

        if member:
            member.status = MemberStatus.DISABLED

    def enable(self, member_id):
        member = self.find_by_id(member_id)

        if member:
            member.status = MemberStatus.ACTIVE

    def find_active(self):
        return self.find_by_status(MemberStatus.ACTIVE.value)

    def count_active(self):
        return len(self.find_active())