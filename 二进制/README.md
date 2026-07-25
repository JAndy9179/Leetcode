### 命令面板

- 打开命令面板：`ctrl + shift + p`

- 搜索：`Select Interpreter`


### 代码仓库

#### 初始化

1. 初始化本地仓库: git init

2. 添加文件到暂存区: git add .

3. 提交更改: git commit -m "first commit"

> 首次提交之前需要先配置: 
> git config --global user.email "jandy9179@gmail.com"
> git config --global user.name "JAndy9179"

4. 重命名分支为 main: git branch -M main

5. 关联远程仓库: git remote add origin https://github.com/JAndy9179/Leetcode.git

6. 推送代码到 github: git push -u origin main

> 如果 push 之前又对文件进行了修改, 只需要再 add 一次, 然后再 commit 一次, 之后再 push