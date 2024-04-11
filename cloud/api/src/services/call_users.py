from fastapi import APIRouter, status, HTTPException, Request
from models.user_model import User
from config.db_config import ConfigDB


router = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)


@router.get("/get_users")
def get_users() -> list[dict[str, str | list[str] | int]]:
    DB = ConfigDB()
    cursor = DB.get_db_cursor()
    users = []
    SQL_query = (
        f"SELECT idusers, forename, name, email, role FROM USERS"
    )
    cursor.execute(SQL_query)
    user_data = cursor.fetchall()
    user_data = [dict(row) for row in user_data]
    for user in user_data:
        users.append({"idUsers": user["idusers"], "forename": user["forename"], "name": user["name"], "email": user["email"], "role": user["role"]})
    cursor.close()
    DB.connector.close()
    return users


@router.delete("/del_users/{idUsers}")
def del_users(request: Request, idUsers: str) -> None:
    DB = ConfigDB()
    cursor = DB.get_db_cursor()
    user_role = User().get_current_user_role(request.cookies.get("ICARUS-Login"), cursor)
    if user_role == 1:
        SQL_query = (
            f"DELETE FROM USERS WHERE idusers='{idUsers}'"
        )
        cursor.execute(SQL_query)
        DB.connector.commit()
        cursor.close()
        DB.connector.close()
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid profile.",
        )


@router.post("/update_users/")
def update_users(request: Request, idUsers: str, name: str, forename: str, email: str, role: str) -> None:
    DB = ConfigDB()
    cursor = DB.get_db_cursor()
    user_role = User().get_current_user_role(request.cookies.get("ICARUS-Login"), cursor)
    if user_role == 1 or request.cookies.get("ICARUS-Login") == User().get_user(cursor, id_users=idUsers).cookie:
        # If the request come from a User, he can't set the user_role to Admin.
        # Technically, he can't access the webpage to this, but he can still tinker the request himself.
        if user_role == 2:
            role = 2
        else:
            role = 1 if role == "Admin" else 2
        SQL_query = (
            f"UPDATE USERS SET name = '{name}', forename = '{forename}', email = '{email}', role = '{role}' WHERE idusers = '{idUsers}'"
        )
        cursor.execute(SQL_query)
        DB.connector.commit()
        cursor.close()
        DB.connector.close()
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
