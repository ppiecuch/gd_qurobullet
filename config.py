# config.py


def can_build(env, platform):
    return not env['production']


def configure(env):
    pass


def get_doc_classes():
    return ["Bullet", "BulletType", "BulletSpawner", "BulletServer", "BulletServerRelay"]


def get_doc_path():
    return "doc_classes"
