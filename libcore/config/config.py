#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
from libcore.exception.config_key_not_exist_exception import ConfigKeyNot_ExistException
from libcore.utill.string_utill import StringUtill

class Config:
    """
    配置文件
    """
    __allow_config_keys = (
        'mirror',
        'language',
        'publisher'
    )

    def get(self, key: str) -> str:
        """
        获取配置项
        :param key:
        :return:
        """
        if StringUtill.is_empty(key):
            raise ConfigKeyNot_ExistException("{} is not in config file, because key is empty!".format(key))

        if key not in self.__allow_config_keys:
            raise ConfigKeyNot_ExistException("{} is not in config file, the specified key is illegal.".format(key))

        # TODO 读取配置文件中得 value

        return ""

    def set(self, key: str, value: str) -> bool:
        """
        设置配置项
        :param key:
        :param value:
        :return:
        """

    def get_with_default(self, key: str, default: str):
        """
        获取配置项，如果这个配置为空，则返回 default
        :param key:
        :param default:
        :return:
        """
        pass


if __name__ == "__main__":
    pass
