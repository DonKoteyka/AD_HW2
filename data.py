patter_name = r'^(\w+)[\s|,]{1}(\w+)[\s|,]{1}(\w+)?'
replase_name = r'\1, \2, \3'

patter_phone = r'((\+7|8)\s?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2}))\s?(\(?(\w{3}\.)\s(\d{4})\)?)?'
replase_phone = r'+7(\3)\4-\5-\5 \8\9'

