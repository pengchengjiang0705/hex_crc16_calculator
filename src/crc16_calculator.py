import sys

# 原始C代码中的查找表
CRC_TABLE = [
    0x0000, 0xCC01, 0xD801, 0x1400, 0xF001, 0x3C00, 0x2800, 0xE401,
    0xA001, 0x6C00, 0x7800, 0xB401, 0x5000, 0x9C01, 0x8801, 0x4400
]

def parse_hex_file(file_path):
    """解析十六进制格式的文本文件"""
    with open(file_path, 'r') as f:
        content = f.read().strip()
    
    # 处理空格分隔的十六进制字节
    hex_bytes = []
    for hex_str in content.split():
        # 确保每两个字符表示一个字节
        if len(hex_str) == 1:
            hex_bytes.append(int(hex_str, 16))
        elif len(hex_str) == 2:
            hex_bytes.append(int(hex_str, 16))
        else:
            # 处理可能的多字节值（但按单字节处理）
            for i in range(0, len(hex_str), 2):
                byte_str = hex_str[i:i+2].zfill(2)
                hex_bytes.append(int(byte_str, 16))
    
    return bytes(hex_bytes)

def crc16(data):
    """
    计算CRC16校验值（严格遵循C代码逻辑）
    :param data: 字节数组或bytes对象
    :return: 最终CRC值（16位整数）
    """
    crc = 0xFFFF  # 初始化CRC
    print(f"{'Index':<6} {'Byte(Hex)':<10} {'Intermediate CRC(Hex)':<20}")
    print("-" * 40)
    
    for i, byte in enumerate(data):
        # 处理低4位
        low_nibble = byte & 0x0F
        idx = low_nibble ^ (crc & 0x0F)
        crc = (crc >> 4) ^ CRC_TABLE[idx & 0x0F]
        
        # 处理高4位
        high_nibble = (byte >> 4) & 0x0F
        idx = high_nibble ^ (crc & 0x0F)
        crc = (crc >> 4) ^ CRC_TABLE[idx & 0x0F]
        
        # 打印当前字节处理结果
        print(f"{i:<6} {byte:02X}         {crc:04X}")
    
    # 字节交换（低位转高位）
    return ((crc << 8) | (crc >> 8)) & 0xFFFF

def process_file(file_path):
    """
    处理文件并计算CRC
    :param file_path: 文本文件路径
    """
    try:
        file_data = parse_hex_file(file_path)
        
        print(f"\nFile: {file_path}")
        print(f"Size: {len(file_data)} bytes\n")
        
        final_crc = crc16(file_data)
        print("\n" + "=" * 40)
        print(f"Final CRC16: 0x{final_crc:04X}")
        print("=" * 40)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python crc16_calculator.py <input_file.txt>")
        print("File format: Space-separated hex bytes (e.g., '01 A2 FF')")
    else:
        process_file(sys.argv[1])