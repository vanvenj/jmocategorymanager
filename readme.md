# 背景
AVEVA PDMS中旧版本的模型文件中元件集与数据集分散在不同层次，交叉引用，难以管理、修改、移植。
为了更加科学的管理模型文件，降低模型数据间的耦合度，需要重新整理现有的模型。但是又需要利用现有数据文件避免从零开始建库，所以编写此快速输出模型工具。

# 功能
此工具主要有如下功能：
- 批量加载用户选择层下所有CATE文件以及描述
- 快速预览模型
- 自动整理模型相关联数据并且输出
- 自动对数据文件重新编码，为下次导入做准备

# 原理
一个模型文件CATEGORY包含如下子集：
- SCOM 基础元件及数据
- TEXT 元件参数信息
- PTSE 点集
- GMSE 型集
- DTSE 数据属性
- SDTE 描述、SymbolKey
- BTSE 法兰专用螺栓集

1. 首先使用PML将SCOM关联的数据整理并且输出。
2. 使用Python正则表达式将输出文件编码整理替换成新编码

# 文件介绍
```
pmllib
│   pml.index
│
│─jmocategorymanager
│   │   jmocatecorymanager.pmlfrm 主程序
│   │   format.py 编码处理程序
│   │   readme.md 说明文档
│   │   python27.exe Python环境
│   │   python27.zip Python包
│   │   python27.dll 
│   │ 
└ ─ ...
    │
```

# 如何使用
1. 将文件夹复制到PDMS安装目录中PMLLIB下。
2. 删除PMLLIB目录下 pml.index 文件
3. 在PDMS命令行输入 pml rehash all
4. 在PDMS命令行输入 show !!jmocategorymanager使用此工具。

![snagit](https://github.com/vanvenj/jmocategorymanager/raw/master/snagit.png)
