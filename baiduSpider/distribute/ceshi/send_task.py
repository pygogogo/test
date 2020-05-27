from ceshi.task1 import add1
from ceshi.task2 import add2


res1 = add1.delay(3, 8)
print(res1)   # 16e847f3-fc14-4391-89e2-e2b3546872cf

res2 = add2.delay(4, 9)
print(res2)   # 858c0ae5-8516-4473-8be5-7501fb856ff4