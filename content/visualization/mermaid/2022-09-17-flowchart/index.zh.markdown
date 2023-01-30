---
title: 流程图
author: admin
date: '2022-09-17'
slug: flowchart
categories: []
tags: []
subtitle: ''
summary: '介绍了流程图的结点(node)，箭头，子图，以及各个部分的style设置'
authors: []
lastmod: '2022-09-17T19:09:25+08:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
type: book
weight: 20
---

## 甘特图的组成

主要分为四个部分来介绍

* 结点：结点的形状，**交互**，使用icon，使用特殊字符
* 箭头：箭头的虚实，中间插入文本，跨越阶数，箭头
* 风格：id，class，风格设置参数
* 整体：整体的朝向，子图

## 结点设置

{{%callout warning%}}不要将单词“end”作为流程图节点。大写所有或任何一个字母，以保持流程图不会被中断{{%/callout%}}

### 只设置id

```
flowchart LR
  start --> stop
```

```mermaid
flowchart LR
    start --> strp
```

### 设置id以及文本

```
flowchart LR
  A[start] --> B[stop]
```

```mermaid
flowchart LR
  A[start] --> B[stop]
```

id后根据括号格式的不同可以生成不同的形状

<table>
<thead>
<tr>
<td>格式</td>
<td>显示</td>
</tr>
</thead>
<tbody>
<tr>
<td><code>id(a)</code>四角稍有弧度</td>
<td>
<div class="mermaid">
flowchart LR
  id(a)
</div>
</td>
</tr>
<tr>
<td><code>id([a])</code>左右两边为半圆</td>
<td>
<div class="mermaid">
flowchart LR
  id([a])
</div>
</td>
</tr>
</tr>
<tr>
<td><code>id[[a]]</code>子例程的形状</td>
<td>
<div class="mermaid">
flowchart LR
  id[[a]]
</div>
</td>
</tr>
<tr>
<td><code>id[(a)]</code>圆柱体</td>
<td>
<div class="mermaid">
flowchart LR
  id[(a)]
</div>
</td>
</tr>
<tr>
<td><code>id((a))</code>圆形</td>
<td>
<div class="mermaid">
flowchart LR
  id((a))
</div>
</td>
</tr>
<tr>
<td><code>id>a]</code>不相称的形状</td>
<td>
<div class="mermaid">
flowchart LR
  id>a]
</div>
</td>
</tr>
<tr>
<td><code>id{a}</code>菱形</td>
<td>
<div class="mermaid">
flowchart LR
  id{a}
</div>
</td>
</tr>
<tr>
<td><code>id{{a}}</code>六边形</td>
<td>
<div class="mermaid">
flowchart LR
  id{{a}}
</div>
</td>
</tr>
<tr>
<td><code>id[\a\]</code>平行四边形</td>
<td>
<div class="mermaid">
flowchart LR
  id[\a\]
</div>
</td>
</tr>
<tr>
<td><code>id[/a/]</code>平行四边形</td>
<td>
<div class="mermaid">
flowchart LR
  id[/a/]
</div>
</td>
</tr>
<tr>
<td><code>id[\a/]</code>梯形</td>
<td>
<div class="mermaid">
flowchart LR
  id[\a/]
</div>
</td>
</tr>
<tr>
<td><code>id[/a\]</code>梯形</td>
<td>
<div class="mermaid">
flowchart LR
  id[/a\]
</div>
</td>
</tr>
<tr>
<td><code>id(((a)))</code>同心圆</td>
<td>
<div class="mermaid">
flowchart LR
  id(((a)))
</div>
</td>
</tr>
<tbody>
</table>

**文本可以加上双引号来避免某些格式的误会**

还可以添加某些特殊字符

```
flowchart LR
    A["A double quote:#quot;"] -->B["A dec char:#9829;"]
```

```mermaid
flowchart LR
    A["A double quote:#quot;"] -->B["A dec char:#9829;"]
```

### 文本的交互

