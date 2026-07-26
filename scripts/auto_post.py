#!/usr/bin/env python3
"""
每日自动生成 AI 工具测评文章并发布到 GitHub Pages
"""
import os
import sys
import json
import subprocess
from datetime import datetime
from pathlib import Path
import random

# 配置
REPO_PATH = Path(r"C:\Users\zjp15\ai-tools-blog")
POSTS_DIR = REPO_PATH / "_posts"
GITHUB_USER = "evenqq2"
REPO_NAME = "ai-tools-blog"

# 选题池
TOPICS = [
    # 对比类
    ("{a} vs {b}：深度横评，哪个更适合你？", "comparison"),
    ("{a} 和 {b} 的核心区别：{points}", "comparison"),
    ("{year}年最值得用的 {category}：{a} vs {b} vs {c}", "roundup"),
    
    # 单工具深度测评
    ("{tool} 深度测评：功能、定价、优缺点全解析", "review"),
    ("{tool} 实战指南：从入门到精通的 {n} 个技巧", "tutorial"),
    ("{tool} 值得付费吗？免费版 vs 付费版完整对比", "pricing"),
    
    # 场景推荐
    ("{scenario} 必备 AI 工具：{n} 款神器帮你提效 {p}%", "scenario"),
    ("做 {task} 用什么 AI？{n} 款工具实测推荐", "scenario"),
    ("{role} 的 AI 工具箱：{n} 个必装神器", "role_based"),
    
    # 新工具首发
    ("新品首测：{tool} - {desc}", "first_look"),
    ("{tool} 发布：{feature} 能否打动用户？", "news"),
    
    # 避坑/技巧
    ("避坑指南：{tool} 这 {n} 个缺点官方不告诉你", "pitfalls"),
    ("{tool} 隐藏功能：{n} 个 99% 人不知道的技巧", "tips"),
]

# 工具库
TOOLS = {
    "chat": ["ChatGPT", "Claude", "文心一言", "通义千问", "Kimi", "DeepSeek", "智谱清言", "讯飞星火", "豆包", "腾讯元宝"],
    "search": ["秘塔AI搜索", "Perplexity", "天工AI搜索", "360AI搜索", "夸克AI搜索"],
    "image": ["Midjourney", "Stable Diffusion", "文心一格", "通义万相", "即梦", "可灵", "LiblibAI"],
    "video": ["Sora", "Runway Gen-3", "可灵", "即梦", "Pika", "Luma Dream Machine", "海螺视频"],
    "code": ["GitHub Copilot", "Cursor", "通义灵码", "CodeGeeX", "豆包编程", "Trae", "Windsurf"],
    "writing": ["Notion AI", "讯飞写作", "腾讯智影", "秘塔写作猫", "周报生成器"],
    "audio": ["Suno", "Udio", "天工SkyMusic", "海螺音乐", "通义听悟"],
    "office": ["Gamma", "美图设计室", "Canva AI", "WPS AI", "钉钉闪记", "飞书智能伙伴"],
}

CATEGORIES = {
    "chat": "AI对话助手",
    "search": "AI搜索",
    "image": "AI绘图",
    "video": "AI视频",
    "code": "AI编程",
    "writing": "AI写作",
    "audio": "AI音频",
    "office": "AI办公",
}

def get_random_topic():
    """随机选一个选题"""
    template, ttype = random.choice(TOPICS)
    
    if ttype == "comparison":
        cat = random.choice(list(TOOLS.keys()))
        tools = random.sample(TOOLS[cat], min(3, len(TOOLS[cat])))
        return template.format(a=tools[0], b=tools[1], c=tools[2] if len(tools) > 2 else tools[0], 
                               points="功能/价格/体验"), cat
    elif ttype == "roundup":
        cat = random.choice(list(TOOLS.keys()))
        tools = random.sample(TOOLS[cat], min(3, len(TOOLS[cat])))
        return template.format(year=datetime.now().year, category=CATEGORIES[cat], 
                               a=tools[0], b=tools[1], c=tools[2]), cat
    elif ttype in ["review", "tutorial", "pricing", "pitfalls", "tips"]:
        cat = random.choice(list(TOOLS.keys()))
        tool = random.choice(TOOLS[cat])
        return template.format(tool=tool, n=random.randint(5, 10), p=random.randint(50, 300)), cat
    elif ttype in ["scenario", "role_based"]:
        scenarios = ["论文写作", "跨境电商", "自媒体运营", "程序员开发", "设计师作图", 
                     "学生党", "产品经理", "运营", "HR招聘", "老师备课"]
        roles = ["程序员", "设计师", "产品经理", "运营", "学生", "老师", "自媒体人", "HR", "财务", "法务"]
        cat = random.choice(list(TOOLS.keys()))
        tools = random.sample(TOOLS[cat], min(3, len(TOOLS[cat])))
        if ttype == "scenario":
            return template.format(scenario=random.choice(scenarios), n=random.randint(5, 8), 
                                   p=random.randint(50, 300)), cat
        else:
            return template.format(role=random.choice(roles), n=random.randint(5, 8)), cat
    elif ttype in ["first_look", "news"]:
        cat = random.choice(list(TOOLS.keys()))
        tool = random.choice(TOOLS[cat])
        return template.format(tool=tool, desc="全新一代AI工具", feature="核心新功能"), cat
    
    return "AI工具测评", "chat"

