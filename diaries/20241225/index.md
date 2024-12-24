# 2024/12/25-學習 Markdown 語法


## 1. Markdown 是甚麼

Markdown 是一種輕量級標記語言，它允許你使用易讀易寫的純文字格式來撰寫文件，然後轉換成 HTML 或其他格式。

在 GitHub 上，Markdown 是主要的文件格式，用於撰寫 README.md， 會顯示在 GitHub 的專案首頁，可以用於描述專案的開發背景、功能、使用方法、貢獻者等。

## 2. Markdown 優點

- 易讀易寫：Markdown 使用純文字格式，易於閱讀和撰寫。
- 易於學習：Markdown 的語法簡單，易於學習。
- 易於轉換：Markdown 可以轉換成 HTML、PDF 等格式。

## 3. Markdown 缺點

- 不支援圖片：Markdown 不支援圖片，需要使用 HTML 來插入圖片。
- 不支援表格：Markdown 不支援表格，需要使用 HTML 來插入表格。
- 不支援數學公式：Markdown 不支援數學公式，需要使用 HTML 來插入數學公式。
- 不支援流程圖：Markdown 不支援流程圖，需要使用 HTML 來插入流程圖。

## 4. 怎麼開始寫 Markdown

- VSCode 安裝 Markdown 插件，推薦使用 [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) 插件。

- 啟動 VSCode 後，有兩個方法可以開啟 Markdown 預覽
    - 按 `Ctrl + Shift + P` 開啟命令面板，輸入 `Markdown: Open Preview` 開啟 Markdown 預覽。
    - 按 `Ctrl + Shift + V` 開啟 Markdown 預覽。

## 5. Markdown 語法

<details>
<summary>標題</summary>
Markdown 使用 `#` 來表示標題，`#` 越多表示標題層級越高，`#` 後面要空一格，類似 Word 的標題，會自動調整字體大小，最多可以到 6 級。

```markdown
# 標題 1
## 標題 2
### 標題 3
#### 標題 4
##### 標題 5
###### 標題 6
####### 標題 7
```

效果如下：

![標題](./標題.png)
</details>


<details>
<summary>文字樣式</summary>

```markdown
粗體：**粗體**
斜體：*斜體*
粗斜體：***粗斜體***
刪除線：~~刪除線~~
```

效果如下：

粗體：**粗體**

斜體：*斜體*

粗斜體：***粗斜體***

刪除線：~~刪除線~~
</details>

<details>
<summary>清單</summary>

- 無序清單：使用 `-` 或 `*` 來表示無序清單，`-` 或 `*` 後面要空一格。
- 有序清單：使用 `1.` 或 `1)` 來表示有序清單，`1.` 或 `1)` 後面要空一格。
  
```markdown
- 無序清單 1
- 無序清單 2
1. 有序清單 1
2. 有序清單 2
```

效果如下：

- 無序清單 1
- 無序清單 2
1. 有序清單 1
2. 有序清單 2
</details>

<details>
<summary>連結</summary>

Markdown 使用 `[連結文字](連結網址)` 來表示連結，連結文字會變成藍色，點擊後會跳轉到連結網址。

```markdown
[Google](https://www.google.com)
```

效果如下：

[Google](https://www.google.com)
</details>

<details>
<summary>圖片</summary>

Markdown 使用 `![圖片描述](圖片網址)` 來表示圖片，圖片描述會顯示在圖片下方，圖片網址會顯示在圖片上方。

```markdown
![Google](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)
```

效果如下：

![Google](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)
</details>

<details>
<summary>表格</summary>

Markdown 使用 `|` 來表示表格，`|` 後面要空一格。

```markdown
| 標題 1 | 標題 2 | 標題 3 |
| --- | --- | --- |
| 內容 1 | 內容 2 | 內容 3 |
```

效果如下：

| 標題 1 | 標題 2 | 標題 3 |
| --- | --- | --- |
| 內容 1 | 內容 2 | 內容 3 |
</details>

<details>
<summary>引用</summary>

Markdown 使用 `>` 來表示引用，`>` 後面要空一格。

```markdown
> 引用文字
>> 第二層引用
>>> 第三層引用
>
>> 使用>切開引用
>>> 第三層引用

>使用空格切開引用
```

效果如下：
> 引用文字
>> 第二層引用
>>> 第三層引用
>
>> 使用>切開引用
>>> 第三層引用

>使用空格切開引用
</details>

<details>
<summary>程式碼</summary>

- 單行程式碼：使用 \`\`\` 來表示單行程式碼，\`\`\` 後面要空一格。
- 多行程式碼：使用 \`\`\` 來表示多行程式碼，\`\`\` 加上語言名稱，後面要空一格。

```markdown
\`\`\`python
print("Hello, World!")
\`\`\`
```

效果如下：

```python
print("Hello, World!")
```

</details>

<details>
<summary>分隔線</summary>

Markdown 使用 `---` 來表示分隔線，`---` 後面要空一格。

```markdown
---
```

效果如下：

---
</details>

<details>
<summary>任務列表</summary>

Markdown 使用 `- [ ]` 來表示任務列表，`- [ ]` 後面要空一格。

```markdown
- [ ] 任務 1
- [x] 任務 2
```

效果如下：

- [ ] 任務 1
- [x] 任務 2
</details>

<details>
<summary>內嵌 HTML</summary>

Markdown 使用 `<html>` 來表示內嵌 HTML，`<html>` 後面要空一格。

```markdown
<html>
<body>
This is a regular paragraph.

<table>
    <thead>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Cell 1</td>
            <td>Cell 2</td>
        </tr>
    </tbody>
</table>

This is another regular paragraph.
</body>
</html>
```

效果如下：

<html>
<body>
This is a regular paragraph.

<table>
    <thead>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Cell 1</td>
            <td>Cell 2</td>
        </tr>
    </tbody>
</table>

This is another regular paragraph.
</body>
</html>
</details>
