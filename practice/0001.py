"""
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码
（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
import uuid;
def generate_code():
    keys = [];
    for i in range(200):
        uuid_key = uuid.uuid3(uuid.NAMESPACE_URL,str(uuid.uuid4()));
        keys.append(str(uuid_key).replace("-",""));
    return keys;

if __name__ == "__main__":
    print(generate_code())