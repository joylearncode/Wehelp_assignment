# 第一題

from itertools import product


def calculate(min,max,step):
    result=0
    for num in range(min,max+1,step):
      result = result+num  # result+=num
    print(result)

calculate(1,3,1) #你的程式要能夠計算 1+2+3，最後印出 6
calculate(4,8,2) #最後印出18
calculate(-1,2,2) #最後印出0


#要求二：Python 字典與列表、JavaScript 物件與陣列

def avg(data):
  result=[]
  for employee in data["employees"]:
    if employee["manager"]== False:
      result.append(employee["salary"])
    
  print("average=", sum(result)/len(result))
  

avg({
    "employees": [
                    {"name": "John","salary": 30000,"manager":False},
                    {"name": "Bob","salary": 60000,"manager":True},
                    {"name": "Jenny", "salary": 50000,"manager": False},
                    {"name": "Tony","salary": 40000,"manager":False}

                  ]
    })

#呼叫avg函式


# 要求三：
def func(a):
  def product(b,c):
    print(a+b*c)

  return product
  
func(2)(3,4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1,-5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2,9) # 你補完的函式能印出 -3+(2*9) 的結果 15


# 要求四
# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
# 提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。

def maxProduct(nums):
  result = None
  for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
      product=nums[i]*nums[j]     
      if result == None or product > result:
        result = product
  print(result)

maxProduct([5,20,2,6]) # 得到 120
maxProduct([10,-20,0,3])  # 得到 30
maxProduct([10,-20,0,-3]) # 得到60
maxProduct([-1,2]) # 得到-2
maxProduct([-1,0,2]) # 得到0
maxProduct([5,-1,-2,0]) # 得到2
maxProduct([-5,-2]) # 得到10


# 要求五
# Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.

def twoSum(nums,target):

  for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
      if nums[i]+nums[j]==target:
        return[i,j]

result=twoSum([2,11,7,15],9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9