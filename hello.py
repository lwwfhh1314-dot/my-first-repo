
---

## 📄 hello.py
```python
# hello.py
# 这是我的第一个 Python 文件
# 用来测试 GitHub 上的代码提交与运行

def greet(name: str) -> str:
    """返回一个问候语"""
    return f"Hello, {name}! 欢迎来到我的 GitHub 仓库 🎉"

def count_to_n(n: int):
    """从 1 数到 n"""
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

def add(a: int, b: int) -> int:
    """返回两个数的和"""
    return a + b

if __name__ == "__main__":
    print("=== Python GitHub 示例程序 ===")
    print("-" * 30)

    # 调用问候函数
    print(greet("GitHub"))

    # 调用计数函数
    print("数到 5:")
    count_to_n(5)

    # 调用加法函数
    print("2 + 3 =", add(2, 3))
