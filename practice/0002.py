"""
第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
"""
import uuid;
import MySQLdb


class MyTest:
    def generate_code(self):
        keys = [];
        for i in range(200):
            uuid_key = uuid.uuid3(uuid.NAMESPACE_URL, str(uuid.uuid4()));
            keys.append(str(uuid_key).replace("-", ""));
        return keys;

    def __init__(self):
        self.conn = MySQLdb.connect(host="dev.rdsmaster.cnhz.shishike.com", port=3306, user="dev_stf_wt",
                                    passwd="yk0GeXVTboygwmjymR5X", db="calm_dev");

    def store(self, keys):
        # Use function cursor() to open the cursor operation
        cursor = self.conn.cursor();
        cursor.execute("drop table if EXISTS ukey_test");

        # create table
        sql = '''
            create table ukey_test (key_value varchar(200) not null)
        '''
        cursor.execute(sql);
        # insert
        try:
            for i in keys:
                print(i)
                cursor.execute("insert into ukey_test values ('%s')" % (i));
                self.conn.commit();
                print(i + " inserted...")
        except:
            print("errrrrr");
            self.conn.rollback();  # rollback
        finally:
            self.conn.close();


if __name__ == '__main__':
    test = MyTest();
    keys = test.generate_code();
    test.store(keys);
