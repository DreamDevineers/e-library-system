from uuid import UUID
from typing import Optional

from e_library_system.models.member import Member, MemberStatus
from e_library_system.repositories.member_repository import MemberRepository
from e_library_system.database import Database


class MemberRepositoryImpl(MemberRepository):

    def __init__(self):
        self.db = Database()
        self.db.connect()

    def save(self, member_id: str, data: Member) -> Member:

        query = """
                INSERT INTO members
                (id, first_name, last_name, email, password, phone, address, status, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    first_name = %s,
                    last_name = %s,
                    email = %s,
                    password = %s,
                    phone = %s,
                    address = %s,
                    status = %s
                """

        values = (
            member_id,
            data.first_name,
            data.last_name,
            data.email,
            data.password,
            data.phone,
            data.address,
            data.status.value,
            data.created_at,

            data.first_name,
            data.last_name,
            data.email,
            data.password,
            data.phone,
            data.address,
            data.status.value
        )

        self.db.cursor.execute(query, values)
        self.db.connection.commit()

        return data

    def find_all(self) -> list[Member]:

        query = "SELECT * FROM members"

        self.db.cursor.execute(query)
        results = self.db.cursor.fetchall()

        members = []

        for row in results:
            members.append(
                Member(
                    id=UUID(row["id"]),
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    email=row["email"],
                    password=row["password"],
                    phone=row["phone"],
                    address=row["address"],
                    status=MemberStatus(row["status"]),
                    created_at=row["created_at"]
                )
            )

        return members

    def find_by_id(self, member_id: str) -> Optional[Member]:

        query = "SELECT * FROM members WHERE id = %s"

        self.db.cursor.execute(query, (member_id,))
        row = self.db.cursor.fetchone()

        if row is None:
            return None

        return Member(
            id=UUID(row["id"]),
            first_name=row["first_name"],
            last_name=row["last_name"],
            email=row["email"],
            password=row["password"],
            phone=row["phone"],
            address=row["address"],
            status=MemberStatus(row["status"]),
            created_at=row["created_at"]
        )

    def find_by_email(self, email: str) -> Optional[Member]:

        query = "SELECT * FROM members WHERE email = %s"

        self.db.cursor.execute(query, (email,))
        row = self.db.cursor.fetchone()

        if row is None:
            return None

        return Member(
            id=UUID(row["id"]),
            first_name=row["first_name"],
            last_name=row["last_name"],
            email=row["email"],
            password=row["password"],
            phone=row["phone"],
            address=row["address"],
            status=MemberStatus(row["status"]),
            created_at=row["created_at"]
        )

    def find_by_status(self, status: str) -> list[Member]:

        query = "SELECT * FROM members WHERE status = %s"

        self.db.cursor.execute(query, (status,))
        results = self.db.cursor.fetchall()

        members = []

        for row in results:
            members.append(
                Member(
                    id=UUID(row["id"]),
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    email=row["email"],
                    password=row["password"],
                    phone=row["phone"],
                    address=row["address"],
                    status=MemberStatus(row["status"]),
                    created_at=row["created_at"]
                )
            )

        return members

    def disable(self, member_id: str) -> None:

        query = """
                UPDATE members
                SET status = %s
                WHERE id = %s
                """

        self.db.cursor.execute(
            query,
            (MemberStatus.DISABLED.value, member_id)
        )

        self.db.connection.commit()

    def enable(self, member_id: str) -> None:

        query = """
                UPDATE members
                SET status = %s
                WHERE id = %s
                """

        self.db.cursor.execute(
            query,
            (MemberStatus.ACTIVE.value, member_id)
        )

        self.db.connection.commit()

    def find_active(self) -> list[Member]:

        return self.find_by_status(MemberStatus.ACTIVE.value)

    def count_active(self) -> int:

        query = """
                SELECT COUNT(*) AS total
                FROM members
                WHERE status = %s
                """

        self.db.cursor.execute(
            query,
            (MemberStatus.ACTIVE.value,)
        )

        row = self.db.cursor.fetchone()

        return row["total"]