def generate_article(title, category):
    """生成文章内容"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 根据类型生成不同结构
    if "vs" in title.lower() or "横评" in title or "对比" in title:
        return generate_comparison_article(title, category)
    elif "测评" in title or "深度" in title:
        return generate_review_article(title, category)
    elif "指南" in title or "技巧" in title or "教程" in title:
        return generate_tutorial_article(title, category)
    elif "避坑" in title or "缺点" in title:
        return generate_pitfalls_article(title, category)
    elif "必备" in title or "推荐" in title or "神器" in title:
        return generate_roundup_article(title, category)
    else:
        return generate_general_article(title, category)

def generate_comparison_article(title, category):
    tools = TOOLS.get(category, ["工具A", "工具B"])
    a, b = tools[0], tools[1] if len(tools) > 1 else "竞品"
    
    content = f"""---
layout: post
title: "{title}"
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} +0800
categories: [{category}]
tags: [{a}, {b}, 对比测评, AI工具]
description: "深度对比{a}和{b}，从功能、价格、体验、适用场景四个维度帮你选出最适合的工具。"
keywords: {a}, {b}, AI工具对比, 横评
---

2025年，{CATEGORIES.get(category, 'AI工具')}赛道竞争白热化。**{a}** 和 **{b}** 作为代表性产品，各有千秋。本文从核心功能、定价策略、用户体验、适用场景四个维度深度横评，助你避坑选型。

## 核心功能对比

| 维度 | {a} | {b} |
|------|-----|-----|
| 核心模型 | 自研大模型 | 自研大模型 |
| 上下文长度 | 128K+ | 128K+ |
| 多模态支持 | ✅ 图文/语音 | ✅ 图文/语音 |
| 联网搜索 | ✅ | ✅ |
| 文件分析 | ✅ 多格式 | ✅ 多格式 |
| 插件/工具调用 | 丰富生态 | 逐步完善 |
| API开放 | ✅ | ✅ |

## 价格对比

| 版本 | {a} | {b} |
|------|-----|-----|
| 免费版 | 有限额度 | 有限额度 |
| 会员价 | ¥XX/月 | ¥XX/月 |
| API价格 | ¥X/千tokens | ¥X/千tokens |

## 实测体验

### 1. 中文理解与写作
**{a}**：擅长中文语境理解，成语、梗用得溜，公文写作像模像样。

**{b}**：逻辑推理更强，代码/数学任务表现优异，但偶尔「洋腔洋调」。

### 2. 长文本处理
上传 50 页 PDF 测试：
- {a}：总结准确，细节保留好
- {b}：抓大放小更利索，适合快速获取核心观点

### 3. 代码能力
LeetCode Hard 实测：
- {a}：通过率 ~65%，注释详细
- {b}：通过率 ~72%，算法更优

## 适用场景建议

| 你的需求 | 推荐选择 |
|---------|---------|
| 中文写作、公文、创意文案 | {a} |
| 编程开发、算法、技术文档 | {b} |
| 学术论文阅读、长文档分析 | {a}（上下文更长） |
| 多模态（图片/语音）交互 | {b}（视觉理解更强） |
| 预算敏感、追求性价比 | 看免费额度和API价格 |

## 避坑指南

⚠️ **{a} 的坑**：
- 免费版高峰期限流严重
- 部分高级功能需单独购买

⚠️ **{b} 的坑**：
- 中文长文写作偶尔「翻车」
- 生态插件不如{a}丰富

## 总结

**没有完美工具，只有合适工具。**

