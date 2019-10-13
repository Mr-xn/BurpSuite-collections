chcp 936
rem 设置936编码防止某些中文路径导致批处理失效
@echo off
rem 必须切到根目录执行才行
cd \
start javaw -Dfile.encoding=utf-8 -javaagent:%~dp0\BurpSuiteCn.jar -Xbootclasspath/p:%~dp0\burp-loader-keygen.jar -Xmx1024m -jar %~dp0\burpsuite_pro_v1.7.37.jar
exit