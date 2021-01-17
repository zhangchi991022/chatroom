# coding=utf-8
# 代码文件：chapter24/ChatRoom/com/zhijieketang/qq/client/login_frame.py

"""用户登录窗口"""
import json

from com.zhijieketang.qq.client.friends_frame import FriendsFrame
from com.zhijieketang.qq.client.my_frame import *
from com.zhijieketang.qq.client.reg_frame import RegFrame


class LoginFrame(MyFrame):
    def __init__(self):
        super().__init__(title='账号登录', size=(750, 500))  # 决定窗口大小

        # self.contentpanel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)

        # 创建顶部图片
        # topimage = wx.Bitmap('resources/images/123.jpg', wx.BITMAP_TYPE_JPEG)
        # topimage_sb = wx.StaticBitmap(self.contentpanel, bitmap=topimage,size=(50,250))

        # 设置顶部图片大小格式
        topimage = wx.Image('resources/images/1234.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        topimage_sb = wx.StaticBitmap(self.contentpanel, -1, topimage, pos=(10, 10),
                                      size=(750, 300))  # 决定了初始topimage_sb的大小
        topimage_sb.SetBackgroundColour("#a8a8a8")

        def resizeBitmap(image, width, height):
            bmp = image.Scale(width, height).ConvertToBitmap()
            return bmp

        img_ori = wx.Image('resources/images/login_bg.jpg', wx.BITMAP_TYPE_JPEG)
        topimage_sb.SetBitmap(resizeBitmap(img_ori, 750, 300))  # 重新调整图片的大小但是不能超过初始值

        # 创建界面控件
        middlepanel = wx.Panel(self.contentpanel)
        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)  # 字体设置  panel
        middlepanel.SetFont(font)
        middlepanel.SetBackgroundColour("white")

        accountid_st = wx.StaticText(middlepanel, label='QQ号码', )
        # font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL,False)
        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, faceName='微软雅黑')
        accountid_st.SetFont(font)

        password_st = wx.StaticText(middlepanel, label='QQ密码')
        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, faceName='微软雅黑')
        password_st.SetFont(font)

        self.accountid_txt = wx.TextCtrl(middlepanel, -1, u'', pos=(180, 25), size=(150, 25))  # ----------有问题
        # self.accountid_txt.SetForegroundColour('gray')             #-------------框样式
        self.password_txt = wx.TextCtrl(middlepanel, style=wx.TE_PASSWORD, size=(150, 25))

        # st = wx.StaticText(middlepanel, label='忘记密码？')           #----暂时未设置

        CheckBox = wx.CheckBox(middlepanel, -1, '隐身登录')
        font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, faceName='微软雅黑')
        CheckBox.SetFont(font)

        # 创建FlexGrid布局fgs对象
        fgs = wx.FlexGridSizer(3, 2, 5, 5)  # FlexGridSizer(rows, cols, vgap, hgap)
        fgs.AddMany([(accountid_st, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.FIXED_MINSIZE),  # QQ号码 StaticText
                     (self.accountid_txt, 1, wx.CENTER),  # QQ号码 TextCtrl
                     # wx.StaticText(middlepanel),                              #可用来占格

                     (password_st, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.FIXED_MINSIZE),
                     (self.password_txt, 1, wx.CENTER),
                     # (st, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.FIXED_MINSIZE),
                     # wx.StaticText(middlepanel),
                     wx.StaticText(middlepanel),
                     (CheckBox, 1, wx.CENTER | wx.EXPAND)])
        # (wx.CheckBox(middlepanel, -1, '自动登录'), 1, wx.CENTER | wx.EXPAND)
        # 自动登陆和隐身登录

        # 设置FlexGrid布局对象
        fgs.AddGrowableRow(0, 1)
        fgs.AddGrowableRow(1, 1)
        fgs.AddGrowableCol(0, 1)
        fgs.AddGrowableCol(1, 1)
        # fgs.AddGrowableCol(2, 1)

        panelbox = wx.BoxSizer()
        panelbox.Add(fgs, -1, wx.CENTER | wx.ALL | wx.EXPAND, border=0)  # panelbox border
        middlepanel.SetSizer(panelbox)

        # 创建按钮对象
        okb_btn = wx.Button(parent=self.contentpanel, label='登录', size=(5, 5))  # --------size??
        self.Bind(wx.EVT_BUTTON, self.okb_btn_onclick, okb_btn)
        okb_btn.SetBackgroundColour("white")
        okb_btn.SetForegroundColour("black")

        # cancel_btn = wx.Button(parent=self.contentpanel, label='取消')
        # self.Bind(wx.EVT_BUTTON, self.cancel_btn_onclick, cancel_btn)

        # 创建水平Box布局hbox对象
        hbox = wx.BoxSizer(wx.HORIZONTAL)  # hbox是最底下的那部分
        reg_btn = wx.Button(parent=self.contentpanel, label='申请号码↓')
        reg_btn.SetBackgroundColour("white")
        reg_btn.SetForegroundColour("black")
        self.Bind(wx.EVT_BUTTON, self.reg_btn_onclick, reg_btn)  # 绑定button 申请号码

        # self.Bind(wx.EVT_BUTTON, self.cancel_btn_onclick, cancel_btn)
        hbox.Add(okb_btn, 1, wx.CENTER | wx.ALL | wx.EXPAND, border=20)  # ---控制按钮整体大小
        hbox.Add(reg_btn, 1, wx.CENTER | wx.ALL | wx.EXPAND, border=20)
        # hbox.Add(cancel_btn, 1, wx.CENTER | wx.ALL | wx.EXPAND, border=10)

        vbox = wx.BoxSizer(wx.VERTICAL)  # 创建垂直Box布局对象
        vbox.Add(topimage_sb, -1, wx.CENTER | wx.EXPAND)
        vbox.Add(middlepanel, -1, wx.CENTER | wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox, -1, wx.CENTER | wx.BOTTOM, border=0)  # --也可以控制最下面按钮大小

        self.contentpanel.SetSizer(vbox)
        self.contentpanel.SetBackgroundColour("white")  # 设置整背景颜色

    def okb_btn_onclick(self, event):
        """确定按钮事件处理"""

        account = self.accountid_txt.GetValue()
        password = self.password_txt.GetValue()
        user = self.login(account, password)

        if user is not None:
            logger.info('登录成功。')
            next_frame = FriendsFrame(user)
            next_frame.Show()
            self.Hide()
        else:
            logger.info('登录失败。')
            dlg = wx.MessageDialog(self, '您QQ号码或密码不正确',
                                   '登录失败',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()

    def reg_btn_onclick(self, event):
        next_frame = RegFrame()
        next_frame.Show()

    def cancel_btn_onclick(self, event):
        """取消按钮事件处理"""

        # 退出系统
        self.Destroy()
        sys.exit(0)

    def login(self, userid, password):
        """客户端向服务器发送登录请求"""

        json_obj = {}
        json_obj['command'] = COMMAND_LOGIN
        json_obj['user_id'] = userid
        json_obj['user_pwd'] = password

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
            return json_obj

        # 设置背景图片

    def OnEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()

        # 重新设置图片大小函数
        def resizeBitmap(image, width, height):
            bmp = image.Scale(width, height).ConvertToBitmap()
            return bmp

        image = wx.Image("resources/images/login_bg.jpg", wx.BITMAP_TYPE_ANY)  # 加载图片
        bmp = resizeBitmap(image, 750, 500)  # 重置大小
        dc.DrawBitmap(bmp, 0, 0)  # 需要传入Bitmap对象用来显示