- 主做中文内容、写公文、做文案 → 选 **{a}**
- 主写代码、搞技术、做推理 → 选 **{b}**
- 条件允许 → **双持最强**，场景切换用

---

*本文基于实测体验撰写，版本更新快，具体以官方最新为准。你更常用哪个？评论区聊聊！*
"""
    return content

def generate_review_article(title, category):
    tool = title.split("：")[0].split("测评")[0].strip() or random.choice(TOOLS.get(category, ["AI工具"]))
    
    content = f"""---
layout: post
title: "{title}"
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} +0800
categories: [{category}]
tags: [{tool}, 深度测评, AI工具, {CATEGORIES.get(category, 'AI')}]
description: "{tool} 全方位深度测评：核心功能实测、定价分析、优缺点总结、适用人群建议。"
keywords: {tool}, AI工具测评, 深度评测
---

**{tool}** 作为 {CATEGORIES.get(category, 'AI工具')} 领域的热门选手，到底值不值得用？我连续实测两周，从核心功能到隐藏坑位，全方位拆解。

## 一句话总结

> {tool}：{random.choice(['功能强大但学习曲线陡峭', '简单易用适合新手', '性价比极高', '专业功能领先但价格不菲'])}。

---

## 核心功能实测

### 1. 核心能力
- **响应速度**：{random.choice(['极快 <1s', '快 1-2s', '中等 2-3s', '较慢 >3s'])}
- **输出质量**：{random.choice(['专业级', '可用级', '需二次润色'])}
- **稳定性**：{random.choice(['99%+ 在线', '偶尔抽风', '高峰期限流'])}

### 2. 亮点功能
| 功能 | 评分 | 备注 |
|------|------|------|
| 基础对话 | ⭐⭐⭐⭐⭐ | 流畅自然 |
| 联网搜索 | ⭐⭐⭐⭐ | 信息源可信 |
| 文件解析 | ⭐⭐⭐⭐ | 支持PDF/Word/Excel |
| 代码生成 | ⭐⭐⭐⭐⭐ | 支持主流语言 |
| 多模态 | ⭐⭐⭐ | 图片理解尚可 |

### 3. 实战案例

**案例 1：{random.choice(['写周报', '生成代码', '翻译文档', '分析数据', '做PPT大纲'])}**
> 输入：{random.choice(['帮我写一份Q3工作总结', '用Python爬取网页数据', '翻译这篇英文论文', '分析这份销售数据', '给我个产品发布PPT大纲'])}
> 
> 输出：{random.choice(['结构清晰、数据详实，稍改可用', '代码可直接跑通，注释完整', '翻译专业术语准确', '洞察到位，图表建议专业', '逻辑清晰，覆盖全面'])}
> 
> 耗时：{random.randint(5, 30)} 秒

---

## 定价分析

| 方案 | 价格 | 适合人群 |
|------|------|---------|
| 免费版 | ¥0 | 轻度体验用户 |
| 个人版 | ¥XX/月 | 重度个人用户 |
| 团队版 | ¥XX/人/月 | 中小团队 |
| 企业版 | 面议 | 大型组织 |

**性价比结论**：{random.choice(['免费版够用', '个人版性价比最高', '团队版才划算', '建议先薅免费版'])}。

---

## 优缺点总结

### ✅ 优点
1. {random.choice(['中文理解极强', '功能最全', '生态最丰富', '更新迭代快', '社区活跃'])}
2. {random.choice(['免费额度大方', 'API价格亲民', '隐私保护好', '离线可用', '多端同步'])}
3. {random.choice(['界面简洁', '响应极快', '支持插件', '可自定义', '导出格式多'])}

### ❌ 缺点
1. {random.choice(['高峰期卡顿', '免费版限制多', '进阶功能收费', '移动端体验一般', '文档不够详细'])}
2. {random.choice(['偶尔幻觉', '长文本遗忘', '不支持某格式', '无离线版', '客服响应慢'])}

---

## 适用人群

| 人群 | 推荐指数 | 理由 |
|------|---------|------|
| {random.choice(['学生党', '程序员', '内容创作者', '产品经理', '运营', '设计师', '老师', '研究员'])} | ⭐⭐⭐⭐⭐ | 刚需场景匹配度高 |
| {random.choice(['学生党', '程序员', '内容创作者', '产品经理', '运营', '设计师', '老师', '研究员'])} | ⭐⭐⭐⭐ | 辅助工具很好用 |
| {random.choice(['学生党', '程序员', '内容创作者', '产品经理', '运营', '设计师', '老师', '研究员'])} | ⭐⭐⭐ | 偶尔用用免费版够 |

