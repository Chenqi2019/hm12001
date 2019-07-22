import yaml

# data={"name": "张三", "age": 25}
#
# with open("../data/write.yaml", "w", encoding="utf-8")as f:
#     yaml.dump(data, f, encoding="utf-8", allow_unicode=True)


sj = {"name":"李四","address":"北京市大兴区","email":"1234567@qq.com"}

with open("../data/write.yaml","w",encoding="utf-8")as f:
    yaml.dump(sj,f,allow_unicode=True)