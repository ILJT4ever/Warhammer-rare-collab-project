# 战锤稀有模型价格追踪项目

本项目旨在自动抓取多个电商平台（如淘宝、闲鱼、eBay、Mercari）上绝版/稀有的战锤模型的**在售和已售价格、型号、发布时间等信息**，并将其结构化导出为 Excel 或 JSON 文件，方便模型收藏者、转卖者进行价格分析与比对。

---

## 📁 项目结构说明
warhammer-rare-collab-project/
├── crawlers/ # 各平台爬虫脚本（如 taobao.py）
├── data/raw/ # 原始抓取数据（已被 .gitignore 忽略）
├── outputs/ # 输出的 Excel、CSV、JSON 等结果文件
├── utils/ # 工具函数模块（如模型名解析器）
├── main.py # 主程序入口，统一调度所有平台爬虫
├── requirements.txt # 所需依赖库列表
├── .gitignore # Git 忽略规则
├── LICENSE # MIT 开源协议
└── README.md # 当前说明文档（你正在读的这个文件）

---

## ✅ 当前进度与功能开发计划

### 已完成 ✅
- [x] 项目结构初始化
- [x] 虚拟环境与依赖配置（requirements.txt）
- [x] 淘宝爬虫初版（抓取标题、价格、链接等）
- [x] 主程序 main.py，实现多平台统一调用框架

### 待开发 🔧
- [ ] 闲鱼爬虫
- [ ] eBay / PicClick 爬虫
- [ ] Mercari 日本平台爬虫
- [ ] 模型名称、材质、状态等智能解析（utils/parser.py）
- [ ] 数据清洗与重复商品合并
- [ ] 输出更丰富字段（如平台、发货地、时间等）

---

## 💡 使用说明（本地运行步骤）

> 所有操作建议使用 Python 3.8+ 环境，推荐 macOS / Linux 系统

### 1️⃣ 创建并激活虚拟环境（推荐）

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境（Mac / Linux）
source venv/bin/activate

### 2️⃣ 安装依赖库

pip install -r requirements.txt

### 3️⃣ 运行主程序，抓取淘宝数据

python3 main.py

结果将保存到：outputs/all_prices.xlsx

🤝 协作规范（给所有开发者）
所有新功能请在 crawlers/、utils/ 等对应目录中创建新的模块
所有代码需用中文注释
每个功能建议单独开分支，提交 PR 后再合并主分支
建议通过 VS Code 或 PyCharm 编辑项目，方便路径与导入管理
提交前确认未将数据/临时文件加入 Git（已通过 .gitignore 忽略）

🧑‍💻 协作者如何加入？
由仓库管理员添加你为协作者
你将收到 GitHub 邀请，请登录 GitHub 接受邀请
然后执行以下命令 clone 仓库：
git clone https://github.com/xxx/warhammer-rare-collab-project.git
cd warhammer-rare-collab-project

📮 联系方式 / 问题反馈
如有任何协作问题或爬虫问题，请联系仓库管理员或创建 Issue

# 🧠 GitHub 项目新手协作指南（零基础入门版）

适用于：**第一次接触编程或 GitHub 的新手协作者**，通过此文档你将学会如何加入我们的项目、设置环境、参与协作。

---

## ✅ 你需要准备：

* 一台电脑（Windows 或 Mac）
* 安装好 [GitHub Desktop](https://desktop.github.com/)
* 安装好 [Python 3.9+](https://www.python.org/downloads/)
* 安装好 [VS Code 编辑器](https://code.visualstudio.com/)（可选但强烈推荐）

---

## 第一步：加入我们的项目

### 1.1 接受 GitHub 邀请

1. 仓库管理员会通过你的 GitHub 用户名邀请你
2. 登录 [GitHub官网](https://github.com/)，点击右上角铃铛🔔，**接受邀请**

### 1.2 安装 GitHub Desktop（图形界面操作）

1. 下载：[https://desktop.github.com/]
2. 安装后登录你的 GitHub 账号
3. 进入 GitHub Desktop → `File` → `Clone Repository`
4. 找到项目 `warhammer-rare-collab-project`，选择位置后点击 `Clone`

---

## 第二步：创建运行环境（一次性设置）

### 2.1 打开终端（Terminal / CMD）

* Mac：打开 Terminal
* Windows：使用 PowerShell 或 CMD

### 2.2 创建虚拟环境

```bash
python3 -m venv venv
```

### 2.3 激活虚拟环境

* Mac/Linux：

```bash
source venv/bin/activate
```

* Windows：

```bash
venv\Scripts\activate
```

### 2.4 安装项目所需库

```bash
pip install -r requirements.txt
```

---

## 第三步：运行程序看看效果

```bash
python3 main.py
```

程序会尝试抓取淘宝战锤模型的价格信息，并生成一个 Excel 表格：

```
outputs/all_prices.xlsx
```

---

## 第四步：如何参与协作？

### 4.1 用 GitHub Desktop 提交代码

1. 在项目中修改文件（如填写一个爬虫）
2. GitHub Desktop 会自动识别你做了修改
3. 左下角填写：

   * `Summary`（一行说明你改了啥）
   * `Description`（可选，多行列出具体更改点）
4. 点击 `Commit to main`
5. 点击右上角 ⚠️`Push origin` ⚠️（‼️要在确保程序正常运行的情况下操作）上传到 GitHub

### 4.2 不想要自己的修改了怎么办？

在 GitHub Desktop → `Changes` 界面 → 点击右下角 `Discard all changes`，即可放弃本地更改。

---

## 第五步：开发建议

* 项目结构已划分好，不要在根目录新建文件
* 写代码请用中文注释
* 每加一个新平台爬虫，新建一个文件如 `crawlers/xianyu.py`
* 不懂就问，欢迎随时在群里提问

---

## 📮 常见问题（FAQ）

### Q1：我从来没用过编程，怕出错怎么办？

> 不用怕！你只是修改自己本地的副本，⚠️在没有push前⚠️，出错不会影响整体，任何东西都能撤回。

### Q2：为什么我 push 的按钮是灰的？

> 因为你还没有填写 `Summary`，在左下角写一句话就可以了。

### Q3：为什么我运行 `main.py` 报错？

> 可能是没安装依赖。请确认你运行了 `pip install -r requirements.txt`，并激活了虚拟环境。

---

## 🧩 建议（选做）

* 学习 Git 原理：[https://learngitbranching.js.org/]
* 学会用 VS Code / PyCharm打开项目，查看代码更方便
* 用 markdown 写文档，增强你的协作能力

---
