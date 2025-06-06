"""Remove unique name restriction on agents

Revision ID: cdb3db091113
Revises: e20573fe9b86
Create Date: 2025-01-10 15:36:08.728539

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "cdb3db091113"
down_revision: Union[str, None] = "e20573fe9b86"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("unique_org_agent_name", "agents", type_="unique")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint("unique_org_agent_name", "agents", ["organization_id", "name"])
    # ### end Alembic commands ###
