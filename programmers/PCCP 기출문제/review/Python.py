# Python

# 숫자
# 버전 2.4부터 int 단일형으로 통합되었다
# bool은 논리 자료형이지만 파이썬에서 내부적으로 1(True)과 0(False)으로 처리되는 int의 서브 클래스다
# int는 object의 하위 클래스이므로 결국 다음과 같은 구조를 띤다
# object > int > bool

print(True == 1) # True
print(False == 0) # True

# 매핑
# 파이썬에 내장된 유일한 매핑 자료형은 딕셔너리다

# 집합
# 파이썬의 집합 자료형인 set은 중복된 값을 갖지 않는 자료형이다
# 빈 집합은 다음과 같은 형태로 선언한다
a = set()
print(type(a)) # <class 'set'>
# 빈 집합이 아닌 값이 포함된 집합을 선언할 때는 중괄호를 사용하는데 딕셔너리와 동일하므로 이 점에 유의한다
a = {'a', 'b', 'c'}
print(type(a)) # <class 'set'>
a = {'A':'a', 'B':'b', 'C':'c'}
print(type(a)) # <class 'dict'>
# set은 입력 순서가 유지되지 않으며 중복된 값이 있을 경우 하나의 값만 유지한다

# 시퀀스
# 파이썬에서는 list라는 시퀀스 타입이 사실상 배열의 역할을 수행한다
# 시퀀스는 불변과 가변으로 구분하는데 불변에는 str, tuple, bytes가 해당된다

# 객체
# C나 자바는 성능에 대한 우선순위가 높은 언어다
# 때문에 좀 더 하드웨어에 가까운 원시 타입을 별도로 제공하며 원시 타입으로 구현했을 때 훨씬 더 빠른 속도로 실행할 수 있다
# 파이썬은 원시 타입을 지원하지 않는다
# 파이썬은 원시 타입의 속도를 포기하는 대신 객체의 다양한 기능과 편의성을 선택했다
# 파이썬은 모든 것이 객체이다
# 불변 객체: bool, int, float, tuple, str
# 가변 객체: list, set, dict

# 파이썬의 비교 연산자 중 is와 ==가 있다
# is는 id() 값을 비교하는 함수다
# None은 null로서 값 자체가 정의되어 있지 않으므로 ==로 비교가 불가능하다
# 따라서 다음과 같이 is로만 비교가 가능하다
if a is None:
    pass
# ==는 값을 비교하는 연산자다
a = [1, 2, 3]
print(a == a) # True
print(a == list(a)) # True
print(a is a) # True
print(a is list(a)) # False
# 값은 동일하지만 list()로 한 번 더 묶어주면 별도의 객체로 복사가 되고 다른 ID를 갖게 된다
# 따라서 is는 False가 된다
# copy.deepcopy()로 복사한 결과 또한 값은 같지만 ID는 다르기 때문에 ==로 비교하면 True is로 비교할 경우 False가 된다

# 리스트
# 리스트는 입력 순서가 유지되며 내부적으로는 동적 배열로 구현되어 있다
# 파이썬의 리스트는 자바의 ArrayList와 유사하다
# 파이썬 리스트의 가장 좋은 점은 스택과 큐에서 사용 가능한 모든 연산을 함께 제공한다는 것이다
# 리스트 마지막 요소를 pop()으로 추출하는 것은 O(1)이지만 첫 번째 요소를 추출하는 pop(0)은 O(n)이다
# 이 경우 데크 자료형으로 성능을 높일 수 있다
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i, j, elem = 0, 10, 5
len(a) # O(1)
a[i] # O(1)
a[i:j] # O(k)
elem in a # O(n)
a.count(elem) # O(n)
a.index(elem) # O(n)
a.append(elem) # O(1) 리스트의 마지막에 요소를 추가한다
a.pop() # O(1) 리스트 마지막 요소를 추출한다
a.pop(0) # O(n) 리스트 첫 번째 요소를 추출한다
del a[i] # O(n)
a.sort() # O(n log n) Timsort를 사용하여 정렬한다
min(a), max(a) # O(n)
a.reverse # O(n)
# 리스트는 다음과 같이 선언한다
a = list
a = []
a = [0, 1, 2]
# 파이썬의 리스트는 다양한 자료형을 단일 리스테 관리할 수 있어 매우 편리하다
a = [0, 1, 2, 'hello', True]
# 리스트 슬라이싱
print(a[1:2]) # [1] 인덱스 1에서 인덱스 2 이전까지의 값으로 인덱스 2는 포함되지 않는다
print(a[1:4])
print(a[1:-1])
print(a[1:])
print(a[::2]) # 2칸씩 건너뛰게 된다

# 딕셔너리
# 키/값 구조로 이루어졌으며, 파이썬 3.7+에서는 입력 순서가 유지되며, 내부적으로는 해시 테이블로 구현되어 있다
# 자바의 HashMap과 유사하다
# 숫자뿐만 아니라, 문자, 집합까지 불변 객체를 모두 키로 사용할 수 있다
# 다양한 타입을 키로 지원하면서도 입력과 조회 모두 O(1)에 가능하다
a = {1:2, 2:3, 3:4}
key = 1
value = 10

len(a) # O(1)
a[key] # O(1)
a[key] = value # O(1)
key in a # O(1)

# 파이썬 3.6이하에서는 입력 순서가 유지되지 않아 collections.OrderedDict()라는 별도 자료형을 제공했다
# 파이썬 3.6부터는 딕셔너리의 메모리 사용량이 20% 정도 줄어드는 성능 개선 또한 진행됐다
# 항상 입력 순서가 유지되는 collections.OrderedDict()
# 조회 시 항상 기본 값을 생성해 키 오류를 방지하는 collections.defaultdict()
# 요소의 값을 키로 하고 개수를 값 형태로 만들어 카운팅하는 collections.Counter()
# 딕셔너리는 다음과 같이 선언할 수 있다
a = dict()
a = {1:'A'}
# 리스트에서는 존재하지 않는 인덱스를 조회할 경우 IndexError가 발생하며
# 딕셔너리에서는 존재하지 않는 키를 조회하면 KeyError가 발생한다
# KeyError는 키를 삭제할 때도 발생한다
try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키')

if 'key4' in a:
    print('존재하는 키')
else:
    print('존재하지 않는 키')

for k, v in a.items():
    print(k, v)

del a[1]



import collections

a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 6
print(a['c']) # 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = collections.Counter(a)
print(b.most_common(2)) # 가장 빈도가 높은 2개의 요소 추출
