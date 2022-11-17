import re

address = "北縣淡水鎮妖怪村西米路"

# 處理"台"
address = address.replace("臺","台")

# 處理特別案例
address = address.replace('苗栗縣頭份鎮', '苗栗縣頭份市').replace('彰化縣員林鎮', '彰化縣員林市').replace('南海諸島東沙', '南海島東沙群島').replace('南海諸島南沙', '南海島南沙群島').replace('南海諸島釣魚台列嶼', '釣魚台釣魚台').replace('[石曹]村', '[石曹]里').replace('頭家東村', '頭家東里').replace('拉芙蘭村', '拉芙蘭里').replace('那瑪夏鄉', '那瑪夏區').replace('達卡努瓦村', '達卡努瓦里').replace('瑪雅村', '瑪雅里').replace('南沙魯村', '南沙魯里')

# 處理縮寫
address = re.sub(r'^北縣', '台北縣', address)
address = re.sub(r'^北市', "台北市", address)

# 處理六都
def convert_district(match): 
    return ('新北' if match.group(1) == '台北' else match.group(1)) + '市' + ((match.group(2) + '區') if match.group(2) is not None else '') + ((match.group(3) + '里') if match.group(3) is not None else '')

address = re.sub(r'^(台北|桃園|台中|台南|高雄)縣(?:(\w{2})[市鄉鎮])?(?:(\w{2})村)?', convert_district, address)
address = address.replace('台南市中區', '台南市中西區').replace('台南市西區', '台南市中西區')

print(address)