主要是插入链接，语法为`click nodeId callback`或`click nodeId call callback()`或`click nodeId href`,callback是一个自定义的javascript函数，href是一个网页链接，javascript的不详细解释了，见[交互](https://mermaid-js.github.io/mermaid/#/flowchart?id=interaction)

```
flowchart LR
    A-->B
    B-->C
    C-->D
    D-->E
    click A "https://www.github.com" "_blank"
```

```mermaid
flowchart LR
    A-->B
    B-->C
    C-->D
    D-->E
    click A "https://www.github.com" "_blank"
```

### 添加icon

可以从fontawesome添加icon`fa:#icon class name#`.

```
flowchart TD
    B["fab:fa-twitter for peace"]
    B-->C[fa:fa-ban forbidden]
    B-->D(fa:fa-spinner);
    B-->E(A fa:fa-camera-retro perhaps?)
```

```mermaid
flowchart TD
    B["fab:fa-twitter for peace"]
    B-->C[fa:fa-ban forbidden]
    B-->D(fa:fa-spinner);
    B-->E(A fa:fa-camera-retro perhaps?)
```

## 箭头

结点是存在等阶（rank）的，正常`-->`或`---`或`-.-`或`===`即三个代表下一阶（带箭头的虚线表示比较特殊），每多一个符号，多一个阶，比如`---->`和`-----`表示下三个阶，结点之间的线会被拉长。

箭头形式以及相应等阶书写方式如下图所示。

<table>
<thead>
<tr>
<th>Length</th>
<th align="center">1</th>
<th align="center">2</th>
<th align="center">3</th>
</tr>
</thead>
<tbody><tr>
<td>Normal</td>
<td align="center"><code>---</code></td>
<td align="center"><code>----</code></td>
<td align="center"><code>-----</code></td>
</tr>
<tr>
<td>Normal with arrow</td>
<td align="center"><code>--&gt;</code></td>
<td align="center"><code>---&gt;</code></td>
<td align="center"><code>----&gt;</code></td>
</tr>
<tr>
<td>Thick</td>
<td align="center"><code>===</code></td>
<td align="center"><code>====</code></td>
<td align="center"><code>=====</code></td>
</tr>
<tr>
<td>Thick with arrow</td>
<td align="center"><code>==&gt;</code></td>
<td align="center"><code>===&gt;</code></td>
<td align="center"><code>====&gt;</code></td>
</tr>
<tr>
<td>Dotted</td>
<td align="center"><code>-.-</code></td>
<td align="center"><code>-..-</code></td>
<td align="center"><code>-...-</code></td>
</tr>
<tr>
<td>Dotted with arrow</td>
<td align="center"><code>-.-&gt;</code></td>
<td align="center"><code>-..-&gt;</code></td>
<td align="center"><code>-...-&gt;</code></td>
</tr>
</tbody></table>

### 在箭头之间插入文本

两种方式

* 在箭头中间插入，但是前面箭头字符个数必须小于下一等阶的字符个数，因为text不是下一阶，后面箭头字符个数决定了b的位置,dotted arrow特殊，后面从点开始,下一阶是多加一个点

```
flowchart LR
  a -. text ..-> b
```

```mermaid
flowchart LR
  a -. text ..-> b
```

* 在箭头之后的\|\|之间插入文本，文本前后箭头格式一致，不可以设置text的位置

```
flowchart LR
  a ===>|text| b
```

```mermaid
flowchart LR
  a ===>|text| b
```

### 链式文本

```
flowchart LR
   A -- text --> B -- text2 --> C
```

```mermaid
flowchart LR
   A -- text --> B -- text2 --> C
```

**逻辑关系**

```
flowchart LR
   a --> b & c--> d
```

```mermaid
flowchart LR
   a --> b & c--> d
```

```
flowchart LR
  a & b --> c & d
```

```mermaid
flowchart LR
  a & b --> c & d
```

### new arrow

在两边加上不同的符号

```
flowchart LR
   a --o b
```

```mermaid
flowchart LR
   a --o b
```

```
flowchart LR
   a o--x b
```

```mermaid
flowchart LR
   a o--x b
``` 

## 风格设置

### 链接风格

`linkStyle 3 stroke:#ff3,stroke-width:4px,color:red;`

设置第四个链接的style

### 根据id设置node

```
flowchart LR
    id1(Start)-->id2(Stop)
    style id1 fill:#f9f,stroke:#333,stroke-width:4px
    style id2 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
```

```mermaid
flowchart LR
    id1(Start)-->id2(Stop)
    style id1 fill:#f9f,stroke:#333,stroke-width:4px
    style id2 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
```

### 根据class设置

先为node设置类，`class nodeId1,nodeID2 classname`可以为多个id的node设置同一个class，或者通过`:::`符号，然后通过`classDef className fill:#f9f,stroke:#333,stroke-width:4px;`设置style,如下:

```
flowchart LR
    A:::someclass --> B
    classDef someclass fill:#f96;
```

```mermaid
flowchart LR
    A:::someclass --> B
    classDef someclass fill:#f96;
```

通过设置`classDef default fill:#f9f,stroke:#333,stroke-width:4px;`为所有未特殊指定类的node设置默认格式

## 全局设置

### 注释

`%%text`

```
flowchart LR
%% this is a comment A -- text --> B{node}
   A -- text --> B -- text2 --> C
```

### 方向

`flowchart #direction#`,direction可选有:

    TB - top to bottom
    TD - top-down/ same as top to bottom
    BT - bottom to top
    RL - right to left
    LR - left to right

### 子图

* 子图还可以嵌套子图，通过end表示结束
* 子图可以和node，子图相连接
* 子图也可以设置id和title
* 子图也可以设置方向

语法如下

    subgraph title
      graph definition
    end

```
flowchart LR
  subgraph TOP
    direction TB
    subgraph B1
      direction RL
      i1 -->f1
    end
    subgraph B2
      direction BT
      i2 -->f2
    end
  end
  A --> TOP --> B
  B1 --> B2
```

.rmd结尾可以生效
  
