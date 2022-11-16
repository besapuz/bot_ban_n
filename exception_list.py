from connect_db import connect_db

db = connect_db()


def get_except_chat_id(telegram_id):
    try:
        with db.cursor() as cursor:
            # Получить данные
            sql = f"""
                    SELECT except_chat 
                    FROM users 
                    WHERE telegram_id={telegram_id}
                    """
            cursor.execute(sql)
            result = cursor.fetchone()

    except Exception as e:
        return f"Error {e}"

    if result is None:
        return [0]
    else:
        return result


# UPDATE users SET except_chat='{}'::bigint[] WHERE telegram_id=
# SELECT except_chat FROM users WHERE telegram_id=