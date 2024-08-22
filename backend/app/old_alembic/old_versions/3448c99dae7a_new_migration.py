"""New Migration

Revision ID: 3448c99dae7a
Revises: e2412789c190
Create Date: 2024-07-12 03:48:09.303650

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '3448c99dae7a'
down_revision = 'e2412789c190'
branch_labels = None
depends_on = None


def upgrade():
  # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("email", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("full_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("id", sa.int(), nullable=False),
        sa.Column(
            "hashed_password", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_table(
        "item",
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("id", sa.int(), nullable=False),
        sa.Column("title", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("owner_id", sa.int(), nullable=False),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('license', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('model', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('color', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('capacity', sa.int(), nullable=False),
    sa.Column('id', sa.int(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('driver',
    sa.Column('id', sa.int(), nullable=False),
    sa.Column('user_id', sa.int(), nullable=False),
    sa.Column('license', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('car_id', sa.int(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_driver_id'), 'driver', ['id'], unique=False)
    op.create_table('passenger',
    sa.Column('id', sa.int(), nullable=False),
    sa.Column('user_id', sa.int(), nullable=False),
    sa.Column('current_location', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('distination', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('wokring_place', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_passenger_id'), 'passenger', ['id'], unique=False)
    op.create_table('route',
    sa.Column('start_location', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('end_location', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('distance', sa.Float(), nullable=False),
    sa.Column('estimated_time', sa.Date(), nullable=False),
    sa.Column('id', sa.int(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trip',
    sa.Column('current_location', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('distination', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('wokring_place', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.int(), nullable=False),
    sa.Column('driver_id', sa.int(), nullable=False),
    sa.Column('route_id', sa.int(), nullable=False),
    sa.Column('start_time', sa.Date(), nullable=False),
    sa.Column('end_time', sa.Date(), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('status', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_trip_trip_id'), 'trip', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("item")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###
    op.drop_index(op.f('ix_trip_trip_id'), table_name='trip')
    op.drop_table('trip')
    op.drop_table('route')
    op.drop_index(op.f('ix_passenger_id'), table_name='passenger')
    op.drop_table('passenger')
    op.drop_index(op.f('ix_driver_id'), table_name='driver')
    op.drop_table('driver')
    op.drop_table('car')
    # ### end Alembic commands ###
