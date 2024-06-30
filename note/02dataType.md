
- Object Oriented Programming: 객체 지향 프로그래밍
  - 뜻
    - Object: 물건/객체
      - 어떠한 용도를 위해 만들어진 도구
      - 이미 만들어진 것이 있다면 새로 만들지 않고 재사용함
      - 각각의 목적에 따라 생성되어 기능을 담당함
      - 같은 역할을 하는 것들을 모아 '타입'으로 사용
    - Oriented: ~로 만들어진/ ~에서 기인한
    - Programming
  - 같은 형태의 인스턴스를 생성하기 위해 클래스를 사용
    - 클래스는 용도에 맞는 객체를 생성하도록 도움
    - 생성된 인스턴스 사이의 소통으로 프로그램이 운영
# I. 데이터 타입
- Data type: 데이터를 저장하는 방식
- built-in: 파이썬에서 기본적으로 제공하는 라이브러리의 data type
  - int, float, bool, str, list, tuple, set, dict, none...
## A. 데이터 타입 확인하기
- 핵심 객체 보는 방법
  - `객체.__class__`
  - `type(객체)`
```python
x = 100
print(x.__class__)
print(x.__class__.__class__)
print(type(x))
print(type(type(x))) 
```
- console
```
<class 'int'>
<class 'type'>
<class 'int'>
<class 'type'>
```
- 데이터 관련 키워드
  - class: 직접 객체(타입)를 만들때 사용
  - modules: 기존에 만든 객체들을 가져와 사용
  - libraries: 모듈의 모임. package 단위
    - ex) Pandas, Numpy, Matplotlib...
## B. 데이터 타입 관련 기본 라이브러리 맛보기
- Numbers: 숫자형
  - Integer: 정수
  - Float: 실수(정수 제외)
  - Boolean: True and False(1, 0) 
    - 다른 언어에서는 boolean이 별도의 유형일 때도 있음
```python
X = 400
print("X isInt? {0}".format(isinstance(X, int)))#True
print("X isFloat? {0}".format(isinstance(X, float)))
print("X isString? {0}".format(isinstance(X, str)))
print("X isBoolean? {0}".format(isinstance(X, bool)))

Y = 400.1
print("Y isInt? {0}".format(isinstance(Y, int)))
print("Y isFloat? {0}".format(isinstance(Y, float)))#True
print("Y isString? {0}".format(isinstance(Y, str)))
print("Y isBoolean? {0}".format(isinstance(Y, bool)))

Z = True
X = 400
print("Z isInt? {0}".format(isinstance(Z, int)))#True
print("Z isFloat? {0}".format(isinstance(Z, float)))
print("Z isString? {0}".format(isinstance(Z, str)))
print("Z isBoolean? {0}".format(isinstance(Z, bool)))#True
```
# II. Numbers
# III. String
# IV. List
# V. Dictionary
# VI. Tuple
# VII. None
# IIX. immutable variable vs mutable variable 

[연습용 코드](../src/ex02_dataType.py)