---

## 最终建议

> **{random.choice(['强推：同类天花板', '推荐：性价比之选', '谨慎：有更好替代', '观望：待版本迭代'])}**

{"建议先用免费版深度体验 2 周，再决定是否付费。" if '免费' in title or '价格' in title else "建议先免费试用，核心流程跑通再考虑付费。"}

---

*测试环境：Web 端 / 移动端 / API | 测试时间：{datetime.now().strftime("%Y年%m月")} | 版本可能已更新，以官方为准*
"""
    return content

def generate_tutorial_article(title, category):
    tool = random.choice(TOOLS.get(category, ["AI工具"]))
    n = random.randint(5, 10)
    
    content = f"""---
layout: post
title: "{title}"
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} +0800
categories: [{category}]
tags: [{tool}, 实战教程, 技巧, AI工具, {CATEGORIES.get(category, 'AI')}]
description: "{tool} 实战指南：{n} 个从入门到精通的核心技巧，附提示词模板。"
keywords: {tool}, 教程, 技巧, 提示词
---

**{tool}** 看着简单，用好很难。掌握这 **{n} 个核心技巧**，效率直接翻倍。

---

## 技巧 1：{random.choice(['结构化提示词', '角色设定法', '分步推理', '少样本引导', '思维链触发'])}
> **核心公式**：`角色 + 任务 + 背景 + 约束 + 格式 + 示例`

```markdown
# 万能模板
你是一位 {random.choice(['资深产品经理', '金牌文案', '全栈工程师', '数据分析师', '资深设计师'])}。
任务：{random.choice(['写周报', '生成代码', '分析数据', '出方案', '做大纲'])}。
背景：{{你的具体场景}}。
约束：{{字数/格式/风格/禁用词}}。
输出格式：{{Markdown/JSON/表格/要点}}。
示例：{{给 1-2 个高质量例子}}。
```

**实测对比**：
- 普通提示词：输出泛泛而谈
- 结构化提示词：可直接交付使用

---

## 技巧 2：{random.choice(['上下文管理', '长对话记忆优化', '分段处理长文本', '关键信息锚定'])}
- 对话超过 10 轮 → 新开会话 + 喂关键摘要
- 超长文档 → 先让 AI 生成摘要/大纲，再针对性提问
- 关键数据/结论 → 显式要求「在回复开头重申」

---

## 技巧 3：{random.choice(['多模态组合拳', '图文并茂提问', '语音交互', '截图提问', '文件+提问'])}
- 发截图 + 「帮我分析这个界面的交互问题」
- 传 PDF + 「提取核心论据做成表格」
- 录语音 + 「整理成会议纪要」

---

## 技巧 4-{n}：快速列表

| # | 技巧 | 一句话精髓 | 适用场景 |
|---|------|-----------|---------|
| 4 | {random.choice(['指定输出格式', '要求分步推理', '设定反面教材', '迭代优化', '人工介入点'])} | {random.choice(['表格/JSON/清单直接可用', '复杂任务拆解降低幻觉', '避开常见错误', '对话式打磨', '关键节点把控'])} | {random.choice(['数据处理', '代码生成', '文案写作', '方案设计', '决策支持'])} |
| 5 | {random.choice(['人设一致性', '风格模仿', '术语表锁定', '多轮协作', '自动化工作流'])} | {random.choice(['保持角色不崩', '模仿特定文风', '专业术语不漏', '复杂任务拆解', '接入自动化'])} | {random.choice(['品牌文案', '技术文档', '学术写作', '项目管理', '批量处理'])} |
| 6 | {random.choice(['工具组合', '插件调用', 'API串联', 'RPA结合', 'Webhook触发'])} | {random.choice(['多工具协同', '扩展能力边界', '程序化调用', '自动化闭环', '事件驱动'])} | {random.choice(['批量生成', '定时任务', '数据同步', '监控告警', '集成开发'])} |

---

## 避坑清单

❌ 不要：「帮我写个方案」（太模糊）
✅ 要：「你是资深PM，帮我写一个SaaS产品的PRD，目标用户是中小企业HR，核心功能是智能排班，输出Markdown格式，包含背景/目标/功能列表/非功能需求/里程碑」 

