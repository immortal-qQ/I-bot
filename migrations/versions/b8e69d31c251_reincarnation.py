"""reincarnation

Revision ID: b8e69d31c251
Revises: 
Create Date: 2024-04-15 14:38:22.903407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8e69d31c251'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tg_user',
    sa.Column('tg_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('nickname', sa.String(length=100), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('tg_id')
    )
    op.create_table('parsed_reminder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('remind_at', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['tg_user.tg_id'], name='fk_tg_user_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('started_at', sa.DateTime(), nullable=False),
    sa.Column('finished_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['tg_user.tg_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reminder_org_intersection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reminder_id', sa.Integer(), nullable=True),
    sa.Column('organization_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], name='fk_organization_id'),
    sa.ForeignKeyConstraint(['reminder_id'], ['parsed_reminder.id'], name='fk_parsed_reminder_id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reminder_org_intersection')
    op.drop_table('session')
    op.drop_table('parsed_reminder')
    op.drop_table('tg_user')
    op.drop_table('organization')
    # ### end Alembic commands ###
