# import re
#
# les = re.finditer(r"\d+","我的电话是10086,别人10101")
# for i in les:
#     print(i.group())
# import re
#
# it = re.findall(r"\d+", "12a32bc43jf3")
# print(it)
import re

h = """
<div class='tjs'>span id='1'>彭于晏</span>身高180</div>
<div class='cs'>span id='2'>镰刀</span>身高190</div>
<div class='go'>span id='3'>速度</span>身高178</div>
<div class='lj'>span id='4'>周星驰</span>身高170</div>
"""
obj = re.compile(r"<div class='lj'>span .*?</div>")
print(re.findall(obj,h))