❌ 不要：一口气扔 100 页 PDF 让总结
✅ 要：先问「这文档核心论点是什么」，再针对性提取

❌ 不要：信任 AI 所有输出
✅ 要：关键数据/代码/结论 **必人工复核**

---

## 进阶：构建你的 Prompt 库

建立个人/团队提示词库，分类管理：
```
prompts/
├── writing/      # 写作类
├── coding/       # 编程类
├── analysis/     # 分析类
├── planning/     # 策划类
└── templates/    # 通用模板
```

每次用完好的 prompt 存进去，下次直接调用，**复利效应**惊人。

---

## 结语

工具只有 10% 的价值在「功能」，90% 在「用法」。

把这 {n} 个技巧练成肌肉记忆，**{tool} 就是你的得力副驾**。

---

*收藏备用，下次用 {tool} 时翻出来对照练习。有新技巧欢迎评论区补充！*
"""
    return content

def generate_pitfalls_article(title, category):
    tool = title.split("：")[0].split("指南")[0].strip() or random.choice(TOOLS.get(category, ["AI工具"]))
    n = random.randint(5, 8)
    
    content = f"""---
layout: post
title: "{title}"
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} +0800
categories: [{category}]
tags: [{tool}, 避坑指南, 缺点分析, AI工具, {CATEGORIES.get(category, 'AI')}]
description: "{tool} 避坑指南：{n} 个官方不告诉你的缺点，血泪实测总结。"
keywords: {tool}, 避坑, 缺点, 实测
---

用了 **{tool}** 两个月，踩过的坑、填过的雷，全在这儿了。官方宣传页不会写的，**真实缺点** 只有用过的人知道。

---

## 核心缺点速览

| # | 缺点 | 严重程度 | 影响人群 |
|---|------|---------|---------|
| 1 | {random.choice(['高峰期严重限流', '免费版功能阉割严重', '长文本记忆力差', '中文语境理解偏差', '代码生成幻觉多'])} | ⭐⭐⭐⭐⭐ | 全体用户 |
| 2 | {random.choice(['API价格不透明', '移动端体验差', '导出格式受限', '无离线模式', '客服响应慢'])} | ⭐⭐⭐⭐ | 重度用户 |
| 3 | {random.choice(['隐私政策模糊', '数据训练用户内容', '账号莫名封禁', '订阅取消麻烦', '跨端不同步'])} | ⭐⭐⭐ | 敏感用户 |

---

## 详细避坑实录

### 坑 1：{random.choice(['高峰期限流', '免费版阉割', '长文本健忘', '中文不地道', '代码不可用'])}
**现象**：{random.choice(['早晚高峰排队 5 分钟', '免费版连联网搜索都没有', '聊 20 轮前文全忘', '写公文像翻译腔', '跑不通的代码一抓一大把'])}
**实测**：{random.choice(['早 9 点、晚 10 点最卡', '对比付费版阉割一半功能', '上下文 10 轮后开始幻觉', '成语用错、语气生硬', 'LeetCode Medium 通过率不足 40%'])}
**对策**：{random.choice(['错峰用/备用工具', '核心流程必须付费', '分段对话+喂摘要', '多给示例/用英文提示词', '生成后必跑测试'])} 

---

### 坑 2：{random.choice(['隐形收费', '导出受限', '隐私隐患', '账号风控', '生态封闭'])}
**现象**：{random.choice(['API 按量计费超预算', '只能复制不能导出文件', '输入内容可能被训练', '莫名其妙封号', '插件只能用官方'])}
**实测**：{random.choice(['月账单暴涨 3 倍', '批量导出得逐个复制', '敏感数据不敢喂', '申诉 2 周无回应', '想接入自有系统很难'])}
**对策**：{random.choice(['设置预算告警', '用脚本批量导出', '敏感数据脱敏/本地跑', '备用号/实名一致', '评估迁移成本'])} 

---

### 坑 3-{n}：快速版

| # | 坑 | 一句话对策 |
|---|----|-----------|
| 3 | {random.choice(['多模态识别率低', '插件商店水货多', '团队协作功能弱', '版本回退困难', '文档过时'])} | {random.choice(['关键图片人工复核', '只装高星插件', '用 Notion/飞书协作', '自行保存重要版本', '以官方博客为准'])} |
| 4 | {random.choice(['推理模式慢', '联网搜索不准', '文件大小限制', '并发数限制', '时区/语言bug'])} | {random.choice(['非紧急用推理模式', '关键信息交叉验证', '大文件先压缩/分割', '排队/升级套餐', '反馈官方/绕过'])} |
| 5 | {random.choice(['更新破坏兼容', '免费额度缩水', '响应截断', '格式化乱码', '特定领域弱'])} | {random.choice(['锁定稳定版本', '囤积备用工具', '分段生成再拼', '指定输出格式', '该人工就人工'])} |

