# Burp-Suite-collections

#### BurpSuite 相关收集项目

#### 起因

前阵子在**先知**上有朋友发了一个汉化的教程，但是需要手动输入这些命令而且还容易出错，故，我在此基础上写了个一键自动生成桌面快捷方式加上汉化启动。先上图：汉化+桌面快捷方式的一键启动效果：

![BurpSuite破解版汉化脚本.gif](https://raw.githubusercontent.com/Mr-xn/Burp-Suite-collections/master/BurpSuite%E7%A0%B4%E8%A7%A3%E7%89%88%E6%B1%89%E5%8C%96%E8%84%9A%E6%9C%AC.gif)

##### 使用方法：

如果你习惯`【推荐】`英文不想使用汉化版的，直接运行`Create Desktop Link.bat` 即可创建英文版的桌面快捷方式，当然你也可以两个都创建。*(汉化版在某些插件上面会出现各种 **UI** **BUG** ，如果你的 Burp 界面出现了 BUG 请切换英文原版试试)*

只针对 `Windows` 而言：直接 `Download` 项目所有文件 双击 `创建桌面快捷方式.bat` 即可自动创建`汉化版`桌面快捷方式：<img src="https://raw.githubusercontent.com/Mr-xn/Burp-Suite-collections/master/Goescat-Macaron-Burp-suite.ico" width="32" height ="32" align=right />

如果需要替换图标，要么名字和现在的一样，要么就修改 `创建桌面快捷方式.bat` 里面大约 48 行的 图标名字:

```set icon=%~dp0Goescat-Macaron-Burp-suite.ico``` 将其中的 `%~dp0` 后的 `Goescat-Macaron-Burp-suite.ico` 换成自己喜欢的图标的名字。(此举针对小白)

##### 文件列表

```

+--- books
|   +--- 本地文件包含漏洞检测工具 – Burp国产插件LFI scanner checks.pdf
|   +--- Burp Suite使用 _ Pa55w0rd 's Blog.pdf
|   +--- burpsuite实战指南.pdf
|   +--- Configuring Burp Suite with Android Nougat.pdf
|   +--- nmap-man-page.pdf
|   +--- Nmap渗透测试思维导图.png
|   +--- readme.md
|   +--- 利用burp插件Hackvertor绕过waf并破解XOR加密 - 嘶吼 RoarTalk.pdf
+--- burp-loader-keygen.jar
+--- BurpSuiteCn.jar
+--- burpsuite_pro_v1.7.37.jar
+--- BurpSuite破解版汉化脚本.gif
+--- Burp_start.bat
+--- Burp_start_en.bat
+--- cn.txt
+--- Create Desktop Link.bat
+--- GitZip-for-github_v0.3.1.crx
+--- Goescat-Macaron-Burp-suite.ico
+--- Mrxn's Blog.url
+--- plugins
|   +--- burp-vulners-scanner-1.2.jar
|	+--- LFI scanner checks.jar
|   +--- bypasswaf.jar
|   +--- chunked-coding-converter.0.2.1.jar
|   +--- jsEncrypter.0.2
|   |   +--- jsEncrypter.0.2.jar
|   |   +--- jsEncrypter_readme.pdf
|   |   +--- nodejs_server.js
|   |   +--- phantomjs_server.js
|   |   +--- README.md
|   |   +--- 对登录中账号密码进行加密之后再传输的爆破的思路和方式 - FreeBuf互联网安全新媒体平台.pdf
|   |   +--- 编写加密传输爆破插件jsEncrypter _ 回忆飘如雪.pdf
|   +--- Readme.md
|   +--- sqlmap.jar
+--- plugins.png
+--- README.md
+--- 创建桌面快捷方式.bat
+--- 吾爱破解论坛.url

```
##### 插件目录 plugins 介绍:

![plugins](https://raw.githubusercontent.com/Mr-xn/Burp-Suite-collections/master/plugins.png)

LFI scanner checks.jar --- 是国人 [lufei](https://github.com/lufeirider/Project/tree/master/LFIScanner) 为burp轻量级扫描器做的一个检测LFI(Local File Include)本地文件包含漏洞插件。相关文章可以在 [freebuf](https://www.freebuf.com/sectool/75118.html) 看他写的或者是看项目[保存的PDF版](https://github.com/Mr-xn/BurpSuite-collections/blob/master/books/本地文件包含漏洞检测工具 – Burp国产插件LFI scanner checks.pdf) 。

jsEncrypter.0.2 --- jsEncrypter 使用 `phantomjs` 调用前端加密函数对数据进行加密，方便对加密数据输入点进行fuzz

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

还有项目里面的books目录:  [**burpsuite实战指南.pdf等书籍**](https://github.com/Mr-xn/Burp-Suite-collections/tree/master/books)

#### Tips

如果你只想下载本项目的一部分，比如只想下载 **plugins** 目录，那么推荐你在 `Chrome` 浏览器下安装 **[GitZip for github](<https://chrome.google.com/webstore/detail/gitzip-for-github/ffabmkklhbepgcgfonabamgnfafbdlkn>)** 这款插件，安装后，你只需要双击想要下载的目录或者十文件即可单独下载，十分的方便。如果你的网络环境不方便进入 Chrome 商店下载，可以下载本项目里的 [GitZip-for-github_v0.3.1.crx](https://raw.githubusercontent.com/Mr-xn/Burp-Suite-collections/master/GitZip-for-github_v0.3.1.crx) 离线安装包或者是[蓝奏云](https://www.lanzous.com/i3r80dg) 密码:`mrxn` 下载后解压，也可去 [这里](https://chrome-extension-downloader.com/) 输入此插件的ID：`ffabmkklhbepgcgfonabamgnfafbdlkn` 自行下载，安装方法可以参考这里：[Chrome crx插件扩展离线安装方法 (兼容全版本)](https://sspai.com/post/52767)。

欢迎各位补充！

##### 注意：禁止使用本项目所有软件及其文章等资源进行非法测试！

