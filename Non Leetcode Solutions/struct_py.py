from typing import NamedTuple
class MyStruct(NamedTuple):
    name:str
    rno:int
    age:int
    marks:list

rohan=MyStruct('rohan',18,18,[88,98,76])
mishti=MyStruct('mishti',2,18,[84,98,73])
print(sum(rohan.marks)//len(rohan.marks))
