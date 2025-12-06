# <span style="color:#00FF55; font-family:Consolas,monospace;">Fwogx402 · 两栖链上人工智能系统</span>

<img src="assets/Fwogx402.png" alt="Fwogx402 标志" width="260"/>

> <span style="color:#33FF77;">这一仓库不是单一合约或者单一模型的代码集合, 而是围绕 Fwogx402 构建的完整研究环境。</span>

Fwogx402 试图回答一个具体问题:

<span style="color:#00EE55;">如果一个模因在 BNB 生态中不再只是头像和图片, 而被当作严肃的计算对象对待, 它可以被实现成什麽样的系统。</span>

本仓库包含协议设计, 仿真框架, 叙事引擎, 威胁模型, 神经模块以及链上集成层。  
所有文件与文档均以研究为导向, 不承诺任何收益, 不鼓励任何形式的盲目使用资金。

---

## <span style="color:#00DD55;">一 名称与符号</span>

### 1.1 Fwog

在 BNB 社区中, fwog 是一种广泛传播的青蛙模因。  
在本项目中, fwog 被赋予了新的含义:

- 作为链上事件的边缘观测者  
- 作为资金流, 情绪与叙事之间的翻译器  
- 作为两栖智能体的视觉化符号  

### 1.2 402

402 在链上文化中通常被视为高风险和高波动的代号。  
在架构内部, 402 被定义为一组关于风险预算与流动性敏感度的参数向量。

### 1.3 项目名 Fwogx402

Fwogx402 表示  
fwog 这一模因与 402 型参数族的交叉组合,  
既指代具体的仓库, 也指代一整套实验性协议与工具链。

---

## <span style="color:#00CC55;">二 架构总览</span>

从宏观角度看, Fwogx402 拆分为四个层级:

1. 感知层 Perception Layer  
2. 决策层 Decision Layer  
3. 执行层 Execution Layer  
4. 叙事层 Narrative Layer  

四个层级围成一个闭环:

> 区块数据 → 特征图 → 意图 → 约束执行 → 事件压缩 → 回写记忆

```text
[链上事件]  ──>  [感知层: 过滤与编码]
              ↓
          [决策层: 多模型投票]
              ↓
          [执行层: 受约束行为]
              ↓
          [叙事层: 文字与图形输出]
              ↺
```

每一轮循环都被记录为一帧时间片, 用于重放与安全分析。

---

## <span style="color:#00CC44;">三 目录与模块说明</span>

项目结构保持高度模块化, 方便选择性启用。

```text
Fwogx402/
│
├── assets/                 项目标志与可视化素材
│     └── Fwogx402.png
│
├── src/                    两栖智能体的核心实现
│     ├── core.py           主循环与模式切换
│     ├── meme_adapter.py   模因情绪适配器
│     ├── liquidity.py      流动性观测与评分
│     ├── policy_router.py  策略路由与风险模板
│     └── telemetry.py      运行时指标与日志
│
├── docs/                   高层文档
│     ├── overview.md       总览与设计动机
│     ├── architecture.md   各层级详细说明
│     └── green_theory.md   “绿色理论”与两栖概念
│
├── research/               研究记录与假设
│     ├── amphibious_dynamics.md   两栖动态模型
│     ├── meme_signal_models.md    模因信号建模
│     └── risk_budgeting.md        风险预算实验
│
├── simulation/             仿真与重放框架
│     ├── engine.py
│     ├── replay.py
│     └── liquidity_scenarios.md
│
├── onchain/                链上参考合约
│     ├── FwogGuardian.sol
│     ├── LiquiditySentinel.sol
│     └── MemeOracle.sol
│
├── neural_models/          神经网络与编码器
│     ├── fwog_encoder.py
│     ├── vector_memory.py
│     └── chain_feature_model.py
│
├── meme_lab/               模因实验室
│     ├── fwog_shock_tests.md
│     ├── cultural_inference.py
│     └── narrative_mutation_engine.py
│
├── benchmarks/             基准与开销分析
│     ├── stress_profiles.md
│     └── compute_costs.md
│
└── threat_analysis/        威胁建模与防御
      ├── attack_surface.md
      ├── behavioral_anomalies.md
      └── containment_strategies.md
```

