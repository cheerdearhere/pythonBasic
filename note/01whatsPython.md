
# I. 사용하는 이유
- 소프트웨어 관리에 유용하다
    - 읽고 쓰기 편하다
    - Objected-Oriented(객체지향 언어)
- 개발 속도가 빠르다
    - 다른 언어에 비해 코드를 짧게 작성할 수 있다.
- 거의 모든 플랫폼에 파이썬 코드를 이식할 수 있다
    - 리눅스/윈도우/맥 모두 같은 코드로 운영 가능
- 어플리케이션간 소통이 원활하다
    - 부분적으로 파이썬 사용 가능
    - C or C++ 라이브러리들 사용 가능
- 사용처
    - 시스템 개발(OS)
    - GUI(Graphical User Interface): ex) Tkinter
    - 웹 어플리케이션 개발: front, back 모두 가능
    - 많은 언어, 어플리케이션과 소통, 결합 가능(C, C++ 사용한 프로그램): ex) 엑셀
    - 프로토타입 프로그래밍: python으로 우선 프로토타입을 뽑고 C언어로.
    - 데이터 관련 작업
    - 이외에도 다양한 영역에서 사용
# II. 장점 단점
## A. 단점
- 소스코드 > 바이트코드 > 머신코드 과정을 거치기에 저급언어에 비해 느리다
- C 언어로 된 라이브러리를 사용할 수 있어 필요한 부분에서 더빠른 속도를 확보할 수 있다.
    - ex) NumPy library(C)
## B. 장점
- 객체지향언어
- 무료, 오픈소스 라이브러리 많음
- 타입 추론, 메모리 관리 등 사용자 편의성이 좋은 편
# III. 파이썬 탄생 이야기
- Guido van Rossum 개발
- 파이썬에 `import this` 코드를 쓰면 파이썬의 철학에 대해 나옴
  - 프로그램내에서 한번만 사용 가능
```
Beautiful is better than ugly. 아름다움이 추함보다 좋다.
Explicit is better than implicit. 명백함이 모호함보다 좋다.
Simple is better than complex. 단숨함이 복잡함보다 좋다.
Complex is better than complicated. 복합성이 어수선한 것보다 좋다.
Flat is better than nested. 펼쳐놓는 것이 중첩보다 좋다.
Sparse is better than dense. 드문드문한 것이 조밀한 것보다 좋다.
Readability counts. 가독성은 중요합니다.
Special cases aren't special enough to break the rules. 특별한 경우들은 룰을 어길 정도로 특별하지 않다.
Although practicality beats purity. 실제적이고 실용적인 것이 순수함을 이긴다.
Errors should never pass silently. 오류는 말없이 지나쳐선 안된다.
Unless explicitly silenced. 명백하지 않으면 말하지 않는다.
In the face of ambiguity, refuse the temptation to guess. 모호함에 마주하게 되면 추측하지 말아라.
There should be one-- and preferably only one --obvious way to do it. 어떤 일을 하는 확실한 방법이 (될 수 있으면 하나만) 있어야 한다.
Although that way may not be obvious at first unless you're Dutch. 처음에는 어떤 방식이 분명하지 않을 수 있다.
Now is better than never. 지금이 일찍이 어떤 때보다 좋다.
Although never is often better than *right* now. 한 번도 일어나지 않는 것이 당장 일어나는 것보다 더 좋다.
If the implementation is hard to explain, it's a bad idea. 설명하기 어려운 구현은 좋지 않은 아이디어다.
If the implementation is easy to explain, it may be a good idea. 설명하기 쉬운 구현은 좋은 아이디어에 가깝다.
Namespaces are one honking great idea -- let's do more of those! 이름 공간은 좋은 생각이지만 그 이상을 수행하자.
```
# IV. 프로그래밍 언어의 작동
- 컴퓨터가 이해할 수 있는 기계어와 사람의 언어(high level)로 분류
  - input: 컴퓨터에 사람이 명령, 전달
  - output: 수행한 결과를 사람에게 전달
- 기계어에 더 가까운 언어<(low level)------------(high level)>사람말에 더 가까운 언어
  - `<---python/javascript----C/C++------assemblyLanguage>`
- 컴퓨터 동작 방식
  - 외부 저장 메모리 -> RAM -> CPU(연산) -> RAM -> 외부 저장 메모리
- 기본은 +연산. 이를 묶음으로 만들어 사칙연산, 조작문 등을 처리
- 고급언어를 저급언어로 번역해 실행시키는 역할
- 통역과정: python script > compiler > byte code > python VM -> machine code

# V. 파이썬 실행시키기
- 파이썬 관련 설치
  - [파이썬 페이지에서 인터프리터를 받음](https://www.python.org/)
  - [자바 프로그래머인 경우](https://www.jython.org/)
  - [데이터 처리인경우](https://docs.conda.io/en/latest/)
  - mac인 경우 [homebrew](https://brew.sh/)로 관리
- 설치하지 않고 txt 파일을 만들어 작성한 뒤 확장자를 py로 변경. 
- 원하는 버전으로 실행