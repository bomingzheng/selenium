# 登录测试数据

# 正常登陆
win_data = {'user': '13825161923', 'pwd': 'lemon123'}
unusual_data = [{'user': '1382516192', 'pwd': 'lemon123', 'except': '请输入正确的手机号'},
                {'user': '138251619231', 'pwd': 'lemon123', 'except': '请输入正确的手机号'},
                {'user': '11382516192', 'pwd': 'lemon123', 'except': '请输入正确的手机号'},
                {'user': '', 'pwd': 'lemon123', 'except': '请输入手机号'},
                {'user': '13825161923', 'pwd': '', 'except': '请输入密码'}]
pwd_error_data = [{'user': '14725800852', 'pwd': 'lemon123', 'except': '此账号没有经过授权，请联系管理员!'},
                  {'user': '13825161923', 'pwd': 'lemon111', 'except': '帐号或密码错误!'}]

