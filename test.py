try:
    import cryptography
    print("cryptography 包安装成功！")
except ImportError:
    print("cryptography 包未安装，请检查。")