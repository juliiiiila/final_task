from framework.db.common_db_steps import BaseDBSteps
from sqlalchemy import text


class DBSteps(BaseDBSteps):
    def group_creation(self):
        sql = text("""
            insert into public.auth_group (name) values ('test')
            """)
        self.execute(sql)

    # def group_id(self):
    #     sql = """
    #         select name from public.auth_group where name = 'test'
    #         """
    #     return self.fetch_all(sql)

    def get_user(self):
        sql = """
            select username from public.auth_user where username = 'test_user'
            """
        return self.fetch_all(sql)

    def get_user_in_group(self):
        sql = """
            SELECT aug.id FROM public.auth_user au
            left join public.auth_user_groups aug
                on au.id=aug.user_id 
            left join public.auth_group ag
                on ag.id=aug.group_id 
            WHERE au.username in ('test_user')
                and ag.name in ('test')
            """
        return self.fetch_all(sql)

    def user_group_delete(self):
        sql = text("""
            delete from public.auth_user_groups where id = 1
            """)
        self.execute(sql)

    def group_delete(self):
        sql = text("""
            delete from public.auth_group where name = 'test'
            """)
        self.execute(sql)

    def user_delete(self):
        sql = text("""
            delete from public.auth_user where username = 'test_user'
            """)
        self.execute(sql)
