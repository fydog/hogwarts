import yaml


class Utils:
    @classmethod
    def from_file(cls , path):
        with open(path,'r',encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
            params = yaml_data['params']
            keys = set()
            values=[]
            if isinstance(params, list):
                # 如果参数是列表
                for row in params:
                    if isinstance(row , dict):
                        for key in row.keys():
                            keys.add(key)
                            # 重复数据去重
                            values.append(list(row.values())[0])
                            # 列表的第一个值
            var_name = ','.join(keys)
            return {'keys':var_name, 'values': values}



                
