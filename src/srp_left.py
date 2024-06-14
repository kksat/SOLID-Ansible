#!/usr/bin/env python3


class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def save_to_database(self):
        print(f"Saving {self.username} to the database.")

    def send_email(self, subject: str, message: str):
        print(f"Sending email to {self.email}: {subject} - {message}")


user = User("john_doe", "john@example.com")
user.save_to_database()
user.send_email("Welcome", "Thanks for signing up!")
