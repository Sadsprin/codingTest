# STRING

> string data type
* 문자열 변수를 초기화할 때는 큰따옴표(")나 작은 따옴표(')를 이용합니다.
* 문자열 안에 큰따옴표나 작은따옴표가 포함되어야 하는 경우가 있습니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 👉 전체 문자열을 큰따옴표로 구성하는 경우, 내부적으로 작은따옴표를 포함할 수 있습니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 👉 전체 문자열을 작은따옴표로 구성하는 경우, 내부적으로 큰따옴표를 포함할 수 있습니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 👉 혹은 백슬래시(\)를 사용하면, 큰따옴표나 작은따옴표를 원하는 만큼 포함시킬 수 있습니다.<br>

```python
data = 'hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

# 실행 결과
# hello World
# Don't you know "Python"?

a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a*3)

a = "ABCDEF"
print(a[2:4])

# 실행 결과
# Hello World
# StringStringString
# CD
a = 'hello'
a[1] = 'a'
# Error
# 값을 바꾸는 것은 불가능
```

> Tuple data type
* 튜플 자료형은 리스트와 유사하지만 다음과 같은 문법적 차이가 있습니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 👉 튜플은 한 번 선언된 값을 변경할 수 없습니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 👉 리스트는 대괄호([])를 이용하지만, 튜플은 소괄호(())를 이용합니다.<br>
* 튜플은 리스트에 비해 상대적으로 공간 효율적입니다.

```python
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# 네 번째 원소만 출력
print(a[3])

# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])

# 실행 결과
# 4
# (2, 3, 4)

a = (1, 2, 3, 4)
a[0] = 6
# Error 선언된 값을 변경할 수 없습니다.
```
> Tuple Profit
* 서로 다른 성질의 데이터를 묶어서 관리해야 할 때<br>
&nbsp;&nbsp;&nbsp;&nbsp; 👉 최단 경로 알고리즘에서는 (비용, 노드 번호)의 형태로 튜플 자료형을 자주 사용합니다.<br>
* 데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때<br>
&nbsp;&nbsp;&nbsp;&nbsp; 👉 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있습니다.<br>
* 리스트보다 메모리를 효율적으로 사용해야 할 때



> dictionary data type
* 사전 자료형은 <strong>키(key)와 값(value)</strong>의 쌍을 데이터로 가지는 자료형입니다.
&nbsp;&nbsp;&nbsp;&nbsp; 👉 앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비됩니다.
* 사전 자료형은 키와 값을 쌍을 데이터로 가지며, 원하는 '변경 불가능한(Immutable) 자료형'을 키로 사용 할 수 있습니다.
* 파이썬의 사전 자료형은 해시 테이블(Hash table)을이용하므로 데이터의 조회 및 수정에 있어서 