任何目录都可以单独使用, 也可以组合成完整管线。

---

## <span style="color:#00BB55;">四 感知层</span>

感知层的目标是“听得到链上的细语”。  
其输入包括:

- 区块高度, 时间戳, gas 使用情况  
- 特定合约与池子的事件流  
- 跨平台价格与成交深度  
- 外部情绪与文本源的摘要结果  

感知层会将这些信息编码成稀疏张量与结构化特征。

```python
class Perception:
    def capture_block_view(self) -> dict:
        return {
            "height": ...,
            "gas_usage": ...,
            "contracts": [...],
            "pools": [...],
        }

    def encode(self, raw: dict) -> "StateView":
        # 这里会进行归一化, 滑动窗口, 异常值处理
        ...
```

在设计上, 感知层不直接产生任何交易意图  
只负责构建多维状态视图 StateView。

---

## <span style="color:#00AA55;">五 决策层与意图引擎</span>

决策层由三类模型共同组成:

1. 统计与贝叶斯模型, 用于估计风险分布  
2. 序列模型, 对价格与流动性时间序列进行建模  
3. 模因情绪编码模型, 对文本与文化信号进行压缩  

最终输出被统一包装为 Intent 对象:

```text
Intent {
    StateView state          当前状态视图
    RiskBudget budget        风险预算
    Tag[] narrative_tags     叙事标签
    Constraint[] rules       执行约束
}
```

伪代码示意:

```python
from fwogx402.policy_router import PolicyRouter

router = PolicyRouter()

def propose_intent(state_view):
    candidates = router.collect_candidates(state_view)
    scored = router.score_candidates(state_view, candidates)
    chosen = router.apply_risk_filters(scored)
    intent = router.materialize_intent(state_view, chosen)
    return intent
```

此处的关键设计是  
任何自动化行为在进入执行层前都必须被显式编码为 Intent,  
并在日志中完整记录。

---

## <span style="color:#009955;">六 执行层与约束系统</span>

执行层的角色非常单一:

- 接收 Intent  
- 检查约束  
- 在白名单合约上执行操作  
- 将结果写入不可变日志  

约束系统覆盖以下维度:

- 单笔最大名义仓位  
- 一定时间窗口内最大操作次数  
- 白名单合约与方法  
- 停机开关与冷却时间  

所有执行逻辑都以“先求活下来”为优先原则设计。  
当链上状态异常时, 执行层会自动切换为只读模式。

---

## <span style="color:#008855;">七 叙事层与输出</span>

叙事层是 Fwogx402 与人类交互的主要界面。  
它会从以下对象中提取信息:

- StateView  
- Intent  
- 执行结果  
- 历史轨迹与回测记录  

然后生成多种形式的输出:

- 时间线式事件摘要  
- 风险与仓位变化图  
- 针对特定行为的自然语言解释  
- 与模因相关的短文本片段  

叙事层遵循三条原则:

1. 不夸大收益  
2. 不隐藏风险  
3. 不制造虚构的确定性  

---

## <span style="color:#007755;">八 仿真与重放框架</span>

`simulation` 目录提供了可复现的实验环境。  

主要功能:

- 回放历史区块与订单簿  
- 在不同策略与风险模板下进行长周期实验  
- 搜集在极端情形下 Fwogx402 的行为特征  

示例用法:

```python
from simulation.engine import SimulationEngine
from fwogx402.core import AmphibiousCore

core = AmphibiousCore(mode="dry_run")
engine = SimulationEngine(core=core)

engine.load_history("data/bnb_history.parquet")
engine.run(days=90)
engine.export_report("out/report_90d.json")
```

