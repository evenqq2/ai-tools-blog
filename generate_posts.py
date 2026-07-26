import os
from datetime import datetime, timedelta

POSTS_DIR = r"C:\Users\zjp15\ai-tools-blog\_posts"

# 确保目录存在
os.makedirs(POSTS_DIR, exist_ok=True)

# 文章数据列表：(filename, title, categories, tags, description, keywords)
articles = []

# 定义日期范围：从2025-07-25开始，每篇文章递增一天
start_date = datetime(2025, 7, 25)

# AI对话类 (chat)
chat_articles = [
    ("chatgpt-vs-claude-2025.md", "ChatGPT vs Claude 2025深度横评：编程、写作、推理谁更强？", "chat",
     ["ChatGPT", "Claude", "对比测评", "AI工具"], 
     "深度对比ChatGPT和Claude在编程能力、写作质量、逻辑推理方面的表现，帮你选择最适合的AI助手。", 
     "ChatGPT, Claude, AI对比, 编程能力, 写作质量, 逻辑推理"),
    ("deepseek-full-review.md", "DeepSeek V3 全方位测评：免费AI的天花板？", "chat",
     ["DeepSeek", "免费AI", "性能测评", "AI工具"],
     "DeepSeek V3作为完全免费的AI模型，其实力究竟如何？全面测试其在各项任务中的表现。",
     "DeepSeek V3, 免费AI, 性能测评, 国产AI, 大语言模型"),
    ("kimi-200w-context-test.md", "Kimi 200万字上下文实测：长文档处理真能兑现吗？", "chat",
     ["Kimi", "长文本", "上下文测试", "AI工具"],
     "Kimi宣称支持200万字上下文，实际效果如何？我们用真实长文档进行了严格测试。",
     "Kimi, 200万字上下文, 长文档处理, 上下文长度, AI对话"),
    ("ernie-vs-qwen.md", "文心一言4.0 vs 通义千问2.5：国产AI巅峰对决", "chat",
     ["文心一言", "通义千问", "国产AI", "对比测评"],
     "百度文心一言4.0和阿里通义千问2.5，谁是国产AI之王？全维度横评告诉你答案。",
     "文心一言, 通义千问, 国产AI, AI对比, 文心一言4.0, 通义千问2.5"),
    ("doubao-review.md", "豆包AI深度测评：字节跳动的AI助手值得用吗？", "chat",
     ["豆包", "字节跳动", "AI助手", "功能测评"],
     "字节跳动推出的豆包AI助手功能如何？实测其在日常使用中的表现和优缺点。",
     "豆包, 字节跳动, AI助手, 功能测评, 使用体验"),
    ("zhipu-qingyan-review.md", "智谱清言测评：学术研究最好的国产AI？", "chat",
     ["智谱清言", "学术研究", "AI测评", "知识问答"],
     "智谱AI的清言模型在学术研究场景中的表现如何？深度测试其知识理解和推理能力。",
     "智谱清言, 学术研究, AI测评, 知识问答, 智谱AI"),
    ("xunfei-xinghuo-review.md", "讯飞星火V4测评：语音AI的王者？", "chat",
     ["讯飞星火", "语音AI", "语音合成", "AI测评"],
     "讯飞星火V4在语音理解和合成方面的表现如何？全面评估其语音AI能力。",
     "讯飞星火, 语音AI, 语音合成, AI测评, 讯飞星火V4"),
    ("tencent-yuanbao-review.md", "腾讯元宝测评：企鹅家的AI助手能打几分？", "chat",
     ["腾讯元宝", "腾讯AI", "AI助手", "功能测评"],
     "腾讯推出的元宝AI助手到底值不值得使用？我们从功能、体验、生态三方面进行测评。",
     "腾讯元宝, 腾讯AI, AI助手, 功能测评, 使用体验, 腾讯生态"),
]

