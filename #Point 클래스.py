#Point 클래스
class Point:
  def __init__(self, x = 0, y= 0):
    self.x = x
    self.y = y

  def __str__(self):      #출력용 문자열을 리턴 /정수도 문자열로 출력함 __str__
    return f"({self.x},{self.y})"

p = Point(1,2)

print(p)   #"(1,2)""

s= str(p) # "1,2" 문자열로 만듦
print(s)

# 연산자 오버로딩
