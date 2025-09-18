import os
import sys
from pathlib import Path

def check_file_existence():
    """检查文件是否存在并提供诊断信息"""
    filename = "pi_digits.txt"
    script_dir = Path(__file__).parent.absolute()
    
    print("=== 文件诊断工具 ===")
    print(f"当前工作目录: {os.getcwd()}")
    print(f"脚本所在目录: {script_dir}")
    print()
    
    # 检查文件是否存在
    file_path = os.path.join(script_dir, filename)
    if os.path.exists(file_path):
        print(f"✅ 找到文件: {file_path}")
        print(f"文件大小: {os.path.getsize(file_path)} 字节")
        return True
    else:
        print(f"❌ 未找到文件: {file_path}")
        print()
        print("可能的原因:")
        print("1. 文件名不正确（检查大小写和扩展名）")
        print("2. 文件不在脚本所在目录")
        print("3. 文件被其他程序占用")
        return False

def read_file_with_checks():
    """尝试读取文件并提供详细的错误信息"""
    filename = "pi_digits.txt"
    script_dir = Path(__file__).parent.absolute()
    file_path = os.path.join(script_dir, filename)
    
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print("\n=== 文件内容 ===")
            print(contents)
            return True
    except FileNotFoundError:
        print(f"\n错误: 无法找到文件 '{filename}'")
        print("请检查:")
        print(f"1. 文件是否在目录: {script_dir}")
        print("2. 文件名是否正确（包括大小写和.txt扩展名）")
        print("3. 文件是否被其他程序打开")
    except PermissionError:
        print(f"\n错误: 没有权限读取文件 '{filename}'")
    except Exception as e:
        print(f"\n发生未知错误: {str(e)}")
    
    return False

def list_directory_contents():
    """列出脚本所在目录的所有文件和文件夹"""
    script_dir = Path(__file__).parent.absolute()
    print("\n=== 目录内容 ===")
    print(f"目录: {script_dir}")
    print("\n文件和文件夹列表:")
    
    try:
        items = os.listdir(script_dir)
        for item in items:
            item_path = os.path.join(script_dir, item)
            if os.path.isfile(item_path):
                print(f"📄 {item} (文件, {os.path.getsize(item_path)} 字节)")
            else:
                print(f"📁 {item} (文件夹)")
    except Exception as e:
        print(f"无法列出目录内容: {str(e)}")

if __name__ == "__main__":
    # 执行诊断
    list_directory_contents()
    print("\n" + "="*50)
    file_exists = check_file_existence()
    
    if file_exists:
        print("\n尝试读取文件...")
        read_file_with_checks()
    else:
        print("\n请将pi_digits.txt文件放置在正确目录后重新运行此程序。")
        print(f"正确目录: {Path(__file__).parent.absolute()}")
    
    # 等待用户按键退出（仅在直接运行时）
    if __name__ == "__main__":
        input("\n按Enter键退出...")