# AI编程类 (coding)
coding_articles = [
    ("cursor-vs-copilot.md", "Cursor vs GitHub Copilot 2025：AI编程双雄对决", "coding",
     ["Cursor", "GitHub Copilot", "AI编程", "对比测评"],
     "Cursor和GitHub Copilot两大AI编程工具究竟谁更强？我们从代码质量、易用性、价格方面进行横评。",
     "Cursor, GitHub Copilot, AI编程, 代码质量, 易用性, 价格比较"),
    ("cursor-full-review.md", "Cursor 编辑器深度测评：真的能取代VS Code吗？", "coding",
     ["Cursor", "AI编程", "VS Code替代", "功能测评"],
     "Cursor宣称自己是下一代AI编程编辑器，实际使用体验如何？能否真正取代VS Code？",
     "Cursor, AI编程, VS Code替代, 功能测评, 编辑器体验, AI代码生成"),
    ("tongyi-lingma-review.md", "通义灵码实测：阿里的AI编程助手如何？", "coding",
     ["通义灵码", "AI编程", "阿里巴巴", "代码生成"],
     "阿里巴巴推出的通义灵码在实际编程中的表现如何？支持哪些语言？代码质量怎么样？",
     "通义灵码, AI编程, 阿里巴巴, 代码生成, 编程助手, 编程语言支持"),
    ("codegeex-review.md", "CodeGeeX测评：国产免费AI编程插件", "coding",
     ["CodeGeeX", "国产AI", "免费编程", "代码补全"],
     "智谱AI推出的免费AI编程插件CodeGeeX到底怎么样？支持多少种编程语言？",
     "CodeGeeX, 国产AI, 免费编程, 代码补全, 编程插件, 智谱AI"),
    ("windsurf-review.md", "Windsurf测评：Codeium的新AI IDE", "coding",
     ["Windsurf", "Codeium", "AI IDE", "编程工具"],
     "Codeium推出的全新AI原生IDE Windsurf到底值不值得尝试？功能和性能如何？",
     "Windsurf, Codeium, AI IDE, 编程工具, AI原生, 编程体验"),
    ("trae-review.md", "Trae测评：字节跳动的AI编程工具", "coding",
     ["Trae", "字节跳动", "AI编程", "代码助手"],
     "字节跳动推出的AI编程工具Trae在实际使用中的表现如何？支持哪些功能？",
     "Trae, 字节跳动, AI编程, 代码助手, 编程工具, 字节跳动AI"),
    ("ai-coding-workflow.md", "AI编程工作流：Copilot+Cursor+终端效率指南", "coding",
     ["AI编程", "工作流", "效率提升", "编程技巧"],
     "如何结合使用GitHub Copilot、Cursor和终端命令，打造最高效的AI编程工作流？实战技巧分享。",
     "AI编程, 工作流, 效率提升, 编程技巧, Copilot, Cursor, 终端命令"),
]

