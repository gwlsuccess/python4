from redis import StrictRedis
class Config:

    DEBUG=True
    # 设置密钥
    SECRET_KEY = 'heyKyqaUgg8jAJJvjwxy3bUCkBFBX5ao3kK0HLptbW8='

    # 设置数据库连接
    SQLALCHEMY_DATABASE_URL='mysql://root:mysql@localhost/test3'
    # 配置数据库的动态追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis的主机和端口
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 使用redis来保存session信息
    SESSION_TYPE = 'redis'
    # 对象session信息进行签名
    SESSION_USE_SIGNER = True
    # 存储session的redis实例
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 指定session的过期时间1天
    PERMANENT_SESSION_LIFETIME = 86400
class developmentConfig(Config):
    DEBUG = True
class productionConfig(Config):
    DEBUG = False

my_dict={
    'development':developmentConfig,
    'production':productionConfig
}