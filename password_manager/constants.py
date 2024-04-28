from typing import TypedDict

RECORD_EXTENSION = ".bin"
VAULT_EXTENSION = ".sccv"
SIGNED_AT = "SIGNED_AT"
SIGNED_VAULT_NAME = "SIGNED_VAULT_NAME"
SIGNED_VAULT_PASSWORD = "SIGNED_VAULT_PASSWORD"


class PasswordStrength(TypedDict):
    STRONG: str
    MEDIUM: str
    WEAK: str


PWD_STRENGTH: PasswordStrength = dict(
    STRONG="strong",
    MEDIUM="medium",
    WEAK="weak",
)

