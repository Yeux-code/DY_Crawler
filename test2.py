import base64

# Base64 编码字符串
encoded_str = "MS4wLjABAAAAp-PbxQo21FoPDXDgHG1LqiOXVZW1h-K8AcODlMovl6K6DKoNUARSqBJLOkD4Or2Q"
try:
    decoded_bytes = base64.b64decode(encoded_str)
    decoded_str = decoded_bytes.decode('utf-8', errors='ignore')  # 假设文本是 UTF-8 编码
    print("Base64 解码明文:", decoded_str)
except Exception as e:
    print("Base64 解码失败:", e)

# 十六进制编码字符串
hex_str = "0a2cdfc355aca65487c19cd6db22ac6ebba6af225d6203d6bfa5526e561769383aca46d0a69d8bb222ecd004d4bb1a4b0a3c8c73fb3ddeb21c514cf00621c4dfc0962cd1ee0218ab30bac3bcf7f0f2f5363267d9d06697a23fa2e6374b29603ab29728f0095e2581b33f56d71c0b10e7a2e90d18e5ade4c9012001220103311c8dca"
try:
    decoded_bytes = bytes.fromhex(hex_str)
    decoded_str = decoded_bytes.decode('utf-8', errors='ignore')  # 假设文本是 UTF-8 编码
    print("Hex 解码明文:", decoded_str)
except Exception as e:
    print("Hex 解码失败:", e)
