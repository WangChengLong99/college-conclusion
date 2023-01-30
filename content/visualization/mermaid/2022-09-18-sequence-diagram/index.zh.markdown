---
title: 序列图(sequence diagram)
author: admin
date: '2022-09-18'
slug: sequence-diagram
categories: []
tags: []
subtitle: ''
summary: '介绍序列图的使用和语法'
authors: []
lastmod: '2022-09-18T10:13:29+08:00'
featured: no
image:
  caption: ''
  focal_point: ''
  preview_only: no
projects: []
weight: 30
type: book
---

## 介绍

序列图是一个交互图，显示了流程之间如何操作以及以何种顺序操作。重点在于如何操作流程图重在流程，序列图重在流程之间的交互。
基本形式如下：

```
sequenceDiagram
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!
    Alice-)John: See you later! -）实现有问题，实际删除了这行
```

```mermaid
sequenceDiagram
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!
```

{{%callout warning%}}单词“end”可能会破坏图。如果不可避免，必须使用圆括号()，引号""，或括号{}，[]来围住单词"end"。即:(end)， [end]， {end}。{{%/callout%}}

## 创建用户对象

* participant：默认一个用户是一个participant
  * 默认的用户就是一个participant
  * 显式声明 `participant Alice`
  * 给人名一个id `participant A as Alice`,之后可以用A来代替
* actor：更加形象的表示

```
sequenceDiagram
  participant A as Alice
  participant Bob
  A -> Bob: 从一个id到另一个id，A显示为Alice
  Bob -> C: C未声明，但是，默认是participant
```

```mermaid
sequenceDiagram
  participant A as Alice
  participant Bob
  A -> Bob: 从一个id到另一个id，A显示为Alice
  Bob -> C: C未声明，但是，默认是participant
```

## 实现用户之间的交互Messages

`[Actor][Arrow][Actor]:Message text` 定义两个用户之间的交互

<table>
<thead>
<tr>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr>
<td>-&gt;</td>
<td>Solid line without arrow</td>
</tr>
<tr>
<td>--&gt;</td>
<td>Dotted line without arrow</td>
</tr>
<tr>
<td>-&gt;&gt;</td>
<td>Solid line with arrowhead</td>
</tr>
<tr>
<td>--&gt;&gt;</td>
<td>Dotted line with arrowhead</td>
</tr>
<tr>
<td>-x</td>
<td>Solid line with a cross at the end</td>
</tr>
<tr>
<td>--x</td>
<td>Dotted line with a cross at the end.</td>
</tr>
<tr>
<td>-)</td>
<td>Solid line with an open arrow at the end (async)</td>
</tr>
<tr>
<td>--)</td>
<td>Dotted line with a open arrow at the end (async)</td>
</tr>
</tbody></table>

可以声明autonumber参数，为交互添加编号顺序

```
sequenceDiagram
    autonumber
    Alice->>John: Hello John, how are you?
        loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
```

```mermaid
sequenceDiagram
    autonumber
    Alice->>John: Hello John, how are you?
        loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
```

## 激活禁止用户,activation

activate/deactivate 可以激活或禁止一个用户

```
sequenceDiagram
    Alice->>John: Hello John, how are you?
    activate John
    John-->>Alice: Great!
    deactivate John
```

```mermaid
sequenceDiagram
    Alice->>John: Hello John, how are you?
    activate John
    John-->>Alice: Great!
    deactivate John
```

加上后缀+/-可以激活或者禁止

```
sequenceDiagram
  Alice->>+John: hello john,how are you?
  John->>-Alice: Great!
```
  
```mermaid
sequenceDiagram
  Alice->>+John: hello john,how are you?
  John->>-Alice: Great!
```

激活可以为相同的参与者堆叠:

```
sequenceDiagram
    Alice->>+John: Hello John, how are you?
    Alice->>+John: John, can you hear me?
    John-->>-Alice: Hi Alice, I can hear you!
    John-->>-Alice: I feel great!
```

```mermaid
sequenceDiagram
    Alice->>+John: Hello John, how are you?
    Alice->>+John: John, can you hear me?
    John-->>-Alice: Hi Alice, I can hear you!
    John-->>-Alice: I feel great!
```

## 添加循环结构

```
loop text
...statement...
end
```

```
sequenceDiagram
    Alice->John: Hello John, how are you?
    loop Every minute
        John-->Alice: Great!
    end
```
```mermaid
sequenceDiagram
    Alice->John: Hello John, how are you?
    loop Every minute
        John-->Alice: Great!
    end
```

## 可选路径，条件判断Alt/opts

```
alt Describing text
... statements ...
else discribing text
... statements ...
else
... statements ...
.
.
.
end
```

```
opt Describing text
... statements ...
end
```

Alt可以有else，是一个判断结构，opts表示可选项，可以有也可以没有。