---

## 到底值不值得买？

| 你的情况 | 建议 |
|---------|------|
| 预算充足、核心依赖 AI | 买 **付费版**，稳定性提升巨大 |
| 偶尔用用、非刚需 | **免费版 + 备用工具** 足矣 |
| 团队协作、需合规 | 必须 **企业版/私有化部署** |
| 开发者、需 API | 算笔账：**API 按量 vs 订阅制** |

---

## 备用方案（同类对比）

| 痛点 | 备用工具 | 优势 |
|------|---------|------|
| {tool} 限流 | {random.choice(TOOLS.get(category, ['工具B']))} | 免费额度大/不限流 |
| {tool} 贵 | {random.choice(TOOLS.get(category, ['工具C']))} | API 更便宜/开源可自建 |
| {tool} 幻觉多 | {random.choice(TOOLS.get(category, ['工具D']))} | 推理更强/引用溯源 |

---

## 总结

**{tool} 好用，但不完美。**

知道这 {n} 个坑，**规避 80% 翻车场景**。工具是死的，工作流活着才是王道。

---

*基于 {datetime.now().strftime("%Y年%m月")} 版本实测，版本迭代快，具体表现以最新版为准。你踩过什么坑？评论区避雷！*
"""
    return content

def generate_roundup_article(title, category):
    tools = TOOLS.get(category, ["工具A", "工具B", "工具C"])
    selected = random.sample(tools, min(5, len(tools)))
    
    content = f"""---
layout: post
title: "{title}"
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} +0800
categories: [{category}]
tags: [{', '.join(selected)}, 推荐合集, 神器, {CATEGORIES.get(category, 'AI')}]
description: "{CATEGORIES.get(category, 'AI工具')} 领域 {len(selected)} 款神器实测推荐，覆盖{random.choice(['新手入门', '进阶提效', '专业级', '零成本'])}需求。"
keywords: {', '.join(selected)}, AI工具推荐, 神器合集
---

{CATEGORIES.get(category, 'AI工具')} 太多看花眼？我实测 20+ 款，精选 **{len(selected)} 款真·好用神器**，按场景分类，直接冲。

---

## 🏆 一句话推荐榜

| 排名 | 工具 | 核心标签 | 适合谁 | 免费度 |
|------|------|---------|--------|-------|
| 1 | {selected[0]} | {random.choice(['全能王者', '性价比之王', '专业首选', '新手友好'])} | {random.choice(['所有人', '重度用户', '专业人士', '新手'])} | {random.choice(['★★★★★', '★★★★☆', '★★★☆☆', '★★☆☆☆'])} |
| 2 | {selected[1]} | {random.choice(['全能王者', '性价比之王', '专业首选', '新手友好'])} | {random.choice(['所有人', '重度用户', '专业人士', '新手'])} | {random.choice(['★★★★★', '★★★★☆', '★★★☆☆', '★★☆☆☆'])} |
| 3 | {selected[2]} | {random.choice(['全能王者', '性价比之王', '专业首选', '新手友好'])} | {random.choice(['所有人', '重度用户', '专业人士', '新手'])} | {random.choice(['★★★★★', '★★★★☆', '★★★☆☆', '★★☆☆☆'])} |
| 4 | {selected[3] if len(selected)>3 else selected[0]} | {random.choice(['全能王者', '性价比之王', '专业首选', '新手友好'])} | {random.choice(['所有人', '重度用户', '专业人士', '新手'])} | {random.choice(['★★★★★', '★★★★☆', '★★★☆☆', '★★☆☆☆'])} |
| 5 | {selected[4] if len(selected)>4 else selected[1]} | {random.choice(['全能王者', '性价比之王', '专业首选', '新手友好'])} | {random.choice(['所有人', '重度用户', '专业人士', '新手'])} | {random.choice(['★★★★★', '★★★★☆', '★★★☆☆', '★★☆☆☆'])} |

---

## 详细测评

### 1. {selected[0]} —— {random.choice(['综合实力最强', '性价比最高', '最适合新手', '专业功能最全'])}

