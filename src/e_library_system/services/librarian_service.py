from uuid import UUID

from e_library_system.models.librarian import Librarian
from e_library_system.repositories.librarian_repository import LibrarianRepository
from e_library_system.repositories.member_repository import MemberRepository
from e_library_system.dtos.login_request import LoginRequest
from e_library_system.dtos.create_librarian_request import CreateLibrarianRequest


class LibrarianService:

    def __init__(
        self,
        librarian_repository: LibrarianRepository,
        member_repository: MemberRepository,
    ):
        self.librarian_repo = librarian_repository
        self.member_repo = member_repository


    def register(self, request: CreateLibrarianRequest) -> Librarian:

        existing = self.librarian_repo.find_by_email(request.email)

        if existing is not None:
            raise ValueError("A librarian with this email already exists")

        librarian = Librarian(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            password=request.password,
            phone=request.phone,
            address=request.address,
        )

        self.librarian_repo.save(librarian)

        return librarian

    def authenticate(self, login_request: LoginRequest) -> Librarian:

        librarian = self.librarian_repo.find_by_email(login_request.email)

        if librarian is None:
            raise ValueError("Invalid email or password")

        if librarian.password != login_request.password:
            raise ValueError("Invalid email or password")

        return librarian


    def get_all(self) -> list[Librarian]:
        return self.librarian_repo.find_all()

    def get_by_id(self, librarian_id: UUID) -> Librarian:

        librarian = self.librarian_repo.find_by_id(str(librarian_id))

        if librarian is None:
            raise ValueError("Librarian not found")

        return librarian

    def get_by_email(self, email: str) -> Librarian:

        librarian = self.librarian_repo.find_by_email(email)

        if librarian is None:
            raise ValueError("Librarian not found")

        return librarian

    def update(self, librarian_id: UUID, request: CreateLibrarianRequest) -> Librarian:

        existing = self.librarian_repo.find_by_id(str(librarian_id))

        if existing is None:
            raise ValueError("Librarian not found")

        updated = Librarian(
            id=librarian_id,
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            password=request.password,
            phone=request.phone,
            address=request.address,
            created_at=existing.created_at,
        )

        self.librarian_repo.update(str(librarian_id), updated)

        return updated

    # def delete(self, librarian_id: UUID) -> None:
    #
    #     existing = self.librarian_repo.find_by_id(str(librarian_id))
    #
    #     if existing is None:
    #         raise ValueError("Librarian not found")
    #
    #     self.librarian_repo.delete(str(librarian_id))

    # Member management

    def disable_member(self, member_id: UUID) -> None:

        member = self.member_repo.find_by_id(str(member_id))

        if member is None:
            raise ValueError("Member not found")

        self.member_repo.disable(str(member_id))

    def enable_member(self, member_id: UUID) -> None:

        member = self.member_repo.find_by_id(str(member_id))

        if member is None:
            raise ValueError("Member not found")

        self.member_repo.enable(str(member_id))
