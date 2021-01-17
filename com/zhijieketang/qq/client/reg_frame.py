import json

from com.zhijieketang.qq.client.my_frame import *


class RegFrame(MyFrame):
    def __init__(self):
        super().__init__(title='注册', size=(500, 430))

        # 创建顶部图片
        # topimage = wx.Bitmap('resources/images/1234.jpg', wx.BITMAP_TYPE_JPEG)
        # topimage_sb = wx.StaticBitmap(self.contentpanel, bitmap=topimage)

        topimage = wx.Image('resources/images/login_bg.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        topimage_sb = wx.StaticBitmap(self.contentpanel, -1, topimage, pos=(10, 10),
                                      size=(500, 220))  # 决定了初始topimage_sb的大小
        topimage_sb.SetBackgroundColour("#a8a8a8")

        def resizeBitmap(image, width, height):
            bmp = image.Scale(width, height).ConvertToBitmap()
            return bmp

        img_ori = wx.Image('resources/images/login_bg.jpg', wx.BITMAP_TYPE_ANY)
        topimage_sb.SetBitmap(resizeBitmap(img_ori, 500, 220))  # 重新调整图片的大小但是不能超过初始值

        # 创建界面控件
        middlepanel = wx.Panel(self.contentpanel, style=wx.BORDER_NONE)

        accountid_st = wx.StaticText(middlepanel, label='邮箱')
        password_st = wx.StaticText(middlepanel, label='账号密码')
        name_st = wx.StaticText(middlepanel, label='用户名')
        self.accountid_txt = wx.TextCtrl(middlepanel)
        self.name_txt = wx.TextCtrl(middlepanel)
        self.password_txt = wx.TextCtrl(middlepanel, style=wx.TE_PASSWORD)

        # 创建FlexGrid布局fgs对象
        fgs = wx.FlexGridSizer(3, 3, 8, 15)
        fgs.AddMany([(accountid_st, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.FIXED_MINSIZE),
                     (self.accountid_txt, 1, wx.CENTER | wx.EXPAND),
                     wx.StaticText(middlepanel),
                     (name_st, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.FIXED_MINSIZE),
                     (self.name_txt, 1, wx.CENTER | wx.EXPAND),
                     wx.StaticText(middlepanel),
                     (password_st, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.FIXED_MINSIZE),
                     (self.password_txt, 1, wx.CENTER | wx.EXPAND),
                     wx.StaticText(middlepanel)])

        # 设置FlexGrid布局对象
        fgs.AddGrowableRow(0, 1)
        fgs.AddGrowableRow(1, 1)
        fgs.AddGrowableCol(0, 1)
        fgs.AddGrowableCol(1, 1)
        fgs.AddGrowableCol(2, 1)

        panelbox = wx.BoxSizer()
        panelbox.Add(fgs, -1, wx.CENTER | wx.ALL | wx.EXPAND, border=10)
        middlepanel.SetSizer(panelbox)

        # 创建按钮对象
        okb_btn = wx.Button(parent=self.contentpanel, label='申请')
        okb_btn.SetBackgroundColour("white")
        okb_btn.SetForegroundColour("black")
        self.Bind(wx.EVT_BUTTON, self.okb_btn_onclick, okb_btn)
        cancel_btn = wx.Button(parent=self.contentpanel, label='取消')
        cancel_btn.SetBackgroundColour("white")
        cancel_btn.SetForegroundColour("black")
        self.Bind(wx.EVT_BUTTON, self.cancel_btn_onclick, cancel_btn)

        # 创建水平Box布局hbox对象
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        hbox.Add(okb_btn, 1, wx.CENTER | wx.ALL | wx.EXPAND, border=10)
        hbox.Add(cancel_btn, 1, wx.CENTER | wx.ALL | wx.EXPAND, border=10)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(topimage_sb, -1, wx.CENTER | wx.EXPAND)
        vbox.Add(middlepanel, -1, wx.CENTER | wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox, -1, wx.CENTER | wx.BOTTOM, border=1)

        self.contentpanel.SetSizer(vbox)
        self.contentpanel.SetBackgroundColour("white")

    def cancel_btn_onclick(self, event):
        """取消按钮事件处理"""

        # 退出系统
        self.Destroy()
        # sys.exit(0)

    def okb_btn_onclick(self, event):
        account = self.accountid_txt.GetValue()
        password = self.password_txt.GetValue()
        name = self.name_txt.GetValue()
        user = self.reg(account, password, name)

    def reg(self, userid, password, name):
        json_obj = {}
        json_obj['command'] = COMMAND_REG
        json_obj['user_id'] = userid
        json_obj['user_pwd'] = password
        json_obj['user_name'] = name

        # JSON编码
        json_str = json.dumps(json_obj)
        # 给服务器端发送数据
        client_socket.sendto(json_str.encode(), server_address)

        # 从服务器端接收数据
        json_data, _ = client_socket.recvfrom(1024)
        # JSON解码
        json_obj = json.loads(json_data.decode())
        logger.info('从服务器端接收数据：{0}'.format(json_obj))

        if json_obj['result'] == '0':
            # 登录成功
            dlg = wx.MessageDialog(self, '该账号成功注册',
                                   '注册成功',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            self.Destroy()
            return json_obj

        if json_obj['result'] == '-1':
            print(1)
            dlg = wx.MessageDialog(self, '该账号已被注册',
                                   '注册失败',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
