
# lecture_1 basic algorithm

> 복잡도 (Complexity)

* 시간 복잡도 : 특정한 크기의 입력에 대하여 알고리즘의 수행 시간 분석
* 공간 복잡도 : 특정한 크기의 입력에 대하여 알고리즘의 메모리 사용량 분석

> 빅오 표기법 ( Big-O Notation ) <br>

* 가장 빠르게 증가하는 항만을 고려하는 표기법입니다.

<img src="./img/bigo.jpg" width="300" height="300"/>

> 알고리즘 설계 Tip
 
 * 일반적으로 CPU 기반의 개인 컴퓨터나 채점용 컴퓨터에서 연산 횟수가 5억을 넘어가는 경우<br>
 &nbsp;&nbsp; C언어 => 1 ~ 3초 가량의 시간이 소요<br>
 &nbsp;&nbsp; Python => 5 ~ 15초 가량의 시간이<br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; % pypy의 경우 때때로 C언어보다도 빠르게 동작하기도 합니다.<br>

* <img src="https://render.githubusercontent.com/render/math?math=O(N^3)">의 알고리즘을 설계한 경우, N의 값이 5000이 넘는다면 얼마나 걸릴까?
* 코딩 테스트 문제에서 시간제한은 통상 1~5초 가량이라는 점에 유의하세요<br>
&nbsp;&nbsp; 혹여 문제에 명시되어 있지 않은 경우 대략 5초 정도라고 생각하고 문제를 푸는 것이 합리적입니다.

> 문제에서 가장 먼저 확인해야 하는 내용은 시간제한(수행시간 요구사항)입니다.<br>


&nbsp;&nbsp; 시간제한이 1초인 문제를 만났을 때, 일반적인 기준은 다음과 같습니다. --> 2천만개 수행가능<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; N = 500  => 시간 복잡도가 <img src="https://render.githubusercontent.com/render/math?math=O(N^3)">인 알고리즘을 설계하면 문제를 풀 수 있습니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; N = 2000  => 시간 복잡도가 <img src="https://render.githubusercontent.com/render/math?math=O(N^2)">인 알고리즘을 설계하면 문제를 풀 수 있습니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; N = 100000  => 시간 복잡도가 <img src="https://render.githubusercontent.com/render/math?math=O(NlogN)">인 알고리즘을 설계하면 문제를 풀 수 있습니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; N = 10000000  => 시간 복잡도가 <img src="https://render.githubusercontent.com/render/math?math=O(N)">인 알고리즘을 설계하면 문제를 풀 수 있습니다.<br>

> 알고리즘 문제 해결 과정

* 일반적인 알고리즘 문제 해결 과정은 다음과 같습니다.<br>
&nbsp;&nbsp;&nbsp;&nbsp; 1. 지문 읽기 및 컴퓨터적 사고<br>
&nbsp;&nbsp;&nbsp;&nbsp; 2. 요구사항(복잡도) 분석<br>
&nbsp;&nbsp;&nbsp;&nbsp; 3. 문제 해결을 위한 아이디어 찾기<br>
&nbsp;&nbsp;&nbsp;&nbsp; 4. 소스코드 설계 및 코딩<br>

* 수행 시간 측정 소스코드 예제
``` python
import time
start_time = time.time()
end_time = time.time()
print("time:", end_time - start_time)
```