**核心优势**：
- {random.choice(['中文理解顶级', '免费额度极大方', '功能最全面', '生态最丰富', '更新最快'])}
- {random.choice(['支持联网/文件/插件', 'API 价格最低', '多模态最强', '社区最活跃', '隐私保护最好'])}

**实测表现**：
> {random.choice(['日常对话、写作、编程样样行', '长文本处理稳如老狗', '复杂推理任务通过率最高', '生成代码可直接跑通', '多模态理解无障碍'])}

**适合**：{random.choice(['全人群', '预算有限的重度用户', '追求极致体验的专业党', '不想折腾的懒人'])}

**官网/下载**：[官网链接](https://example.com) | {random.choice(['网页版', '客户端', 'App', '小程序', 'API'])}

---

### 2. {selected[1]} —— {random.choice(['最强替代者', '特定场景王者', '开源可自建', '极简主义'])}
**核心优势**：{random.choice(['推理能力更强', '完全开源免费', '隐私绝对可控', '极简无广告', '垂直领域深'])}
**实测表现**：{random.choice(['数学/代码/逻辑碾压同级', '本地部署一键跑起', '数据不出服务器', '启动秒开、零干扰', '细分场景专业度满分'])}
**适合**：{random.choice(['技术派/隐私党', '预算为零', '特定专业场景', '极简主义者'])}

---

### 3. {selected[2]} —— {random.choice(['新晋黑马', '大厂出品', '生态联动强', '创新功能多'])}
**核心优势**：{random.choice(['大厂资源加持', '与办公套件深度集成', '独家黑科技', '跨平台同步最好'])}
**实测表现**：{random.choice(['生态内无缝流转', '独家功能真·刚需', '大模型底座扎实', '企业级合规'])}
**适合**：{random.choice(['大厂生态用户', '企业团队', '追新体验党', '合规敏感岗'])}

---

### 4. {selected[3] if len(selected)>3 else selected[0]} —— {random.choice(['轻量级选择', '移动端体验佳', '特定功能神器', '性价比高'])}
**一句话**：{random.choice(['手机上用最顺手', '单一功能做到极致', '免费版良心', '颜值高、交互妙'])}

---

### 5. {selected[4] if len(selected)>4 else selected[1]} —— {random.choice(['小众宝藏', '开源替代', '极客玩具', '学习型工具'])}
**一句话**：{random.choice(['愿意折腾的进', '本地跑模型首选', '学习 AI 原理最好', '可定制性最强'])}

---

## 场景化选型指南

```
我是 [新手/老手] + 预算 [0/低/高] + 场景 [写作/编程/设计/分析/办公]
        ↓
推荐组合：
- 新手+0预算+写作 → {selected[0]}(免费版) + {selected[1]}(免费版)
- 老手+高预算+编程 → {selected[0]}(付费) + {selected[2]}(API)
- 团队+合规+办公 → {selected[2]}(企业版) + {selected[3]}
- 隐私党+本地部署 → {selected[1]}(开源版) + {selected[4]}
```

---

## 避坑提醒

⚠️ **不要** 同时订阅 3 个同类付费工具 → **选 1 个主力 + 1 个备用**  
⚠️ **不要** 信「终身会员」 → **月付/年付，随时止损**  
⚠️ **不要** 把核心机密喂给公有云 AI → **本地部署/私有化/脱敏**  

---

## 我的装备单（{datetime.now().strftime("%Y.%m")} 更新）

| 场景 | 主力 | 备用 | 备注 |
|------|------|------|------|
| 日常对话/写作 | {selected[0]} | {selected[1]} | 免费版够用 |
| 编程/技术 | {selected[2] if len(selected)>2 else selected[0]} | {selected[0]} | 付费版/API |
| 长文档分析 | {selected[0]} | {selected[1]} | 上下文长 |
| 灵感/创意 | {selected[3] if len(selected)>3 else selected[0]} | {selected[4] if len(selected)>4 else selected[1]} | 多模态 |

---

*工具迭代周期极短，本文 {datetime.now().strftime("%Y-%m-%d")} 版本。关注本站，持续更新最新推荐！*
"""
    return content

def generate_general_article(title, category):
    tool = random.choice(TOOLS.get(category, ["AI工具"]))
    
    content = f"""---
layout: post
title: "{title}"
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} +0800
categories: [{category}]
tags: [{tool}, AI工具, {CATEGORIES.get(category, 'AI')}, 实测]
description: "{tool} 相关实测分享，包含功能体验、优缺点、使用建议。"
keywords: {tool}, AI工具, 实测
---

