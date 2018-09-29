# encoding: utf-8

# 用来存放映射数据库的命令

from flask_migrate import Migrate, MigrateCommand  # 模型到表的迁移
from flask_script import Manager

from companyServer import app
from exts import db

manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到Manager
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()