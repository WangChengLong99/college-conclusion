---
# 文章的题目
title: Example Talk
# 作者
authors: [admin]
# 地址
location: 安徽省
# 所属tag
tags: []
# 文章的预览显示
summary: An example talk using Wowchemy's Markdown slides feature.
# event可以用来记录自己参加的会议，等。
abstract: 这是一个event的示例，会在/talk/下来访问，文章的内容显示
# 事件的名称和链接
event: Wowchemy Conference
event_url: https://example.org
# 事件发生的地址
address:
  city: 合肥
  country: 中国
  # postcode: "94305"
  # region: CA
  street: 肥东县陶冲湖
# 开始日期和结束日期
date: "2030-06-01T13:00:00Z"
date_end: "2030-06-01T15:00:00Z"

# 将会显示在image上的内容
image:
# Featured image
# To use, place an image named `featured.jpg/png` in your page's folder.
# Placement options: 1 = Full column width, 2 = Out-set, 3 = Screen-width
# Focal point options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
# Set `preview_only` to `true` to just use the image for thumbnails.（缩略图，仅在预览界面可以看到，文章中看不到
  placement: 1
  #关于photo的介绍
  caption: "Photo by [Geo](https://github.com/gcushen/)"
  focal_point: "Center"
  preview_only: false
  alt_text: An optional description of the image for screen readers.

# 并没有显示
publishDate: "2017-01-01T00:00:00Z"
all_day: false
featured: false

# button
# 用于显示在顶端的page-resources,会创建button
links:
- icon: twitter
  icon_pack: fab
  name: Follow
  url: https://twitter.com/georgecushen
# url链接,可以以button形式显示网上相关的code，pdf，slides，和video
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""
# 相关的slides下的文件夹
slides: example
# 跟event相关的project，即设置project下的相关文件夹
projects:
- example
---

{{% callout note %}}
Click on the **Slides** button above to view the built-in slides feature.
{{% /callout %}}

Slides can be added in a few ways:

- **Create** slides using Wowchemy's [_Slides_](https://wowchemy.com/docs/managing-content/#create-slides) feature and link using `slides` parameter in the front matter of the talk file
- **Upload** an existing slide deck to `static/` and link using `url_slides` parameter in the front matter of the talk file
- **Embed** your slides (e.g. Google Slides) or presentation video on this page using [shortcodes](https://wowchemy.com/docs/writing-markdown-latex/).

Further event details, including [page elements](https://wowchemy.com/docs/writing-markdown-latex/) such as image galleries, can be added to the body of this page.
