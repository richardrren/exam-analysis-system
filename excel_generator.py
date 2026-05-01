import pandas as pd
from datetime import datetime

def generate_excel(data, output_path):
    """根据数据生成Excel文件"""
    try:
        df = pd.DataFrame(data)
        
        columns_order = ["题号", "题型", "核心考点", "分值", "难度等级", "易错点"]
        df = df[columns_order]
        
        df.to_excel(output_path, index=False, engine="openpyxl")
        return True
    except Exception as e:
        print(f"Excel生成错误: {e}")
        return False
