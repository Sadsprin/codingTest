# List

> List Data Type

* 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형입니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 🧷 사용자 입장에서 C나 자바에서의 배열(Array)의 기능 및 연결 리스트와 유사한 기능을 지원합니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 🎈 C++의 STL vector와 기능적으로 유사합니다<br>
&nbsp;&nbsp;&nbsp;&nbsp; 💻 리스트 대신에 벼열 혹은 테이블이라 부르기도 합니다.<br>

<img src="../../img/list.jpg">

> List initialize

* 리스트는 대괄호([])안에 원소를 넣어 초기화하며, 쉼표(,)로 원소를 구분합니다.
* 비어 있는 리스트를 선언하고자 할 때는 list() 혹은 간단히 []를 이용할 수 있습니다.
* 리스트의 원소에 접근할 때는 인덱스(Index) 값을 괄호에 넣습니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 🧷 인덱스는 0부터 시작합니다.

```python
# 직접 데이터를 넣어 초기화
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 네 번째 원소만 출력
print(a[3])

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 실행결과
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 4
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```
> list index and slicing

* 인덱스 값을 입력하여 리스트의 특정한 원소에 접근하는 것을 인덱싱(Indexing)이라고 합니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 🧷 파이썬의 인덱스 값은 양의 정수와 음의 정수를 모두 사용할 수 있습니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 🎈 음의 정수를 넣으면 원소를 거꾸로 탐색하게 됩니다.<br>

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#여덟 번째 원소만 출력
print(a[7])

#뒤에서 첫 번째 원소 출력
print(a[-1])

#뒤에서 세 번째 원소 출력
print(a[-3])

#네 번재 원소 값 변경
a[3] = 7
print(a)

# 실행결과
# 8
# 9
# 7
# [1, 2, 3, 7, 5, 6, 7, 8, 9]
```

* 리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때는 <strong>슬라이싱(Slicing)</strong>을 이용합니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 🧷 대괄호 안에 콜론(:)을 넣어서 시작 인덱스와 끝 인덱스를 설정할 수 있습니다. <br>
&nbsp;&nbsp;&nbsp;&nbsp; 🎈 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정합니다.<br>

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 네 번째 원소만 출력
print(a[3])

# 두 번째 원소부터 네 번째 원소까지
print(a[1 : 4])

# 실행 결과
# 4
# [2, 3, 4]
```

> List Comprehension

* 리스트를 초기화하는 방법 중 하나 입니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 🧷 대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화 할 수 있습니다.

```python
# 0부터 9까지 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)

# 실행 결과
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i**2 for i in range(1, 10)]
print(array)

# 실행 결과
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

* 리스트 컴프리헨션은 <strong> 2차원 리스트를 초기화할 때 효과적으로 사용</strong>될 수 있습니다.
* 특히 N X M 크기의 2차원 리스트를 한 번에 초기화 해야 할 때 매우 유용합니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 🧷 array = [[0] * m for _ in range(n)]
* 만약 2차원 리스트를 초기화할 때 다음과 같이 작성하면 예기치 않은 결과가 나올 수 있습니다.
&nbsp;&nbsp;&nbsp;&nbsp; 🧷 <br>
&nbsp;&nbsp;&nbsp;&nbsp; 🎈
