import yaml

# 打开并解析 offsets.yaml 文件
with open("offsets.yaml", "r", encoding="utf-8") as file:
    offsets = yaml.safe_load(file)

# 从配置中提取 Deathmatch 模式的字段和偏移值
deathmatch_data = offsets['client_dll']['classes']['CCSGameModeRules_Deathmatch']
fields = deathmatch_data.get('fields', {})

print("🎯 Deathmatch 模式字段偏移：")
for name, offset in fields.items():
    print(f"{name} -> 偏移值: {offset}")