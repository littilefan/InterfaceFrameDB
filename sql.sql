/*创建sql*/

# 创建数据库
create database if not exists interface_autotest default charset utf8 collate utf8_general_ci;

# 选择数据库
use interface_autotest;

# api表
create table interface_api(
	api_id int not null auto_increment comment "自增长主键",
	api_name varchar(50) not null comment "接口名称",
	r_url varchar(50) not null comment "请求接口的URL",
    r_method varchar(10) not null comment "接口请求方式",
    p_type varchar(20) not null comment "传参方式",
    status tinyint default 0,
    ctime datetime,
    unique index(api_name),
    primary key(api_id)
)engine=InnoDB default charset=utf8;

# 接口用例表
create table interface_test_case(
    id int not null AUTO_INCREMENT comment "自增长主键",
    api_id int not null comment "对应interface_api的api_id",
    r_data varchar(255) comment "请求接口时传的参数",
    rely_data varchar(255) comment "用例依赖的数据",
    protocol_code int comment "接口期望响应code",
    res_data varchar(255) comment "接口响应body",
    data_store varchar(255) comment "依赖数据存储",
    check_point varchar(255) comment "接口响应校验依据数据",
    status tinyint default 0 comment "用例执行状态，0不执行，1执行",
    error_info varchar(1000) comment "错误信息列",
    ctime datetime,
    primary key(id),
    index(api_id)
)engine=InnoDB default charset=utf8;

# 接口依赖数据存储表
create table interface_data_store(
    api_id int not null comment "对应interface_api的api_id",
    case_id int not null comment "对应interface_test_case里面的id",
    data_store varchar(255) comment "存储的依赖数据",
    ctime datetime,
    index(api_id,case_id)
)engine=InnoDB default charset=utf8;


INSERT INTO `interface_api` VALUES (1, '用户注册', 'http://39.100.104.214:8080/register/', 'post', 'form', '1', '2018-07-27 22:15:57');
INSERT INTO `interface_api` VALUES (2, '用户登录', 'http://39.100.104.214:8080/login/', 'post', 'form', '1', '2018-07-27 22:15:57');
INSERT INTO `interface_api` VALUES (3, '查询博文', 'http://39.100.104.214:8080/getBlogContent/', 'get', 'url','0', '2018-07-27 22:13:30');

INSERT INTO `interface_test_case` VALUES ('1', '1', '{\"username\":\"zhangsan123\",\"password\":\"zhagn123zhagn\",\"email\":\"zs@qq.com\"}', null, '200', '{\'username\': \'zrichudwea1\', \'code\': \'01\'}', '{\"request\":[\"username\",\"password\"],\"response\":[\"code\"]}', '{\"code\":\"00\"}', '1', '{\'code\': \'01\'}', null);
INSERT INTO `interface_test_case` VALUES ('2', '2', '{\"username\":\"lilydsd23\", \"password\":\"ssd32de2\"}', '{\"request\":{\"用户注册->1\":[\"username\",\"password\"]}}', '200', '{\'token\': \'b0ab9d040a95c592db96e42eef237da9\', \'code\': \'00\', \'userid\': 110, \'login_time\': \'2019-11-09 17:24:06\'}', '', '{\"code\":\"00\"}', '1', '', null);

INSERT INTO `interface_data_store` VALUES ('1', '1', '{\"request\":{\"用户注册\":{\"1\":{\"username\":\"zhangsan123\", \"password\":\"zhagn123zhagn\"},\"headers\":{\"cookie\":\"asdfwerw\"}}},\"response\":{\"用户注册\":{\"1\":{\"code\":\"00\"}, \"headers\":{\"age\":2342}}}}\r\n', null);

data_store的格式
{"request":{"用户注册":{"1":{"username":"zhangsan", "password":"dfsdf23"},"headers":{"cookie":"asdfwerw"}}},"response":{"用户注册":{"1":{"code":"00"}, "headers":{"age":2342}}}}