```
sequenceDiagram
    Alice->>Bob: Hello Bob, how are you?
    alt is sick
        Bob->>Alice: Not so good :(
    else is well
        Bob->>Alice: Feeling fresh like a daisy
    end
    opt Extra response
        Bob->>Alice: Thanks for asking
    end
```

```mermaid
sequenceDiagram
    Alice->>Bob: Hello Bob, how are you?
    alt is sick
        Bob->>Alice: Not so good :(
    else is well
        Bob->>Alice: Feeling fresh like a daisy
    end
    opt Extra response
        Bob->>Alice: Thanks for asking
    end
```

## 串行逻辑，parallel

表示几个操作时同时进行的，并行

```
par [Action 1]
... statements ...
and [Action 2]
... statements ...
and [Action N]
... statements ...
end
```

嵌套

```
sequenceDiagram
    par Alice to Bob
        Alice->>Bob: Go help John
    and Alice to John
        Alice->>John: I want this done today
        par John to Charlie
            John->>Charlie: Can we do this today?
        and John to Diana
            John->>Diana: Can you help us today?
        end
    end
```

```mermaid
sequenceDiagram
    par Alice to Bob
        Alice->>Bob: Go help John
    and Alice to John
        Alice->>John: I want this done today
        par John to Charlie
            John->>Charlie: Can we do this today?
        and John to Diana
            John->>Diana: Can you help us today?
        end
    end
```

## 条件满足必须自动执行

critical region,所有满足条件的必须自动执行

可以有也可以没有option，也可以和par一样嵌套

```
critical [Action that must be performed]
... statements ...
option [Circumstance A]
... statements ...
option [Circumstance B]
... statements ...
end
```

```
sequenceDiagram
    critical "Establish a connection to the DB"
        Service-->DB: connect
    option "Network timeout"
        Service-->Service: "Log error"
    option "Credentials rejected"
        Service-->Service: "Log different error"
    end
```

```mermaid
sequenceDiagram
  critical Establish a connection to the DB
    Service-->DB: connect
```

## break 

可以在流中指示序列的停止(通常用于建模异常)。

```
break [something happened]
... statements ...
end
```

```
sequenceDiagram
    Consumer-->API: Book something
    API-->BookingService: Start booking process
    break when the booking process fails
        API-->Consumer: show failure
    end
    API-->BillingService: Start billing process
```

```mermaid
sequenceDiagram
    Consumer-->API: Book something
    API-->BookingService: Start booking process
    break when the booking process fails
        API-->Consumer: show failure
    end
    API-->BillingService: Start billing process
```

## 背景颜色

可以用rgb或rgba颜色

```
rect rgb(0, 255, 0)
... content ...
end
```

```
sequenceDiagram
    participant Alice
    participant John

    rect rgb(191, 223, 255)
    note right of Alice: Alice calls John.
    Alice->>+John: Hello John, how are you?
    rect rgb(200, 150, 255)
    Alice->>+John: John, can you hear me?
    John-->>-Alice: Hi Alice, I can hear you!
    end
    John-->>-Alice: I feel great!
    end
    Alice ->>+ John: Did you want to go to the game tonight?
    John -->>- Alice: Yeah! See you there.
```

```mermaid
sequenceDiagram
    participant Alice
    participant John

    rect rgb(191, 223, 255)
    note right of Alice: Alice calls John.
    Alice->>+John: Hello John, how are you?
    rect rgb(200, 150, 255)
    Alice->>+John: John, can you hear me?
    John-->>-Alice: Hi Alice, I can hear you!
    end
    John-->>-Alice: I feel great!
    end
    Alice ->>+ John: Did you want to go to the game tonight?
    John -->>- Alice: Yeah! See you there.
```

## 添加notes

位置可以是左边，右边或者两个actor之间

`Note [ right of | left of | over ] [Actor]: Text`

```
sequenceDiagram
    Alice->John: Hello John, how are you?
    Note over Alice,John: A typical interaction
```

```mermaid
sequenceDiagram
    Alice->John: Hello John, how are you?
    Note over Alice,John: A typical interaction
```

## 链接

`link <actor>: <link-label> @ <link-url>`

```
sequenceDiagram
    participant Alice
    participant John
    link Alice: Dashboard @ https://dashboard.contoso.com/alice
    link Alice: Wiki @ https://wiki.contoso.com/alice
    link John: Dashboard @ https://dashboard.contoso.com/john
    link John: Wiki @ https://wiki.contoso.com/john
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!
    Alice-->John: See you later!
```

```mermaid
sequenceDiagram
    participant Alice
    participant John
    link Alice https://dashboard.contoso.com/alice
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!
    Alice-->John: See you later!
```

## css风格

见[css风格](https://mermaid-js.github.io/mermaid/#/sequenceDiagram?id=styling)
