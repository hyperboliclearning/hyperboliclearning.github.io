# 网站链接检查 · 2026-10-06

本次扫描了生成站点中的 15 个 HTML 页面，检查 123 个站内链接和锚点，以及 348 个去重后的外部链接。站内路径在修改后复查，未发现缺失的链接目标或锚点。

使用 arXiv 官方 API 批量核对了 158 篇论文的标题；另外通过 Crossref 元数据核对了 19 个出版记录。短模型名称、章节中的描述性链接以及旧版论文标题，需要结合原论文核对，不能仅凭字符串相似度判定错链。

## 已修复

| 位置 | 问题 | 处理 |
| --- | --- | --- |
| 首页 News · HypRAG | 错误地指向另一篇论文的 arXiv 编号 2405.03188 | 更新为 [2602.07739](https://arxiv.org/abs/2602.07739)，标题与原论文一致 |
| Collection · WWW 2022 tutorial | 原教程网址返回 404 | 改为 [会议官方归档](https://archives.iw3c2.org/www2022/tutorials/) |
| Collection · KDD 2022 tutorial | 原域名无法访问 | 改为 [作者维护的教程页面](https://creddy.net/TUTORIAL/Hyperbolic/kdd-2022/index.html) |
| Collection · Mixed-Curvature Multi-relational Graph Neural Network | 原 PDF 直链返回 404 | 改为 [Amazon Science 论文页面](https://www.amazon.science/publications/mixed-curvature-multi-relational-graph-neural-network-for-knowledge-graph-completion) |
| Collection · Hyperbolic Representations of Source Code | 原 PDF 直链返回 404 | 改为 [Amazon Science 论文页面](https://www.amazon.science/publications/hyperbolic-representations-of-source-code)，并明确标注 AAAI 2022 Workshop |
| Collection · Searching for Actions on the Hyperbole | IEEE PDF 入口无法获取 | 改为 [CVPR 官方开放论文页面](https://openaccess.thecvf.com/content_CVPR_2020/html/Long_Searching_for_Actions_on_the_Hyperbole_CVPR_2020_paper.html) |
| WWW 2025 workshop | 原会议域名无法获取 | 两处链接改为 [IW3C2 官方归档](https://archives.iw3c2.org/www2025/) |
| Keynote | 链接指向仓库中不存在的 keynote.pdf | 移除失效链接，注明 slides 当前不可用 |
| Collection · arXiv:2201.12825 | 列出的旧标题与当前论文页面不同 | 更新为当前标题 Autoencoding Hyperbolic Representation for Adversarial Generation |

Collection 中 2310.18209v1 的旧标题与指定 v1 页面匹配，因此保留其版本链接和标题。

## 检查限制

HTTP 状态只能帮助识别失效入口，不能证明论文内容正确。外链首次扫描返回 299 个 HTTP 200、34 个 403、3 个 404、5 个连接错误、2 个 202、1 个 502、3 个 203、1 个 429。上述已修复项包含这些失败记录；部分受限制的出版页面通过官方元数据核对了标题。

其中 32 个 OpenReview 链接返回浏览器验证页面；其 API 同样限制了本次访问。其他出版商、社交和资料网站也有访问限制或临时限流，不能据此当作坏链接，更不能声称这些页面的内容已经全部核验。保留这些有待人工查看的外链，未自动删改。
