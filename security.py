import bcrypt
import re


def hash_password(password: str) -> str:
    """
    Hash a plain-text password using bcrypt.
    """

    password_bytes = password.encode("utf-8")

    hashed_password = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    )

    return hashed_password.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify a password against its bcrypt hash.
    """

    password_bytes = password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")

    return bcrypt.checkpw(password_bytes, hashed_bytes)


def is_strong_password(password: str) -> bool:
    """
    Validate password strength requirements.
    """

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[@$!%*?&]", password):
        return False

    return True

if __name__ == "__main__":
    password = "StrongPass123!"

    hashed = hash_password(password)

    print("Hashed Password:")
    print(hashed)

    print("\nVerification:")
    print(verify_password(password, hashed))