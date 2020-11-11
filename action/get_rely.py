from utils.db_handler import DB
from utils.md5_encrypt import md5_encrypt

class GetRely(object):
    def __init__(self):
        pass

    @classmethod
    def get(cls,data_source,rely_data,header_source = {}):
        data = data_source.copy()
        db = DB()
        # excel中RelyData格式
        # {
        #     "request": {"username": "register->1", "password": "register->1"},
        #     "response": {"userid": "login->1", "token": "login->1"}
        #  }

        # rely_data = {"request": {"用户注册->1": ["username", "password"]}}
        # store_rely_data = {
        #     "request": {"用户注册": {"1": {"username": "zhangsan123", "password": "zhagn123zhagn"}, "headers": {"cookie": "asdfwerw"}}},
        #     "response": {"用户注册": {"1": {"code": "00"}, "headers": {"age": 2342}}}}
        for key,value in rely_data.items():
            for k,v in value.items():
                api_name, case_id = k.split("->")
                api_id = db.get_api_id(api_name)
                # 从interface_data_store获取data_store存到store_rely_data
                store_rely_data = db.get_rely_data(api_id,case_id)
                # 从store_rely_data遍历,替换成最新的请求参数
                for i in v:
                    if key == "request":
                        if i in store_rely_data["request"][api_name][int(case_id)]:
                            if i == "password":
                                password = md5_encrypt(store_rely_data["request"][api_name][int(case_id)][i])
                                data[i] = password
                            else:
                                data[i] = store_rely_data["request"][api_name][int(case_id)][i]
                    elif key == "response":
                        if i in store_rely_data["response"][api_name][int(case_id)]:
                            data[i] = store_rely_data["response"][api_name][int(case_id)][i]
        return data

if __name__ == '__main__':
    data_source = {"username":"123","password":"123", "code":"01"}
    # rely_data = {"request":{"username":"用户注册->1","password":"用户注册->1"}} #excel的格式
    rely_data = {"request": {"用户注册->1": ["username", "password"]}, "response": {"用户注册->1": ["code"]}}
    data = GetRely.get(data_source,rely_data)
    print(data)


