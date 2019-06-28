# Python3 XML 解析
---
## 什么是 XML？
XML 指可扩展标记语言（eXtensible Markup Language），标准通用标记语言的子集，是一种用于标记电子文件使其具有结构性的标记语言。
你可以通过本站学习 XML 教程

XML 被设计用来传输和存储数据。
XML 是一套定义语义标记的规则，这些标记将文档分成许多部件并对这些部件加以标识。
它也是元标记语言，即定义了用于定义其他与特定领域有关的、语义的、结构化的标记语言的句法语言。
---
## Python 对 XML 的解析
常见的 XML 编程接口有 DOM 和 SAX，这两种接口处理 XML 文件的方式不同，当然使用场合也不同。
Python 有三种方法解析 XML，SAX，DOM，以及 ElementTree:
Python 标准库包含 SAX 解析器，SAX 用事件驱动模型，通过在解析 XML 的过程中触发一个个的事件并调用用户定义的回调函数来处理 XML 文件。
将 XML 数据在内存中解析成一个树，通过对树的操作来操作 XML。
本章节使用到的 XML 实例文件 movies.xml 内容如下：
```

<collection shelf="New Arrivals">
<movie title="Enemy Behind">
   <type>War, Thriller</type>
   <format>DVD</format>
   <year>2003</year>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Talk about a US-Japan war</description>
</movie>
<movie title="Transformers">
   <type>Anime, Science Fiction</type>
   <format>DVD</format>
   <year>1989</year>
   <rating>R</rating>
   <stars>8</stars>
   <description>A schientific fiction</description>
</movie>
   <movie title="Trigun">
   <type>Anime, Action</type>
   <format>DVD</format>
   <episodes>4</episodes>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Vash the Stampede!</description>
</movie>
<movie title="Ishtar">
   <type>Comedy</type>
   <format>VHS</format>
   <rating>PG</rating>
   <stars>2</stars>
   <description>Viewable boredom</description>
</movie>
</collection>

```
---
## Python 使用 SAX 解析 xml
SAX 是一种基于事件驱动的API。
利用 SAX 解析 XML 文档牵涉到两个部分: 解析器和事件处理器。
解析器负责读取 XML 文档，并向事件处理器发送事件，如元素开始跟元素结束事件。
而事件处理器则负责对事件作出响应，对传递的 XML 数据进行处理。

