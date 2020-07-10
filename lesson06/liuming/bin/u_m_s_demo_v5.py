#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         u_m_s_demo.py
# Description:  the executable file makes program start running
# Author:       Aaron
# Date:         2019/7/4
# -------------------------------------------------------------------------------


if __name__ == "__main__":
    import os
    import sys
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 把项目目录加入环境变量
    sys.path.append(BASE_DIR)
    from u_m_s_demo.main import main
    main()
