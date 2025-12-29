"""create initial admin user

Revision ID: ffed11304c67
Revises: 918788054f55
Create Date: 2025-12-29 13:36:29.255531

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from app.core.security import hash_password

# revision identifiers, used by Alembic.
revision: str = 'ffed11304c67'
down_revision: Union[str, Sequence[str], None] = '918788054f55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    password_hash = hash_password("1234")

    op.execute(
        f"""
        INSERT INTO users (username, hashed_password)
        SELECT 'admin', '{password_hash}'
        WHERE NOT EXISTS (
            SELECT 1 FROM users WHERE username = 'admin'
        )
        """
    )



def downgrade() -> None:
    op.execute("DELETE FROM users WHERE username = 'admin'")
