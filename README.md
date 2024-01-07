## XJTU-2023-秋-计算方法-上机实验

### 实验环境

* `python3.11`

* `pycharm`
* `numpy`， `matplotlib`

### 文件结构

```
├─exp1
│      exp1.py
│      sea2023.csv
│
├─exp2
│      exp2.py
│      exp2_least_squares.py
│      fans.txt
│
├─exp3
│      data20231.dat
│      data20232.dat
│      data20233.dat
│      data20234.dat
│      data20235.dat
│      exp3.py
│
├─questions
│      《计算方法》上机题目2023.docx
│
└─report
        计算方法实验上机报告.md
```

其中实验用到的主要源代码为：

* `exp1.py`
* `exp2_least_squares.py`
* `exp3.py`

其中`sea2023.csv`以及`data20231~5.dat`的内容为题目所给，`fans.txt`的内容为每一天的粉丝数量。

每个目录的代码都可以在`cmd`下使用`python xxx.py`运行。

```cmd
Windows:Numerical_Method_exp\exp3> python .\exp3.py
data20231.dat result:
[3.14000101 3.14000007 3.13999815 3.13999913 3.13999812 3.14000184
 3.14000009 3.1400005  3.1400012  3.13999829]
data20232.dat result:
[3.14000181 3.13999959 3.13999976 3.13999884 3.13999924 3.14000053
 3.13999985 3.14000043 3.1399983  3.14000223]
data20233.dat result:
[2.07800144 2.07799986 2.07799851 ... 2.07799978 2.07799843 2.07800332]
data20234.dat result:
[2.07699972 2.0769992  2.07700058 ... 2.07700125 2.07699828 2.07700092]
Windows:Numerical_Method_exp\exp3>
```

