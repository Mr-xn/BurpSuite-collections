## 在 Mac 下制作成 APP 放在 dock 里一键启动 
> 简单记录下

1. 目录结构大致如下，

```shell
├── BurpLoaderKeygen.jar
├── BurpSuite.icns
├── BurpSuiteLoader.jar
├── active_burp.sh
├── burpsuite_pro_v2021.12.1.jar
├── jdk-17.0.1.jdk
└── start_burp.sh
```

其中 BurpLoaderKeygen.jar 和 BurpSuiteLoader.jar 是激活和加载的工具  
BurpSuite.icns 是图标，一会儿制作成应用程序后改变图标的  
jdk-17.0.1.jdk 是 jdk 的目录，我是用的相对位置的 JAVA 不依赖系统的 JAVA 版本，独立运行的  
burpsuite_pro_v2021.12.1.jar 就是 burpsuite 的本身了  
active_burp.sh 是用来激活的脚本：  
```shell
#!/usr/bin/env bash 
# active burp first

SHELL_FOLDER=$(cd `dirname $0`; pwd)
jdk_path=${SHELL_FOLDER}"/jdk-*.jdk/Contents/Home/bin/java"
${jdk_path} -Xdock:icon=${SHELL_FOLDER}/BurpSuite.icns -jar ${SHELL_FOLDER}/BurpSuiteLoader.jar%
```
> 注意 shell 中的 jdk 路径部分，我是用的泛匹配，如果你有多个 jdk 目录，请自行修改。

start_burp.sh 是启动 burpsuite 的脚本，也是制作成 APP 直接使用的部分：
```shell
#!/usr/bin/env bash 

# start burp en after licensed
SHELL_FOLDER=$(cd `dirname $0`; pwd)
jdk_path=${SHELL_FOLDER}"/jdk-*.jdk/Contents/Home/bin/java"
${jdk_path} -Xdock:icon=${SHELL_FOLDER}/BurpSuite.icns -Dfile.encoding=utf-8 -noverify -javaagent:${SHELL_FOLDER}/BurpSuiteLoader.jar -jar -Xmx8G --add-opens=java.desktop/javax.swing=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED ${SHELL_FOLDER}/burpsuite_pro_v202*.jar
```
需要注意如下几点  
> 第一是 jdk 目录，和上一条一样  
> 第二是 burpsuite 的具体版本号我也是采用的泛匹配，参考上面的目录，有需要自行修改  
> 第三是 -Xmx8G 参数 表示设置堆内存的最大值 8G，可参考下表的详细说明  
> 第四是 --add-opens=java.desktop/javax.swing=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED 这两个是对于高版本（17+） jdk 增加的参数，不然启动 burp 会报错，如果你是低版本可以取消  

2. 激活这里不做说明，之前说过没如果不知道，请自行在博客搜索
3. 制作 Mac dock app

首先 打开 自动操作（automator.app），可以 command+空格 搜索自动操作 打开即可  
然后 选择左下角的 **新建文稿**:  
 <img width="638" alt="11" src="https://user-images.githubusercontent.com/18260135/150629786-e39ef1c5-d2f2-4af1-a5c8-719fc19d78cc.png">  
选择 **应用程序**  
<img width="537" alt="12" src="https://user-images.githubusercontent.com/18260135/150629792-520fa2b0-9b78-4ad2-952e-6ef3f4c8341e.png">  
在左边找到 **运行shell脚本**  拖到右边区域  
<img width="1000" alt="13" src="https://user-images.githubusercontent.com/18260135/150629802-1f470bb1-d1cf-4273-b9ee-88ca089391af.png">  
然后填写 shell 内容：`cd /path/to/your/burpsuite && bash start_burp.sh` **注意替换前面的路径为你自己 burpsuite 所在的路径**  
<img width="1000" alt="14" src="https://user-images.githubusercontent.com/18260135/150629813-9d669cca-d3d4-4735-9296-6257dd72d89c.png">  
然后选择右上角的 **运行** 看是否可以正常打开 burpsuite ，如果可以就保存（command+s）  
制作完成，可以在 启动台LaunchPad 里找到你的 burpsuite 或者 在 访达 的应用程序目录找到你的 burpsuite  
<img width="165" alt="15" src="https://user-images.githubusercontent.com/18260135/150629869-7a06a7c4-2a98-426a-a3f6-37f0d3dbb84c.png">  
3. 美化 burpsuite --- 修改 应用程序图标
在 访达 的应用程序目录找到你的 burpsuite 然后右键选择 **显示简介** 然后将 BurpSuite.icns 拖到左上角名字的左边即可生效:  
<img width="265" alt="16" src="https://user-images.githubusercontent.com/18260135/150629988-1dbcebbe-f366-4931-adc2-423cd7161611.png">  

### 下面上面提到的 -Xmx 参数相关：  

JVM之---Java内存分配参数：  
<table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td> <p>配置</p> </td><td> <p>说明</p> </td></tr><tr><td> <p>-Xms</p> </td><td> <p>设置初始堆内存大小</p> </td></tr><tr><td> <p>-Xmx</p> </td><td> <p>设置堆内存的最大值</p> </td></tr><tr><td> <p>-Xss</p> </td><td> <p>设置栈内存的大小</p> </td></tr><tr><td> <p>-XX:MinHeapFreeRatio</p> </td><td> <p>设置堆内存的最小空闲比例</p> </td></tr><tr><td> <p>-XX:MaxHeapFreeRatio</p> </td><td> <p>这是堆内存的最大空闲比例</p> </td></tr><tr><td> <p>-XX:NewSize</p> </td><td> <p>设置新生代的最小内存值</p> </td></tr><tr><td> <p>-XX:NewMaxSize</p> </td><td> <p>设置新生代的最大内存值</p> </td></tr><tr><td>-XX:NewRatio</td><td>设置年轻代（包括Eden和两个Survivor区）与年老代的比值（除去持久代)</td></tr><tr><td> <p>-XX:SurviorRatio</p> </td><td> <p>设置Eden区和Survior区的比例</p> </td></tr><tr><td> <p>-XX:MaxPermSize</p> </td><td> <p>设置持久代的最大值</p> </td></tr><tr><td> <p>-XX:PermSize</p> </td><td> <p>设置持久代的最小值</p> </td></tr><tr><td> <p>-XX:TargetSurvivorRatio</p> </td><td> <p>设置survivor区的可使用率</p> </td></tr></tbody></table>

参考链接：  
https://forum.portswigger.net/thread/run-burp-on-openjdk-17-5611cb564e50e 
