from flask_sqlalchemy import SQLAlchemy

# ORM - object relational mapping
#  helps you connect to multiple DBs (MySQL, MSSQL)
# MSSQL --> MySQL migrating  becomes easier
# no need for RAW - SQL
db = SQLAlchemy()
