import os
# 整个项目的根目录绝对路径
baseDir = os.path.dirname(os.path.dirname(__file__))

# 数据库配置文件绝对路径
config_path = baseDir + "/config/db_config.ini"

log_file_path = baseDir + "/config/Logger.conf"