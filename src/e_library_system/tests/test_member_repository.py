import unittest
from tkinter.font import families

from e_library_system.models.member import Member


class TestMemberRepository(unittest.TestCase):

    def test_create_member(self):
        member = Member(
            name="Olukayode Asemudara",
            email="kay@jiji.com",
            phone="08140673711",
            active=True,
        )

        # result = self.repository.create_member("M001", member)
        #
        # self.assertIsNotNone(result)
        # self.assertEqual(result.id, "M001")
        # self.assertEqual(result.email, "john@example.com")