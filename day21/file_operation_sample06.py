try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("文件不存在!")
except PermissionError:
    print("没有文件访问权限!")
except IOError as e:
    print(f"IO错误: {e}")