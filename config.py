class Config:
    # General pattern
    # mssql+pyodbc://<username>:<password>@<dsn_name>?driver=<driver_name>
    # mssql+pyodbc://@<server_name>/<db_name>?driver=<driver_name>
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://@PF1BTSVQ\SQLEXPRESS/SanlamMovieDB2025?driver=ODBC+Driver+17+for+SQL+Server"
    SQLALCHEMY_MODIFICATION_TRACK = False
