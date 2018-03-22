import unittest
from src.Database.PostgresManager import PostgresManager

class DatabaseTest(unittest.TestCase):
	def setUp(self):
		pass
	
	def Test_CheckInitialization(self):
		ps = PostgresManager()
		self.assertIsNotNone(ps.conn)

	def Test_CheckOperationErrorAfterClosing(self):
		ps = PostgresManager()
		ps.close()
		self.assertRaises(ValueError, ps.commit)


if __name__ == '__main__':
	unittest.main()