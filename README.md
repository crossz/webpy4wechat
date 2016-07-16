# webpy4wechat

Inspired by http://my.oschina.net/yangyanxing/blog/159215

## Features:

1. SAE 环境支持
1. web.py 的 demo
1. 微信"公众号"的基本服务(不包含任何开放平台的功能)

## Notes: 

### 微信
1. 公共号功能 [公共平台]: 默认模板功能 与 自己开发GET/POST的自动回复, 不能并存. 开启认证域, 则会关闭后台模板功能
2. 登陆 [开放平台]: 要添加"网站应用', 这个需要提交资质, 并等待审批. 
2.1 网页授权获取用户基本信息 [ 公众平台的测试账号 ]: 这个不是指网页登陆, 而是公共号内的一些跳转等
2.2 网站应用授权 [开放平台]: 只支持域名, 只支持80端口, 不支持其他端口. 自己起的其他服务, 比如 web.py 就不行了.

### web.py
1. 获取数据
1.1 web.input(),获取url参数，返回值是类似于字典的key-value对,可以用于GET和POST;
1.1 web.data(),获取实体正文，返回值是一个字符串，只能用于POST。

2. 参数 形参: 虽然可以放在 web.input(); 但是为了方便维护, 最好放在 GET(sefl, arg1, arg2)

3. url形式: 
3.1 /?arg1=val1&arg2=val2, 适配 web.input() 返回的 <Storage> 数据类型, 便于更灵活的编程
3.2 RESTful形式, 是正则方式, <Storage> 为空, 需要自己定义更多关于正则的匹配.