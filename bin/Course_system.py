#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
'''
这是系统的入口，其实就算一个项目的接口
'''
import os,sys
base_dir = sys.path.append(os.path.dirname\
                               (os.path.dirname\
                                    (os.path.abspath(__file__))))
from core import main

if __name__ == '__main__':
    main.rum()
