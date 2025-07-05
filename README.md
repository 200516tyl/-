# 学生信息管理系统

基于Flask的学生信息管理系统，包含前端HTML+CSS和后端Flask实现。

## 功能特点

- 用户认证
  - 学生登录/注册
  - 教师登录/注册
  
- 学生功能
  - 个人信息录入
  - 成绩查询
  
- 教师功能
  - 学生信息管理
  - 成绩录入和管理
  - 成绩统计和图表展示

## 技术栈

- 后端：Flask + SQLite
- 前端：HTML + CSS

## 安装和运行

1. 克隆项目
```bash
git clone https://github.com/200516tyl/-.git
cd -
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行项目
```bash
python app.py
```

4. 访问系统
打开浏览器访问：http://localhost:5000

## 项目结构

```
.
├── app.py              # 主应用文件
├── requirements.txt    # 项目依赖
├── static/            # 静态文件
│   └── style.css      # 样式文件
└── templates/         # HTML模板
    ├── in.html        # 入口页面
    ├── index.html     # 主页面
    ├── login.html     # 登录页面
    └── register.html  # 注册页面
    └── oerder.html    # 排序页面
    └── teacher_index.html  # 教师端主界面
    └── teacher_register.html  # 教师端注册界面
    └── teacher_score.html  # 教师端成绩录入 
    └── teacher_score_register.html # 教师端成绩管理
    └── updata.html #教师端成绩修改
    └── score_chart.html #数据可视化


```

## 数据库结构

- user表：用户信息
- student_score表：学生基本信息
- score表：学生成绩信息

## 开发者

- 200516tyl
