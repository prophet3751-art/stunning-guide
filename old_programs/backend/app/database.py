from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1️⃣ Подключение к базе
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # путь к файлу базы
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 2️⃣ Создаём сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3️⃣ База
Base = declarative_base()
