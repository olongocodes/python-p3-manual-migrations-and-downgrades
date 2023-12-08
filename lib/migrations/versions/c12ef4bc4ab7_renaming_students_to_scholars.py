"""Renaming students to scholars

Revision ID: c12ef4bc4ab7
Revises: 791279dd0760
Create Date: 2023-12-08 12:27:14.048822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c12ef4bc4ab7'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
