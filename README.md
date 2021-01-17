# chatroom
即时通讯系统
## 项目简介：

开发一个局域网即时聊天通讯系统，功能涵盖注册，登录，发消息，加好友等，开发环境为python 3.8，主要包括wxPython前端界面设计、多线程socket实现客户端服务器通信、pymysql模块实现数据库连接。



## 模块简介：

1、com文件夹下client文件夹为客户端主要实现部分。add_friend.py：实现加好友功能、chat_frame.py：聊天框架、friends_frame.py：好友界面、login_frame.py：登录界面、reg_frame.py：注册界面、My_frame.py：定义Frame窗口基类。

2、com文件夹下server文件夹为服务器主要实现部分。base_dao.py：读取config.ini里数据库配置信息、user_dao.py：实现用户管理功能，包括处理客户端发来的注册信息、根据用户ID查询用户信息、根据用户ID查询好友信息功能。

3、resources包含系统所用的图片和图标

4、qq_clinet.py：创建登录窗口，进入主事件循环

5、qq_server.py：服务器处理主事件循环
## 运行：

python qq_server.py

python qq_client.py