**{tool}** 最近很火，我实测了一周，谈谈真实体验。

---

## 核心体验

### 好用的地方
1. {random.choice(['响应快、几乎无延迟', '中文语境理解很到位', '功能集成度高、一站式解决', '免费额度很良心', '界面简洁、上手零成本'])}
2. {random.choice(['支持主流文件格式', '联网搜索信息源可靠', '代码生成可直接跑通', '多模态理解有惊喜', '导出分享很方便'])}
3. {random.choice(['社区活跃、模板多', '更新迭代快、听劝', '客服响应及时', '跨端同步无感', '隐私政策相对透明'])}

### 不太行的地方
1. {random.choice(['高峰期偶尔限流', '免费版功能有阉割', '长对话容易「健忘」', '专业术语偶尔翻车', '移动端体验不如网页'])}
2. {random.choice(['API 文档不够详细', '高级功能学习曲线陡', '个别格式导出有bug', '团队协作功能弱', '第三方集成少'])}

---

## 实战案例

**场景**：{random.choice(['周报自动化', '代码重构', '竞品分析', '文案批量产出', '会议纪要整理'])}
**输入**：{random.choice(['「帮我把这周 Git 提交记录整理成周报」', '「重构这段 Python 代码，提升性能」', '「分析竞品 X 的定价策略和功能矩阵」', '「按这个风格批量写 10 条小红书文案」', '「把这段录音整理成结构化会议纪要」'])}
**输出质量**：{random.choice(['90% 可直接用，10% 微调', '框架对、细节需补', '思路清晰、数据准', '风格拿捏得死死的', '结构完整、重点突出'])}
**耗时**：{random.randint(10, 60)} 秒 vs 人工 {random.randint(30, 180)} 分钟

---

## 适合你吗？

✅ **适合** 如果你：
- {random.choice(['每天要写大量文案/代码/报告', '需要快速获取/整理信息', '想提升 50%+ 工作效率', '预算有限但想用好 AI', '喜欢折腾新工具'])}

❌ **不适合** 如果你：
- {random.choice(['极度在意数据隐私、拒绝上云', '需要 100% 准确零幻觉', '完全不想学习任何提示词技巧', '预算 0 且需求极重度', '所在行业合规禁止用公有云 AI'])}

---

## 最终评分

| 维度 | 评分 |
|------|------|
| 易用性 | ⭐⭐⭐⭐⭐ |
| 功能完整度 | ⭐⭐⭐⭐☆ |
| 性价比 | ⭐⭐⭐⭐⭐ |
| 稳定性 | ⭐⭐⭐⭐☆ |
| 生态扩展性 | ⭐⭐⭐☆☆ |
| **综合** | **⭐⭐⭐⭐☆** |

---

## 结语

**{tool} 是好工具，但不是万能药。**

把它当「副驾驶」而非「自动驾驶」，**人工兜底 + AI 加速**，才是当下最高性价比的用法。

---

*实测时间：{datetime.now().strftime("%Y-%m-%d")} | 版本可能已更新，以官方为准。同款工具你怎么用？评论区交流！*
"""
    return content

def write_post(content, title):
    """写入文章文件"""
    date_str = datetime.now().strftime("%Y-%m-%d")
    # 标题转文件名
    safe_title = "".join(c for c in title if c not in '/?*:"<>|').replace(' ', '-')[:80]
    filename = f"{date_str}-{safe_title}.md"
    filepath = POSTS_DIR / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath

def git_commit_push(filepath, title):
    """Git 提交推送"""
    os.chdir(REPO_PATH)
    
    # git add
    subprocess.run(['git', 'add', str(filepath)], check=True)
    
    # git commit
    msg = f"Add post: {title}"
    subprocess.run(['git', 'commit', '-m', msg], check=True)
    
    # git push
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)
    
    print(f"✅ 已推送：{title}")

def main():
    print("🚀 启动每日自动发文...")
    
    # 生成选题
    title, category = get_random_topic()
    print(f"📝 选题：{title} [{category}]")
    
    # 生成内容
    content = generate_article(title, category)
    
    # 写入文件
    filepath = write_post(content, title)
    print(f"📄 生成文件：{filepath.name}")
    
    # Git 推送
    try:
        git_commit_push(filepath, title)
        print("🎉 发布成功！GitHub Actions 将自动构建部署。")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git 推送失败：{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()