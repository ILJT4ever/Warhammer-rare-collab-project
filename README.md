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
