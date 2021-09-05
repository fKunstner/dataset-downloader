import os


class Config:
    __conf = {
        "DATA_ROOT": os.path.expanduser(os.path.join("~", "data", "dsdl")),
    }

    @staticmethod
    def get(name):
        return Config.__conf[name]

    @staticmethod
    def set(name, value):
        Config.__conf[name] = value
        return Config

    @staticmethod
    def set_data_root(value):
        Config.set("DATA_ROOT", value)
        return Config
