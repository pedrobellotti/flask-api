"""empty message

Revision ID: 3829c84b03ad
Revises: 
Create Date: 2021-08-21 12:43:42.014195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3829c84b03ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('codigo', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=250), nullable=False),
    sa.Column('razao_social', sa.String(length=250), nullable=False),
    sa.Column('cnpj', sa.String(length=18), nullable=False),
    sa.Column('data_inclusao', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('codigo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cliente')
    # ### end Alembic commands ###
