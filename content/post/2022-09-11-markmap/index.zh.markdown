---
title: 检验.Rmarkdwon格式下mermaid和markmap和table
author: Wcl
date: '2022-09-11'
slug: markmap
categories: []
tags: []
subtitle: ''
summary: '测试.Rmarkdown后缀的rmd文件，markmap，mermaid和图表的状态'
authors: []
lastmod: '2022-09-11T20:04:59+08:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
---

mermaid这种格式可以直接成功

```mermaid
graph TD;
  A-->B;
  A-->C;
  B-->D;
  C-->D;
```

这样不行

```markmap
- Hugo Modules
  - wowchemy
  - wowchemy-plugins-netlify
  - wowchemy-plugins-netlify-cms
  - wowchemy-plugins-reveal
```

加code可以让格式不变，可以运行成功

{{%markmap%}}
<code>
- Hugo Modules
  - wowchemy
  - wowchemy-plugins-netlify
  - wowchemy-plugins-netlify-cms
  - wowchemy-plugins-reveal
</code>
{{%/markmap%}}

```mermaid
sequenceDiagram
  participant Alice
  participant Bob
  Alice->John: Hello John, how are you?
  loop Healthcheck
      John->John: Fight against hypochondria
  end
  Note right of John: Rational thoughts <br/>prevail...
  John-->Alice: Great!
  John->Bob: How about you?
  Bob-->John: Jolly good!
```

table不行

  table path=\"2_student_info.csv\" header=\"true\" caption=\"Table 1: My results\" 
