from datetime import timedelta, date
from uuid import uuid4

from e_library_system.models.loan import Loan
from e_library_system.repositories.loan_repository_impl import LoanRepositoryImpl


class TestLoanRepository:

    def setup_method(self):
        self.repository = LoanRepositoryImpl()

    def test_that_loan_repository_saves_loan(self):
        member_id = uuid4()
        book_id = uuid4()

        loan = Loan(
            member_id = member_id,
            book_id = book_id,
            loan_date = date.today(),
            due_date = (date.today() + timedelta(days = 2)),
            status = Loan.LoanStatus.ACTIVE,
        )

        result = self.repository.create_loan(loan)

        assert result == loan