仿真结果可直接供 `benchmarks` 与 `threat_analysis` 使用。

---

## <span style="color:#006655;">九 链上集成与安全假设</span>

`onchain` 目录中的合约是为了说明架构思路而提供的参考实现。

- `FwogGuardian.sol`  
  管理角色与权限, 记录所有关键操作的调用轨迹  

- `LiquiditySentinel.sol`  
  监控指定池子与合约的流动性变化,  
  当检测到异常模式时发出警告事件  

- `MemeOracle.sol`  
  将外部计算得到的情绪指数写入链上,  
  供策略在需要时参考  

安全假设包括:

- 节点可能失联  
- 数据源可能失败  
- 模型可能误判  

因此, 所有真实资金环境中的使用场景  
都必须额外进行审计与压力测试。

---

## <span style="color:#005555;">十 威胁分析与异常行为</span>

`threat_analysis` 目录记录了若干场景:

- 大规模情绪操纵与虚假舆论注入  
- 利用节点差异与网络延迟的时间套利  
- 模型被极端数据驱动到不稳定区域  
- 多智能体之间形成错误的自我强化共识  

每一类场景都附带:

- 假设前提  
- 攻击路径  
- 潜在影响  
- 建议的缓解与隔离措施  

目标不是证明 Fwogx402 是安全的,  
而是让所有潜在危险被看见, 被记录, 被讨论。

---

## <span style="color:#004444;">十一 研究议题</span>

当前进行中的研究问题包括但不限于:

1. 模因情绪是否可以作为风险控制信号而不仅是噪声  
2. 当社交数据与链上数据给出相反意见时, 如何进行聚合  
3. 叙事层是否能够显著降低黑箱感与误解  
4. 多策略并行时, 如何避免模式崩塌与过度拟合  
5. 两栖架构在极端波动环境中的恢复时间分布  

对应文档位于 `research` 目录, 会随着实验推进不断更新。

---

## <span style="color:#003333;">十二 本地部署与运行</span>

### 12.1 环境要求

- Python 3.11 或更新版本  
- 只读或小额资金的 BNB 钱包  
- 可用的公共 BNB 节点或自建节点  

### 12.2 安装步骤

```bash
git clone https://github.com/your-account/Fwogx402.git
cd Fwogx402

python -m venv venv
source venv/bin/activate      # Windows 使用 venv\Scripts\activate

pip install -r requirements.txt
```

### 12.3 观测模式

观测模式下不会发送任何链上交易, 仅输出决策与解释。

```bash
python src/core.py --mode observe
```

你将看到:

- 当前监测到的链上片段  
- 内部生成但未执行的 Intent  
- 叙事层对这些 Intent 的解释摘要  

---

## <span style="color:#002222;">十三 贡献指南</span>

欢迎任何严肃的贡献形式, 包括:

- 编写更清晰的文档与图示  
- 提出新的观测指标和风险度量方式  
- 引入不同风格的策略与模型, 前提是可解释  
- 对现有安全假设提出质疑与反例  

在提交 Pull Request 之前, 建议做到:

1. 新增模块附带最小可运行示例  
2. 公共接口提供类型标注与文档字符串  
3. 所有策略可在仿真环境中重放  
4. 对可能的攻击面进行最基本的思考  

---

## <span style="color:#001111;">十四 免责声明</span>

Fwogx402 是一个以研究为目的的开源项目。  

- 不提供任何形式的投资建议  
- 不对任何资金损失承担责任  
- 不鼓励在未经过审计的情况下将本仓库中的代码直接用于生产环境  

如果你选择在真实资金环境中实验本项目中的任何思路,  
请自行承担全部风险, 并确保你对系统行为有足够理解。

---

<span style="color:#00FF55;">Fwogx402 的目标不是成为工具。</span>  
它更接近一台被公开拆解的理论机器,  
邀请所有对“模因, 协议与人工智能交汇点”感兴趣的人  
一起观察, 一起拆解, 一起修正。
