# openpaper

kn1ghtc 的**公开**论文演示与写作统一仓库。安全/密码学/AI 相关研究论文的可复现演示代码、公开可读的写作草稿，从本仓库统一管理、公开托管。

## 定位与协作模式

- **可见性**：Public，任何人都可以 `git clone` / 下载 / Fork / 阅读全部内容。
- **协作权限**：仅仓库所有者（`kn1ghtc`）及其显式邀请的协作者拥有写权限（push / merge）。**不接受未经邀请的直接 push**；如需贡献，请通过 Fork + Pull Request 提出，由维护者审阅后合并。
- **不是** `kctsb` / `NetPenetration` / `llm` / `gamecenter` 等私有工作区子项目的镜像或导出；本仓库只包含**可独立复现**的公开内容。

## 目录约定

每篇论文 / 每个研究子课题一个独立子目录：

```text
openpaper/
├── <paper-or-project-slug>/
│   ├── README.md          # 该子项目说明、来源、复现步骤
│   ├── paper.md            # 论文正文（Markdown，可选 LaTeX 构建产物）
│   ├── demo/                # 可独立运行的演示/验证代码
│   └── data/                 # 可公开分发的数据（不含任何私有/内部数据）
└── prompt-engineering-research/   # 首个子项目：跨厂商系统提示词泄露归档
```

## 密码学演示代码规范（强制）

本仓库任何涉及密码学算法验证、基准测试或论文配图复现的代码：

1. **必须**通过 `pip install kctsb` 使用官方发布在 PyPI 上的公共包 API 调用（<https://pypi.org/project/kctsb/>），例如：

   ```bash
   pip install kctsb
   ```

   ```python
   import kctsb
   from kctsb import ckks, bfv, bgv, ecc_blind_sign, mpc, psi, pir, sss, voprf, abe
   ```

2. **禁止**直接复制、内联或以任意方式引用私有仓库 `kctsb`（源码仓库）中未发布的实现细节、内部路径、内部脚本或未公开的分支代码。所有验证必须建立在**任意第三方**都能通过 `pip install kctsb` 独立获得的公共接口之上。
3. 如果某篇论文的验证代码**不使用** `kctsb`：
   - 必须自包含（self-contained），依赖项全部来自 PyPI/npm 等公共源并在 `requirements.txt` / `pyproject.toml` 中声明；
   - **禁止**引用本工作区任何私有仓库（`kctsb`、`NetPenetration`、`llm`、`gamecenter`、`extensions/kc-devkit` 等）的内部代码、内部 API、内部数据或私有路径；
   - 任何第三方 clone 本仓库后，仅凭 README 中的步骤即可在无额外私有权限的情况下完整运行并验证结果。
4. 提交前自检清单：
   - [ ] 代码中没有 `D:\pyproject\kctsb` 或其他工作区绝对路径；
   - [ ] 没有 `import` 私有仓库内部模块（非 `pip install kctsb` 之外的路径）；
   - [ ] `pip install -r requirements.txt` 后可在全新环境跑通 demo；
   - [ ] 没有任何内部/未公开的密钥、令牌、测试账号、内部域名。

## 子项目索引

| 子目录 | 说明 |
|---|---|
| [`prompt-engineering-research/`](prompt-engineering-research/README.md) | 跨厂商系统提示词（system prompt）泄露 / 官方公开归档，按厂商分类，逐条独立 Markdown 存档，供提示词工程与 LLM 安全研究使用 |

## 许可证

- 代码：[MIT License](LICENSE)。
- `prompt-engineering-research/` 内归档的第三方系统提示词文本版权归其原始模型厂商所有，本仓库仅作研究引用与来源标注，不主张任何权利；详见该子目录 README 的来源与免责声明。

## 赞助与关联仓库

- 本账号私有仓库赞助访问：<https://github.com/sponsors/kn1ghtc>
- 相关私有研究仓库（非本仓库镜像，按赞助等级只读）：`kctsb`（$10/月起）、`NetPenetration`（$50/月起）
