# Burp-Suite-collections

#### BurpSuite 相关收集项目

#### 起因

前阵子在**先知**上有朋友发了一个汉化的教程，但是需要手动输入这些命令而且还容易出错，故，我在此基础上写了个一键自动生成桌面快捷方式加上汉化启动。先上图各位看看效果：

![BurpSuite破解版汉化脚本.gif](https://raw.githubusercontent.com/Mr-xn/Burp-Suite-collections/master/BurpSuite%E7%A0%B4%E8%A7%A3%E7%89%88%E6%B1%89%E5%8C%96%E8%84%9A%E6%9C%AC.gif)

##### 使用方法：

只针对 `Windows` 而言：直接 `Download` 项目所有文件 双击 `创建桌面快捷方式.bat` 即可自动创建桌面快捷方式：<img src="https://raw.githubusercontent.com/Mr-xn/Burp-Suite-collections/master/Goescat-Macaron-Burp-suite.ico" width="32" height ="32" align=right />

如果需要替换图标，要么名字和现在的一样，要么就修改 `创建桌面快捷方式.bat` 里面大约 48 行的 图标名字:

```set icon=%~dp0Goescat-Macaron-Burp-suite.ico``` 将其中的 `%~dp0` 后的 `Goescat-Macaron-Burp-suite.ico` 换成自己喜欢的图标的名字。(此举针对小白)

##### 文件列表

```

> +--- Burp_Suite_Pro_v1.7.37_Loader_Keygen_Chinese_Support
> |   +--- burp-loader-keygen.jar
> |   +--- BurpSuiteCn.jar
> |   +--- burpsuite_pro_v1.7.37.jar
> |   +--- burpsuite实战指南.pdf
> |   +--- BurpSuite破解版汉化脚本.gif
> |   +--- Burp_start.bat
> |   +--- cn.txt
> |   +--- Goescat-Macaron-Burp-suite.ico
> |   +--- Mrxn's Blog.url
> |   +--- plugins
> |   |   +--- burp-vulners-scanner-1.2.jar
> |   |   +--- bypasswaf.jar
> |   |   +--- chunked-coding-converter.0.2.1.jar
> |   |   +--- sqlmap.jar
> |   +--- plugins.png
> |   +--- 创建桌面快捷方式.bat
> |   +--- 吾爱破解论坛.url


```
##### 插件目录 plugins 介绍:

![plugins](https://raw.githubusercontent.com/Mr-xn/Burp-Suite-collections/master/plugins.png)

burp-vulners-scanner-1.2.jar --- burp 根据Vulners.com提供的漏洞库扫描通过burp的请求是否存在漏洞  

地址：https://github.com/vulnersCom/burp-vulners-scanner 

bypasswaf.jar 就如其名bypass 一些waf 

地址：https://www.codewatch.org/blog/?p=408 

chunked-coding-converter.0.2.1.jar 国人c0ny1最新版 burp分块输出，也是对抗waf的插件 

地址：https://github.com/c0ny1/chunked-coding-converter 

sqlmap.jar 联合本地sqlmap 进行注入测试，当然burp插件商店上还有一款 sqli-py(地址：https://github.com/portswigger/sqli-py)可以直接安装就不叙述了

#### 相关教程书籍：

Burp Suite 实战指南 (在线版本)：https://t0data.gitbooks.io/burpsuite/content/ 

Burp Suite新手指南 https://www.freebuf.com/articles/web/100377.html

还有项目里面的:  **burpsuite实战指南.pdf**

#### Tips

欢迎各位补充！

##### 注意：禁止使用本项目所有软件及其文章等资源进行非法测试！

