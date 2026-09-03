from uuid import UUID
from e_library_system.models.member import Member
from e_library_system.repositories.member_repository import MemberRepository
from e_library_system.database import Database


class MemberRepositoryImpl(MemberRepository):

    def __init__(self):
        self.db = Database()
        self.db.connect()

    def create_member(self, member: Member):
        query = """
                INSERT INTO members (id, name, email, phone, password, joined_at, active)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """

        values = (
            str(member.id),
            member.name,
            member.email,
            member.phone,
            member.password,
            member.joined_at,
            member.active
        )

        self.db.cursor.execute(query, values)
        self.db.connection.commit()

        return member

    def get_all(self):
        query = "SELECT * FROM members"

        self.db.cursor.execute(query)
        results = self.db.cursor.fetchall()

        members = []

        for row in results:
            members.append(
                Member(
                    id=UUID(row['id']),
                    name=row['name'],
                    email=row['email'],
                    phone=row['phone'],
                    password=row['password'],
                    joined_at=row['joined_at'],
                    active=bool(row['active'])
                )
            )

        return members

    def get_by_id(self, member_id: UUID):
        query = "SELECT * FROM members WHERE id = %s"

        self.db.cursor.execute(query, (str(member_id),))
        row = self.db.cursor.fetchone()

        if row:
            return Member(
                id=UUID(row['id']),
                name=row['name'],
                email=row['email'],
                phone=row['phone'],
                password=row['password'],
                joined_at=row['joined_at'],
                active=bool(row['active'])
            )

        return None

    def get_by_email(self, email: str):
        query = "SELECT * FROM members WHERE email = %s"

        self.db.cursor.execute(query, (email,))
        row = self.db.cursor.fetchone()

        if row:
            return Member(
                id=UUID(row['id']),
                name=row['name'],
                email=row['email'],
                phone=row['phone'],
                password=row['password'],
                joined_at=row['joined_at'],
                active=bool(row['active'])
            )

        return None

    def update_member(self, member_id: UUID, member: Member):
        query = """
                UPDATE members
                SET name      = %s,
                    email     = %s,
                    phone     = %s,
                    joined_at = %s,
                    active    = %s
                WHERE id = %s
                """

        values = (
            member.name,
            member.email,
            member.phone,
            member.joined_at,
            member.active,
            str(member_id)
        )

        self.db.cursor.execute(query, values)
        self.db.connection.commit()

        return self.get_by_id(member_id)

    def delete_member(self, member_id: UUID):
        query = "DELETE FROM members WHERE id = %s"

        self.db.cursor.execute(query, (str(member_id),))
        self.db.connection.commit()

        return self.db.cursor.rowcount > 0