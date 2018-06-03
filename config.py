class Config:
    DEBUG=True
    # 设置数据库连接
    SQLALCHEMY_DATABASE_URL='mysql://root:mysql@localhost/test3'
    # 配置数据库的动态追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False