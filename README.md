# Get Start
* 文件中一行代表一个 prompts，文件命名格式为 “xxx.txt”，程序只读取 txt 文件，文件需要放在目录 "/prompts" 下 *

## 批量执行 prompts 生成图片
1. 将 prompts 的数据集放在文件夹 /prompts 下
2. 打开终端，切换 conda 环境，执行 ```conda activate google-p2p```
3. 运行 ```python main.py```
4. 运行完成后，即可在 result 下看到相应的图片

## 指定执行某个 prompt 生成图片
1. 将 prompts 的数据集放在文件夹 /prompts 下
2. 打开终端，切换 conda 环境，执行 ```conda activate google-p2p```
3. 运行 ```python main.py --filename spooky.txt```（spooky.txt 就是 prompt 的文件名，需要放在 /prompts 目录下）
4. 运行完成后，即可在 result 下看到相应的图片

## 后台运行 prompt 生成图片
如果数据集太大，想服务器自己运行程序，等到后续有空再回来看结果，可用以下命令后台执行，后台执行时，日志会输出在当前目录 log.log 中，可以查看该日志查询执行结果

### 后台执行例子1
比如原命令是
```python main.py```

后台执行命令则是
```nohup python -u main.py > log.log 2>&1 &```

### 后台执行例子2
比如原命令是
```python main.py --filename spooky.txt```

后台执行命令则是
```nohup python -u main.py --filename spooky.txt > log.log 2>&1 &```