# AI绘图类 (image)
image_articles = [
    ("midjourney-v6-review.md", "Midjourney V6深度测评：AI绘图还值得付费吗？", "image",
     ["Midjourney V6", "AI绘图", "付费测评", "图像生成"],
     "Midjourney V6作为目前最强的AI绘图工具，其实际表现如何？生成质量、使用体验、性价比全面分析。",
     "Midjourney V6, AI绘图, 图像生成, 生成质量, 使用体验, 性价比分析"),
    ("sd-vs-mj.md", "Stable Diffusion vs Midjourney：开源VS商业终极对比", "image",
     ["Stable Diffusion", "Midjourney", "开源AI", "商业AI", "对比测评"],
     "开源之王Stable Diffusion和商业霸主Midjourney，谁是AI绘图的真正王者？全方位横评告诉你答案。",
     "Stable Diffusion, Midjourney, 开源AI, 商业AI, AI绘图, 对比测评, 图像生成"),
    ("flux-review.md", "FLUX.1测评：开源绘图新王者？", "image",
     ["FLUX.1", "开源绘图", "AI图像", "黑森林实验室"],
     "黑森林实验室推出的FLUX.1模型到底有多强？在图像质量、遵循程度、速度方面表现如何？",
     "FLUX.1, 开源绘图, 黑森林实验室, 图像质量, 遵循程度, 生成速度, AI图像生成"),
    ("wenxin-yige-review.md", "文心一格测评：百度AI绘图工具实战", "image",
     ["文心一格", "百度AI", "AI绘图", "图像生成"],
     "百度的AI绘图工具文心一格实际能生成什么样的图片？功能、使用体验、收费情况全面测评。",
     "文心一格, 百度AI, AI绘图, 图像生成, 功能测试, 使用体验, 收费情况"),
    ("tongyi-wanxiang-review.md", "通义万相测评：阿里的AI绘图够强吗？", "image",
     ["通义万相", "阿里巴巴", "AI绘图", "多模态"],
     "阿里巴巴的通义万相在AI绘图领域到底有多少实力？支持哪些类型的图像生成？",
     "通义万相, 阿里巴巴, AI绘图, 多模态, 图像生成, 功能范围, 生成质量"),
    ("jimeng-review.md", "即梦AI测评：字节的绘图工具好用吗？", "image",
     ["即梦", "字节跳动", "AI绘图", "文字转图片"],
     "字节跳动推出的即梦AI绘图工具使用体验如何？生成质量、速度、功能完整性如何？",
     "即梦, 字节跳动, AI绘图, 文字转图片, 生成质量, 生成速度, 功能完整性"),
    ("prompt-engineering-image.md", "AI绘图Prompt工程：从入门到精通的提示词技巧", "image",
     ["Prompt工程", "AI绘图", "提示词技巧", "图像生成"],
     "想要让AI绘图工具生成理想中的图片，关键在于写好Prompt。本文详细教你AI绘图的Prompt工程技巧。",
     "Prompt工程, AI绘图, 提示词技巧, 图像生成, 提示词优化, 质量控制, 风格控制"),
]

# AI视频类 (video)
video_articles = [
    ("sora-review.md", "Sora深度测评：OpenAI的视频生成革命", "video",
     ["Sora", "视频生成", "AI视频", "OpenAI"],
     "OpenAI的Sora模型在视频生成方面到底有多强？生成质量、长度限制、实际应用场景全面测评。",
     "Sora, 视频生成, AI视频, OpenAI, 生成质量, 长度限制, 应用场景"),
    ("kling-video-review.md", "可灵AI视频测评：国产Sora来了？", "video",
     ["可灵AI", "视频生成", "国产AI", "快手"],
     "快手推出的可灵AI视频生成模型究竟怎么样？能否达到Sora的水平？实际测试告诉你答案。",
     "可灵AI, 视�生成, 国产AI, 快手, Sora替代, 生成质量, 应用场景"),
    ("runway-gen3-review.md", "Runway Gen-3测评：专业视频AI工具", "video",
     ["Runway Gen-3", "专业视频", "AI视频", "视频编辑"],
     "Runway Gen-3作为专业级AI视频工具，在视频生成、编辑、特效方面表现如何？值得专业人士使用吗？",
     "Runway Gen-3, 专业视频, AI视频, 视频编辑, 视频生成, 特效生成, 专业工具"),
    ("jimeng-video-review.md", "即梦视频测评：字节的AI视频生成器", "video",
     ["即梦视频", "字节跳动", "AI视频", "文字转视频"],
     "字节跳动的即梦AI视频生成器能生成什么样的视频？质量、长度、使用体验如何？",
     "即梦视频, 字节跳动, AI视频, 文字转视频, 生成质量, 视频长度, 使用体验"),
    ("pika-vs-luma.md", "Pika vs Luma：AI视频生成工具对比", "video",
     ["Pika", "Luma", "AI视频", "对比测评", "视频生成"],
     "Pika和Luma两大AI视频生成工具究竟谁更强？我们从生成质量、控制程度、使用难度方面进行横评。",
     "Pika, Luma, AI视频, 视频生成, 对比测评, 生成质量, 控制程度, 使用难度"),
]

