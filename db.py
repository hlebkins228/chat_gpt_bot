import psycopg2
import pickle
from config import db_host, db_password, db_name, db_user
from config import user_files_path


def db_connect(host=db_host, name=db_name, user=db_user, password=db_password):
    try:
        connection = psycopg2.connect(host=host, user=user, password=password, database=name)
    except Exception as _ex:        # TODO: сделать полноценную обработку ошибок открытия и тд
        print("[INFO] database connection failed: ", _ex)
        return False, _ex
    else:
        return True, connection


def __db_create_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE users(
        id bigint PRIMARY KEY,
        user_login varchar(50) NOT NULL,
        messages_file_name varchar(50) NOT NULL);""")

    connection.commit()

    connection.close()


def db_get_user_filename(connection, user_id):
    cursor = connection.cursor()

    cursor.execute(
        f"""SELECT messages_file_name FROM users WHERE id={user_id};""")

    response = cursor.fetchone()
    if response is None:
        return False, "User not found"
    else:
        return True, response[0]


def db_add_user(connection, user_id, user_login):
    cursor = connection.cursor()

    filename = f"{user_id}.pickle"
    with open(user_files_path + filename, "wb") as file:
        messages_list_init = list()
        pickle.dump(messages_list_init, file)

    cursor.execute(
        f"""INSERT INTO users (id, user_login, messages_file_name) VALUES
                ({user_id}, '{user_login}', '{filename}');""")

    connection.commit()

    return filename


def get_user_messages(filename):
    file_path = user_files_path + filename

    with open(file_path, "rb") as file:
        return pickle.load(file)


def save_user_messages(filename, new_messages_list):
    file_path = user_files_path + filename

    with open(file_path, "wb") as file:
        pickle.dump(new_messages_list, file)


def change_user_model(filename, new_model):
    user_messages = get_user_messages(filename)

    system_role_found = False
    for item in user_messages:
        if item["role"] == "system":
            system_role_found = True
            item["content"] = new_model

    if not system_role_found:
        user_messages.append({"role": "system", "content": new_model})

    save_user_messages(filename, user_messages)


def clear_user_messages(filename):
    file_path = user_files_path + filename

    with open(file_path, "wb") as file:
        messages_empty_list = list()
        pickle.dump(messages_empty_list, file)


def __test(connection):
    cursor = connection.cursor()

    cursor.execute(
        f"""INSERT INTO users (id, user_login, messages_file_name) VALUES
            (123456, 'hleb', 'file.data');"""
    )

    connection.commit()


def __db_print(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")

    print(cursor.fetchall())