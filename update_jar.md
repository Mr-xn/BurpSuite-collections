## 使用 github action 打包最新的 burp 插件

### 前言

大部分的 burp 插件都是基于 JAVA 开发的，我们可以使用 github 的 action 打包插件最新版

### maven 项目的 jar 打包

```yaml

name: maven build and push

# author Mrxn
# github: github.com/Mr-xn

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up JDK 1.8
      uses: actions/setup-java@v1
      with:
        java-version: 1.8
    - name: Build with Maven
      run: 
        mvn clean package -DskipTests=true -Dmaven.javadoc.skip=true -B -V
    - name: Upload a Build Artifact
      uses: actions/upload-artifact@v2.3.1
      with:
        # Artifact name
        name: # optional, default is artifact
          Fiora
        # A file, directory or wildcard pattern that describes what to upload
        path: 
          target/*.jar
        # The desired behavior if no files are found using the provided path.
```

需要注意几点：

第一个是触发条件，我这里是 push 一次就会自动打包，有其他条件的可以自己修改触发条件

第二个是 name ，这里的样例是 Fiora ，你可以自己根据项目名字自己修改

第三个是 path ，也就是打包完成后压缩上传的文件路径，一般情况下是 target 但是有的项目不是，这个可以在 action 页面的日志里看到 build 的结果是什么目录，再修改下 目录就行，样例是上传 target 目录下的所有的 jar 文件，可以根据实际需要修改这里上传的文件类型等等

详细的可以看我的这篇文章：https://mrxn.net/jswz/684.html 

实际项目可以参考我这个：https://github.com/Mr-xn/Fiora 

### 基于 Gradle 的打包 jar

稍作等待，写作中
