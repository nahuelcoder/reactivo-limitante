# -*- coding: utf-8 -*-
# reactivos/database.py


"""Este módulo genera la conexión con la base de datos"""


from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def _createContactsTable():

    """Create the contacts table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS elementos (
            nombre VARCHAR(40) PRIMARY KEY UNIQUE NOT NULL,
            Z INTEGER UNIQUE NOT NULL,
            A INTEGER NOT NULL
        )
        """
    )


def createConnection(databaseName):

    """Crea y abre la conexión con la base de datos."""

    connection = QSqlDatabase.addDatabase("QSQLITE")

    connection.setDatabaseName(databaseName)

    if not connection.open():

        QMessageBox.warning(

            None,

            "RP Contact",

            f"Database Error: {connection.lastError().text()}",

        )

        return False

    _createContactsTable()
    return True
