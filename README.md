# 待办事项管理应用

基于Flask开发的轻量级任务管理Web应用，包含用户系统、任务管理等功能模块。

## 主要功能
- 用户注册/登录
- 任务创建/编辑/删除
- 任务分类与标签管理
- 任务状态追踪（进行中/已完成）

## 安装与运行
```bash
# 克隆仓库
git clone [仓库地址]

# 安装依赖
pip install -r requirements.txt

# 设置环境变量
export FLASK_APP=app.py
export FLASK_ENV=development

# 初始化数据库
flask init-db

# 启动应用
flask run
```

## 使用说明
1. 访问 `http://localhost:5000`
2. 注册新账户或使用测试账号登录
3. 在控制面板创建新任务
4. 使用分类/标签组织任务
5. 标记已完成任务

## 项目结构
// ... existing code ...
app.py         # 主程序入口
config.py      # 应用配置（数据库、密钥等）
exts.py        # Flask扩展初始化
models.py      # 数据库模型定义
blueprints/    # 功能模块蓝图
  auth.py      # 用户认证相关路由
  tasks.py     # 任务管理相关路由
static/        # 静态资源（CSS/JS/图片）
templates/     # Jinja2模板文件