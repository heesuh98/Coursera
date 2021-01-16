##염기서열 안에 AAA개수 세기

import re
s = "GACCATCAAAACTGATAAACTACTTAAAAATCAGT"
matches = re.finditer(r'(?=(AAA))', s)
results = [(match.group(1)) for match in matches]
print(len(results))