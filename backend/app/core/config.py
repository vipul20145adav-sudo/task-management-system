from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    app_version: str

    database_url: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    gemini_api_key: str = ""

    email_host: str = ""
    email_port: str = ""
    email_username: str = ""
    email_password: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()