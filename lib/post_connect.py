import psycopg2
import os


class PostDBConnect:
    def __init__(self) -> None:
        self.drive = psycopg2
        self.connection = None
        self.cursor = None

    def openConnection(self):
        try:
            print("Connecting DB")
            self.connection = self.drive.connect(
                dbname=os.environ["SQL_DB"],
                user=os.environ["SQL_USER"],
                password=os.environ["SQL_PASSWORD"],
                host=os.environ["SQL_HOST"],
                port=os.environ["SQL_POR"]
            )
        except (Exception, self.drive.errors) as error:
            if self.connection:
                print("Failed to connect to the Database", error)