# 新手教学 (tutorial-beginner)
tutorial_beginner_articles = [
    ("ai-beginner-guide.md", "AI新手入门指南：2025年零基础使用AI工具全攻略", "tutorial-beginner",
     ["AI入门", "零基础指南", "使用教程", "新手入门"],
     "完全零基础的你，如何从零开始学习使用AI工具？从注册选择到基础使用，一步步教你成为AI使用者。",
     "AI入门, 零基础指南, 使用教程, 新手入门, AI工具选择, 基础使用, 注册流程"),
    ("prompt-101.md", "Prompt入门：写好AI提示词的5个黄金法则", "tutorial-beginner",
     ["Prompt入门", "提示词技巧", "AI使用基础", "有效沟通"],
     "想让AI更好地理解你的需求？掌握这5个Prompt写作黄金法则，让你的AI使用效率瞬间提升。",
     "Prompt入门, 提示词技巧, AI使用基础, 有效沟通, 提示词写法, AI沟通, 交流技巧"),
    ("ai-tools-setup.md", "手把手教你注册ChatGPT和Claude（含国内访问）", "tutorial-beginner",
     ["ChatGPT注册", "Claude注册", "国内访问", "工具设置"],
     "在国内如何顺利注册和使用ChatGPT和Claude？详细步骤解析，包括网绢环境、验证方法、常见问题解决。",
     "ChatGPT注册, Claude注册, 国内访问, 工具设置, 注册教程, 使用准备, 常见问题"),
]

# 进阶教学 (tutorial-advanced)
tutorial_advanced_articles = [
    ("structured-prompt.md", "结构化Prompt工程：角色+任务+约束+格式体系", "tutorial-advanced",
     ["结构化Prompt", "Prompt工程", "高级技巧", "AI使用进阶"],
     "想要让AI精准理解复杂需求？结构化Prompt方法论帮你系统化地构建提示词，显著提升AI输出质量。",
     "结构化Prompt, Prompt工程, 高级技巧, AI使用进阶, 角色设定, 任务描述, 约束条件, 格式要求"),
    ("ai-workflow-automation.md", "AI工作流自动化：用AI串联你的日常任务", "tutorial-advanced",
     ["工作流自动化", "AI自动化", "任务串联", "效率提升"],
     "如何利用AI工具自动化处理重复性日常任务？从电子邮件处理到数据分析，打造你的AI工作流。",
     "工作流自动化, AI自动化, 任务串联, 效率提升, 任务自动化, 流程优化, 日常任务"),
    ("multi-ai-strategy.md", "多AI协作策略：ChatGPT+Claude+Kimi组合拳", "tutorial-advanced",
     ["多AI协作", "策略组合", "工具组合", "使用技巧"],
     "为什么要同时使用多个AI工具？不同AI工具的优势互补如何帮你在不同场景中发挥最大价值？",
     "多AI协作, 策略组合, 工具组合, 使用技巧, 工具互补, 场景选择, 资源分配"),
]

# 大师教学 (tutorial-master)
tutorial_master_articles = [
    ("rag-build-guide.md", "RAG从0到1：搭建你的私有知识库问答系统", "tutorial-master",
     ["RAG技术", "知识库", "问答系统", "高级应用"],
     "想要让AI回答基于你私有文档的问题？RAG技术帮你构建专属的知识库问答系统，从原理到实现全流程指南。",
     "RAG技术, 知识库, 问答系统, 高级应用, 检索增强生成, 私有知识库, 文档处理, 向量数据库"),
    ("ai-agent-build.md", "AI Agent实战：从概念到搭建你的第一个智能体", "tutorial-master",
     ["AI Agent", "智能体", "自主AI", "高级应用"],
     "想要创建能自主执行任务的AI智能体吗？从理论概念到实际代码，手把手教你搭建第一个AI Agent。",
     "AI Agent, 智能体, 自主AI, 高级应用, 智能体架构, 任务规划, 工具使用, 自主决策"),
]

# 合并所有文章
articles.extend(chat_articles)
articles.extend(coding_articles)
articles.extend(image_articles)
articles.extend(video_articles)
articles.extend(tutorial_beginner_articles)
articles.extend(tutorial_advanced_articles)
articles.extend(tutorial_master_articles)

