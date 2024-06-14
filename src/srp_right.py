#!/usr/bin/env python3


class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email


class UserRepository:
    def save_to_database(self, user: User):
        print(f"Saving {user.username} to the database.")


class EmailService:
    def send_email(self, user: User, subject: str, message: str):
        print(f"Sending email to {user.email}: {subject} - {message}")


user = User("john_doe", "john@example.com")

user_repository = UserRepository()
email_service = EmailService()

user_repository.save_to_database(user)
email_service.send_email(user, "Welcome", "Thanks for signing up!")
