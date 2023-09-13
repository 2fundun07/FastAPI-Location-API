"""db v1.0

Revision ID: 45505516313f
Revises: 
Create Date: 2023-09-11 10:09:39.127285

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45505516313f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("poi") as alter_table_users_op:
        alter_table_users_op.add_column(
            sa.Column("type", sa.String(255)))



def downgrade() -> None:
    pass