# 生成文章内容的函数
def generate_article_content(title, categories, tags, description, keywords):
    # 确保categories是列表
    if isinstance(categories, str):
        categories = [categories]
    
    content = f"""---
layout: post
title: "{title}"
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} +0800
categories: [{', '.join(categories)}]
tags: [{', '.join(tags)}]
description: "{description}"
keywords: "{keywords}"
---

# {title}

## 摘要

{description}

## 正文内容

在这篇文章中，我们将深入探讨{title.split()[0]}的各个方面。通过真实测试、对比分析和实用技巧分享，帮你全面了解这个话题。

### 一、背景介绍

{title.split()[0]}当前正处于快速发展阶段，新功能和改进层出不穷。了解其核心特点和使用方法，对于提高工作效率和解决实际问题至关重要。

### 二、详细测评与分析

#### 功能特点
- **核心功能**：{title.split()[0]}提供了哪些主要功能？
- **使用场景**：适合哪些具体的应用场景？
- **操作难度**：新手友好程度如何？学习曲线陡峭还是平缓？

#### 性能表现
- **响应速度**：在不同任务下的响应时间如何？
- **准确率**：在专业任务中的准确性表现？
- **稳定性**：长时间使用过程中的稳定性如何？

#### 对比测试
我们进行了横向对比测试，主要比较维度包括：
- 功能完整性
- 使用便利性  
- 性价比
- 技术支持
- 更新频率

#### 真实案例分享
下面是一些基于真实使用场景的案例：

**案例1：日常办公应用**
- 场景描述：[具体场景]
- 使用工具：[具体工具名称]
- 处理时间：[对比传统方法所需时间]
- 输出质量：[输出结果评估]
- 使用感受：[主观体验描述]

**案例2：专业技术应用**
- 场景描述：[具体场景]
- 使用工具：[具体工具名称]
- 处理时间：[对比传统方法所需时间]
- 输出质量：[输出结果评估]
- 使用感受：[主观体验描述]

### 三、优缺点总结

#### 主要优势
1. [优势1：具体描述]
2. [优势2：具体描述]
3. [优势3：具体描述]
4. [优势4：具体描述]

#### 需要改进的地方
1. [不足1：具体描述]
2. [不足2：具体描述]
3. [不足3：具体描述]
4. [不足4：具体描述]

#### 适用人群推荐
- **新手用户**：[是否推荐及理由]
- **中级用户**：[是否推荐及理由]
- **专业用户**：[是否推荐及理由]
- **企业用户**：[是否推荐及理由]

### 四、使用建议与技巧

#### 基础使用技巧
- 技巧1：[具体技巧描述]
- 技巧2：[具体技巧描述]
- 技巧3：[具体技巧描述]

#### 进阶使用方法
- 方法1：[具体方法描述]
- 方法2：[具体方法描述]
- 方法3：[具体方法描述]

#### 常见问题解答
**Q：[常见问题1]？**
A：[详细解答]

**Q：[常见问题2]？**
A：[详细解答]

### 五、结论与展望

{title.split()[0]}目前处于[发展阶段]，在[优势领域]表现出色，但在[不足领域]仍有提升空间。对于[目标用户群体]，我们给出以下建议：

- [建议1]
- [建议2]
- [建议3]

展望未来，我们期待{title.split()[0]}在[发展方向]方面有更多突破和创新。

---
*本文基于最新版本进行测试和评估，具体功能和性能可能随版本更新而变化。建议用户参考官方文档获取最准确信息。*
"""
    return content

# 生成所有文章
print(f"开始生成 {len(articles)} 篇文章到 {POSTS_DIR}")

for i, (filename, title, categories, tags, description, keywords) in enumerate(articles):
    # 计算日期：从start_date开始，每篇文章递增一天
    article_date = start_date + timedelta(days=i)
    date_str = article_date.strftime("%Y-%m-%d")
    
    # 生成内容
    content = generate_article_content(title, categories, tags, description, keywords)
    
    # 构建完整文件路径
    filepath = os.path.join(POSTS_DIR, f"{date_str}-{filename}")
    
    # 写入文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"已生成: {os.path.basename(filepath)} - {title}")

print("所有文章生成完成！")