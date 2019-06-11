chcp 936
REM 设置936编码防止某些中文路径导致批处理失效
@echo off
setlocal enabledelayedexpansion
mode con cols=90 lines=30&color 0a&title 创建Burp Suite一键启动【英文原版】脚本快捷方式
echo ======================================================
echo m    m                             mm   m          m
echo ##  ##  m mm  m   m  m mm          #"m  #  mmm   mm#mm
echo # ## #  #"  "  #m#   #"  #         # #m # #"  #    #
echo # "" #  #      m#m   #   #         #  # # #""""    #
echo #    #  #     m" "m  #   #    #    #   ## "#mm"    "mm
echo =======================================================  
echo.
echo [+] 感谢破解作者^&汉化作者^&Burp官方^&各个插件作者^&感谢EveryOne!
echo.
echo [+] 欢迎各位朋友光临我博客@_@：https://mrxn.net
echo.
echo [+] 获得当前路径:%~dp0
set path=%~dp0Burp_start_en.bat
echo.
if exist %path% (
echo [+] 发现Burp【英文原版】一键启动脚本Burp_start_en.bat
echo.
echo [+] 启动脚本路劲：
echo.
echo [+] %path%
echo.
goto :creat
) else (
echo [-] 注意,未发现【英文原版】启动脚本Burp_start_en.bat，请注意是否改名,程序退出... 
echo.
pause
exit
)

:creat
echo [+] 开始创建快捷方式...
echo.
rem 设置程序的完整路径(必要)
set Program=%path%
rem 设置快捷方式名字(必要)
set LinkName=Burp_Suite_En
rem 程序工作路径
set WorkDir=%~dp0
rem 设置快捷方式说明
set Desc=BurpSuite【英文原版】一键启动
rem 设置【英文原版】快捷方式图标
set icon=%~dp0/img/Goescat-Macaron-Burp-suite.ico
if not defined WorkDir call:GetWorkDir "%Program%"
(echo Set WshShell=CreateObject("WScript.Shell"^)
echo strDesKtop=WshShell.SpecialFolders("DesKtop"^)
echo Set oShellLink=WshShell.CreateShortcut(strDesKtop^&"\%LinkName%.lnk"^)
echo oShellLink.TargetPath="%Program%"
echo oShellLink.WorkingDirectory="%WorkDir%"
echo oShellLink.WindowStyle=1
echo oShellLink.Description="%Desc%"
echo oShellLink.IconLocation="%icon%"
echo oShellLink.Save)>makelnk.vbs
echo [+] 【英文原版】桌面快捷方式创建成功!!
echo.
makelnk.vbs
del /f /q makelnk.vbs
pause
goto :eof
:GetWorkDir
set WorkDir=%~dp1
set WorkDir=%WorkDir:~,-1%
pause
goto :eof