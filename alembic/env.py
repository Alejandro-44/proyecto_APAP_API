from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy.engine.url import URL
from alembic import context
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")

# Configuración de Alembic
config = context.config

# Reemplazar la URL de la base de datos en runtime
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Configuración de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importa los modelos de SQLAlchemy
from app.models import Base  # Ajusta esta línea según la estructura de tu proyecto

# Establecer los metadatos del modelo
target_metadata = Base.metadata

def run_migrations_offline():
    """Ejecutar migraciones en modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Ejecutar migraciones en modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
