# kivy_24p

## 什么是 24 点游戏

用 4 个整数，通过 +，-，×，/ 这四种运算，得到 24。比如：

* 1 2 3 4：(2 + 4) * (3 + 1) = 24
* 1 2 3 7：3 + (1 + 2) * 7 = 24

## 如何开始

由于 kivy 需要一些无法通过 pipenv 安装的依赖，请参考 https://kivy.org/docs/installation/installation.html 上的相关内容。

然后使用 pipenv install -r requirements.txt 安装必要的依赖包。完成后使用 pipenv shell 启动虚拟环境。

### 命令行 calc24.py

执行 python ./calc24.py，根据提示输入 4 个整数，程序会给出所有找到的解法。

### kivy App

执行 kivy ./main.py

## 设计说明

TBF


