import courses_orm

if __name__ == "__main__":
    courses_orm.create_db_and_tables()
    courses_orm.add_course("SQL Basics", 20, True)
    courses_orm.add_course("Legacy System", 10, False)
    active = courses_orm.get_active_courses()
