from logging.config import fileConfig

from sqlalchemy import MetaData, engine_from_config, pool

from alembic import context
from db.mysql_conn import DATABASE_URL
from models.config import Base as ConfigBase
from models.dish_ingredient import Base as DishIngredientBase
from models.dish_taste import Base as DishTasteBase
from models.dishes import Base as DishesBase
from models.ingredients import Base as IngredientBase
from models.orders_detail import Base as OrderDetailBase
from models.orders_master import Base as OrderMasterBase
from models.taste import Base as TasteBase
from models.user import Base as UserBase
from models.user_extend import Base as UserExtendBase

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config.set_main_option("sqlalchemy.url", DATABASE_URL)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = MetaData()
for base in [
    ConfigBase,
    DishIngredientBase,
    DishTasteBase,
    DishesBase,
    IngredientBase,
    OrderDetailBase,
    OrderMasterBase,
    TasteBase,
    UserExtendBase,
    UserBase,
]:
    for table in base.metadata.tables.values():
        target_metadata._add_table(table.name, table.schema, table)

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()


# This file is used by Alembic to manage database migrations.
# It sets up the database connection and metadata for the models.
# The `target_metadata` variable is used to specify the metadata for the models
# that Alembic will use to generate migration scripts.
# Firstly, Use alembic init alembic to initial folder.
# Then edit alembic.eny.py
# Use `alembic revision --autogenerate -m "message"` to create a new migration script.
# Use `alembic upgrade head` to apply the latest migrations.
# Use `alembic downgrade -1` to revert the last migration.
