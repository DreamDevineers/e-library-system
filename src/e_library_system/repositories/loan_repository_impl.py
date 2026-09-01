from ast import List
from idlelib import query
from uuid import UUID

from e_library_system.database import Database
from e_library_system.models.loan import Loan
from e_library_system.repositories.loan_repository import LoanRepository


class LoanRepositoryImpl(LoanRepository):

    def __init__(self):
        self.db = Database()
        self.db.connect()

    def create_loan(self, loan: Loan):
        query = """
                    INSERT INTO loans (loan_id, member_id, book_id, loan_date, due_date, return_date, status)
                    VALUES (%s , %s , %s , %s , %s , %s , %s) \
                """

        values = (
            str(loan.loan_id),
            str(loan.member_id),
            str(loan.book_id),
            loan.loan_date,
            loan.due_date,
            loan.return_date,
            loan.status,

        )

        self.db.cursor.execute(query, values)
        self.db.connection.commit()
        return loan


    def get_all(self):
        query = "SELECT * FROM loans"
        self.db.cursor.execute(query)
        result = self.db.cursor.fetchall()

        loans = []
        for row in result:
            loans.append(Loan(
                loan_id = UUID(row['loan_id']),
                member_id = UUID(row['member_id']),
                book_id = UUID(row['book_id']),
                loan_date = row['loan_date'],
                due_date = row['due_date'],
                return_date = row["return_date"],
                status = row['status'],
            ))

        return loans


    def update(self, loan_id: UUID, loan: Loan):
        query = """
                    UPDATE loans
                    SET  
                        member_id = %s, 
                        book_id = %s, 
                        loan_date = %s,
                        due_date = %s, 
                        return_date = %s, 
                        status = %s
                    WHERE loan_id = %s
                """

        values = (
            str(loan.member_id),
            str(loan.book_id),
            loan.loan_date,
            loan.due_date,
            loan.return_date,
            loan.status,
            str(loan.loan_id)
        )

        self.db.cursor.execute(query, values)
        self.db.connection.commit()
        return self.get_by_id(loan_id)

    def get_by_book_id(self, book_id: UUID):
        query = "SELECT * FROM loans WHERE book_id = %s"
        self.db.cursor.execute(query, (str(book_id),))
        result = self.db.cursor.fetchone()
        if result is None:
            return None
        return Loan(
            loan_id = UUID(result["loan_id"]),
            member_id = UUID(result["member_id"]),
            book_id = UUID(result["book_id"]),
            loan_date = result["loan_date"],
            due_date = result["due_date"],
            return_date=result["return_date"],
            status = result["status"],
        )

    def get_by_id(self, loan_id: UUID):
        query = "SELECT * FROM loans WHERE loan_id = %s"
        self.db.cursor.execute(query, (str(loan_id),))
        result = self.db.cursor.fetchone()
        if result is None:
            return None
        return Loan(
            loan_id = UUID(result["loan_id"]),
            member_id = UUID(result["member_id"]),
            book_id = UUID(result["book_id"]),
            loan_date = result["loan_date"],
            due_date = result["due_date"],
            return_date=result["return_date"],
            status = result["status"],
        )

    def get_by_member_id(self, member_id: UUID):
        query = "SELECT * FROM loans WHERE member_id = %s"
        self.db.cursor.execute(query, (str(member_id),))
        result = self.db.cursor.fetchall()
        loans = []

        for row in result:
            loans.append(Loan(
                loan_id = UUID(row["loan_id"]),
                member_id = UUID(row["member_id"]),
                book_id = UUID(row["book_id"]),
                loan_date = row["loan_date"],
                due_date = row["due_date"],
                return_date = row["return_date"],
                status = row["status"],
            ))

        return loans

    def delete(self, loan_id: UUID):
        query = "DELETE FROM loans WHERE loan_id = %s"
        self.db.cursor.execute(query, (str(loan_id),))
        self.db.connection.commit()
        return self.get_by_id(loan_id)

    def count(self) -> int:
        query = "SELECT COUNT(*) FROM loans"
        self.db.cursor.execute(query)
        result = self.db.cursor.fetchone()
        return result["total"]
