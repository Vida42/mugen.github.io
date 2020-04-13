---
layout:     post
title:      "Python Virtual Environments"
subtitle:   " \"Basic Introduction\""
date:       2020-04-12 23:00:00
author:     "Mugen"
header-img: "img/post-bg-virtualenv.jpg"
tags:
    - Kit
    - Knowledge
---

> It took longer than expected.

### 目的

如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，就是安装在系统的Python 3。如果不同的应用需要不同版本的依赖包怎么办？

这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

### 安装virtualenv并且设置虚拟环境（WINDOWS）

1. 安装virtualenv：

```
pip install virtualenv
```

2. 创建新目录并进入

3. 创建一个独立的Python运行环境并命名（例：命名为`venv`）: 

```
virtualenv venv
```

新建的Python环境会被放到当前目录下的venv目录里

4. 使用如下命令进入虚拟环境：

```
venv\Scripts\activate
(mac) source venv\bin\activate
```

此时注意到命令提示符变了，有个(venv)前缀，表示当前环境是一个名为venv的Python环境。

5. 正常安装各种第三方包，并运行python命令

在`venv`环境下，用`pip`安装的包都被安装到`venv`这个环境下，系统Python环境不受任何影响。也就是说，`venv`环境是专门针对当前目录下的应用创建的。


6. 退出当前的venv环境，使用deactivate命令：

```
venv\Scripts\deactivate
(mac) deactivate
```

此时就回到了正常的环境，现在pip或python均是在系统Python环境下执行。

### 项目依赖获取

当项目开发结束的时候，再次进入虚拟环境，执行命令

```
pip freeze > requirements.txt
```

此时虚拟环境中的依赖会生成一个txt文件，后续可以直接使用这个文件进行安装依赖

```
pip install -r requirements.txt
```

Reference:

[1] [virtualenv liaoxuefeng](https://www.liaoxuefeng.com/wiki/1016959663602400/1019273143120480)

[2] [Python 虚拟环境 Virtualenv 分别在 Windows 和 Linux 上的安装和使用](https://tendcode.com/article/virtualenv-for-python/)

[3] [使用virtualenv进行python项目开发](https://blog.csdn.net/lwcaiCSDN/article/details/88236119)

[4] [Virtualenv Docs](https://virtualenv.pypa.io/en/latest/)
