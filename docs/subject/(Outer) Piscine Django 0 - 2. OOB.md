# Subject 번역

> 오늘, 당신은 Python으로 POO에서 ​​새로 습득한 기술로 실리콘 밸리를 정복할 것입니다!

## General rules

-   당신의 프로젝트는 반드시 VM위에서 구현해야 합니다.
-   당신의 VM은 프로젝트를 완료하기 위한 필요한 모든 소프트웨어가 설치되어 있고, 설정되어 있어야 합니다.
-   VM의 운영체제는 자유롭게 선택할 수 있습니다.
-   VM을 클러스터 컴퓨터에서 사용할 수 있어야 합니다.
-   VM과 호스트 머신 간 공유 폴더를 사용해야만 합니다.
-   평가 도중, 작업물을 옮기기 위해 이 공유 폴더를 사용할 것입니다.
-   당신의 함수들은 UB를 제외하고 예기치 못하게 종료되어선 안됩니다. (Seg fault, bus error, double free 등) 발생 시, 프로젝트가 정상 동작하지 않는 것으로 간주하고 0점을 받게 됩니다.
-   제출할 필요가 없고 채점되지 않더라도, 프로젝트에 대한 테스트 프로그램을 만드는 것이 좋습니다. 이렇게 하면 자신의 작업과 동료의 작업을 쉽게 테스트할 수 있습니다. 이러한 테스트는 디펜스 중에 특히 유용합니다. 실제로 디펜스 중에는 자신의 테스트 및/또는 평가하는 동료의 테스트를 자유롭게 사용할 수 있습니다.
-   할당된 git 저장소에 작업을 제출합니다. git 저장소에 있는 작업만 채점됩니다. 작업 채점을 위해 Deepthought이 배정된 경우, 동료 평가가 끝난 후에 채점이 이루어집니다. Deepthought이 채점하는 동안 작업의 어느 부분에서든 오류가 발생하면 평가가 중지됩니다.

## 추가되는 규칙

-   전역 스코프에는 코드를 적지 마세요! 우리는 함수를 원해요.
-   각 제출 파일의 끝에는 다음과 같은 조건문 안에서의 함수 호출이 있어야 합니다.

```python
if __name__ == '__main__':
	your_function(whatever, parameter, is, required)
```

-   캐치되지 않은 모든 예외는 테스트해야 하는 오류가 발생하더라도 작업을 무효화합니다.
-   예제에서 허용된 모듈을 제외하고 모든 `import`는 허용되지 않습니다.
-   `python3` 인터프리터를 사용해야 합니다.

## Ex 00

> 예제 0: 실리콘밸리 정복하기
>
> `ex00` 폴더 안에 `render.py`, `myCV.template`, `settings.py`로 제출
>
> `import sys, os, re` 허용

당신은 이제 막 놀라운 개발자 교육 과정을 수료하고, 새로운 관점으로 인생을 완전히 바꾸려고 합니다.
획기적인 기술로 혁신적인 이력서 생성기를 개발하여, 구직 업계의 빌 게이츠가 되겠다는 단 한 가지 목표를 염두에 두고 실리콘밸리에 도착합니다!

이제 남은 일은... 기술을 개발하는 것 입니다.

`.template` 확장자 파일을 인자로 받는 `render.py` 프로그램을 작성하세요. 이 프로그램은 파일의 내용을 읽어, `setting.py`에 정의된 값과 같은 패턴으로 대체하고, `.html` 확장자로 결과를 작성합니다. (`settings.py`에는 `__main__` 검사를 하지 않아도 됩니다.)

프로그램에서 다음 예제를 복제할 수 있어야 합니다.

```bash
$> cat settings.py
name = "duoquadragintian"
$> cat file.template
<p>"-Who are you?
-A {name}!"</p>
$> python3 render.py file.template
$> cat file.html
<p>"-Who are you?
-A duoquadragintian!"</p>
```

잘못된 파일 확장자나 존재하지 않는 파일, 잘못된 인자 개수등의 예외를 처리해야 합니다.

HTML로 변환된 `myCV.template` 파일을 제출해야 하며, 이 파일에는 최소한 이력서의 전체 구조(문서 형식, 머리글 및 본문 페이지, 페이지 제목, 이력서 소유자의 이름과 성, 나이 및 직업)가 포함되어야 합니다. 물론 이러한 정보가 `.template` 파일에 직접 표시되지는 않습니다.

> `help(globals)`, 키워드 확장(keyword expansion)...

## Ex 01

> 예제 1: 혁신적인 스타트업에서 인턴을 찾습니다. 경력 10년 이상
>
> `ex01/intern.py`로 제출.
>
> 허용 함수 없음

당신은 이 여정을 혼자 시작할 수 없습니다. 당신을 위해 ~~커피를 탈~~ 도울 누군가를 채용할 때는 인턴이 훨 낫습니다. (그게 훨씬 싸게 먹힙니다.)

다음 기능을 포함하는 `Intern` 클래스를 작성하세요.

-   `builder`는 문자열을 파라미터로 받아, `Name` 속성에 할당합니다. "My name? I’m nobody, an intern, I have no name." (제 이름? 전 아무도 아니에요, 인턴이에요, 이름이 없어요.)을 기본 값으로 설정합니다. (역: 생성자 인듯?)
-   `__str__()` 메서드는 해당 인스턴스의 `Name` 속성을 리턴합니다.
-   `Coffee` 클래스는 간단한 `__str__()` 메서드를 가지는 객체입니다. 다음 문자열을 반환합니다. "This is the worst coffee you ever tasted.". (이것은 당신이 지금껏 먹어본 커피 중 최악이다.)
-   `work()` 메서드는 다음 텍스트로 기본 `Exception` 을 발생시킵니다. "I’m just an intern, I can’t do that..." (저는 그냥 인턴이에요. 할 수 없어요...)
-   `make_coffee()` 메서드는 `Intern` 클래스 안에 구현된 `Coffee` 클래스의 인스턴스를 반환합니다.

테스트에서, 이름 없는 `Intern`와 `Mark` 라는 이름을 가진 `Intern` 을 인스턴스화 해야합니다.
각 인스턴스의 이름을 표시하고, `Mark`에게 커피를 요청하여 결과를 확인하세요. 테스트 스크립트에서도 반드시 예외를 핸들링해야 합니다.

## Ex 02

> 예제 2: 한 컵에 5개의 클래스
>
> `ex02/beverages.py`로 제출.
>
> 허용 함수 없음

커피는 최고예요. 더 좋아햐는 음료를 골라보세요! 다음 기능을 포함하는 `HotBeverage` 클래스를 작성합니다.

-   `price` 속성은 0.30의 값을 가집니다.
-   `name` 속성은 "hot beverage" 값을 가집니다.
-   `description()` 메서드는 description 인스턴스를 반환합니다. 해당 값은 "Just some hot water in a cup." 입니다.
-   `__str__()` 메서드는 다음과 같은 형식으로 인스턴스 설명을 반환합니다.
    ```text
    name : <name attribute>
    price : <price attribute limited to two decimal points>
    description : <instance's description>
    ```
    예를 들어, `HotBeverage` 인스턴스는 다음과 같이 출력됩니다.
    ```text
    name : hot beverage
    price : 0.30
    description : Just some hot water in a cup.
    ```
-   `HotBeverage` 클래스를 상속받는 다음의 클래스들을 작성하세요
    -   Coffee :
        -   name : "coffee"
        -   price : 0.40
        -   description : "A coffee, to stay awake."
    -   Tea
        -   name : "tea"
        -   price : 0.30
        -   description : "Just some hot water in a cup."
    -   Chocolate
        -   name : "chocolate"
        -   price : 0.50
        -   description : "Chocolate, sweet chocolate..."
    -   Cappuccino
        -   name : "cappuccino"
        -   price : 0.45
        -   description : “Un po’ di Italia nella sua tazza!”

> [필요한 것, 변경해야 할 것만, 재정의해야 할 것만 재정의해야 합니다... ](https://en.wikipedia.org/wiki/Don't_repeat_yourself)

당신의 테스트에서, 각 클래스를 인스턴스화 하여 출력하세요.

## Ex 03

> 예제 3: 영광스러운 커피머신!
>
> `ex03` 폴더 안에 `machine.py`, `beverages.py` 로 제출
>
> `import random` 허용

여기 계셨군요! 회사가 운영되고 있습니다! 첫 번째 펀드를 통해 건물을 마련했습니다. 커피를 담당할 인턴과 건물 입구에 모든 것을 관리할 레벨 10의 녹색 식물이 있습니다.

그렇지만, 모든 것이 완벽하지 않습니다: 인턴이 끔찍한 커피를 만들고, 최저 임금의 절반이 이 진흙탕에 들어가고 있어요. 여러분들의 개인적인 성공으로 이어질 새로운 장비에 투자할 때가 왔습니다!

다음을 포함하는 `CoffeeMachine` 클래스를 작성하세요.

-   `builder` (역: 이것도 생성자 인듯? 이제 builder = 생성자 로 번역)
-   `HotBeverage`를 상속하는 `EmptyCup` 클래스.
    -   name: "empty cup"
    -   price: 0.90
    -   description: "An empty cup?! Gimme my money back!" (뭐야 빈컵? 내 돈 돌려줘요)
    -   이전 예제의 클래스들을 `beverage.py` 에 복사하여 사용하세요.
-   기본 `Exception`을 상속하는 `BrokenMachineException`
    -   "This coffee machine has to be repaired." 를 표시합니다.
    -   이 텍스트는 객체의 생성자에서 정의되어야 합니다.
-   `repair()` 메서드는 기계를 고쳐 다시 따듯한 음료를 뽑을 수 있게 합니다.
-   `serve()` 메서드는 다음 스펙을 만족합니다.
    -   파라미터: `self`를 제외하고, `HotBeverage`를 상속받는 클래스를 유일한 인자로 가집니다.
    -   리턴: 무작위로 매개변수에 설정된 클래스의 인스턴스를 반환하거나, 그렇지 않으면 EmptyCup 인스턴스를 반환합니다.
    -   노후: 이 기계는 저렴해서, 10개의 음료수를 뽑은 후 고장납니다.
    -   고장난 경우: `serve()` 메서드 호출은 `repair()` 메서드가 호출될 때까지 CoffeeMachine.BrokenMachine 유형 예외를 발생시켜야 합니다.
    -   수리: `repair()` 메서드가 호출된 후, 다시 10번의 `serve()` 호출이 가능해집니다.

당신의 테스트에서, `CoffeeMachine` 을 인스턴스화 하세요. 기계가 고장날 때까지 `beverage.py`에 있는 다양한 음료를 주문해보세요. (당연히 발생하는 예외를 핸들링해야 합니다.) 기계를 고친 후 다시 고장날 때까지 음료를 주문해보세요. (당연히 x2 발생하는 예외를 핸들링해야 합니다.)

## Ex 04

> 예제 4: 기본 클래스 (ft. RMS)
>
> `ex04/elem.py`로 제출.
>
> 허용 함수 없음

이제 웹 가시성을 개선할 차례입니다. 새로 습득한 Python 기술을 사용하여 HTML 콘텐츠를 효율적으로 디자인하고 싶지만, 그 방법을 배우기 위해 상급자에게 조언을 구하고 싶습니다. 당신은 프로그래밍의 신을 위해 인턴을 제물로 바치기로 합니다.

이제 커피 머신이 생겼으니 그는 꽤 쓸모없어졌습니다... 그냥 불태워버려... 성 이그누시우스가 여러분 앞에 나타나 귀중한 계시를 전합니다:

"HTML 요소는 거의 동일한 구조(태그, 콘텐츠, 속성)를 공유한다. 이러한 공유된 동작과 사양을 모두 모을 수 있는 클래스를 만들어 파이썬의 레거시 포스를 사용하여 모든 것을 다시 작성할 필요 없이 간단하고 쉽게 이 클래스를 도출하는 것이 현명할 것이다."

그리고 나서야 성 이그누시오스는 여러분이 작업 중인 Mac을 보게 됩니다. 겁에 질린 그는 더 이상 고민하지 않고 테스트 파일과 불완전한 클래스만 남기고 도망칩니다. 서둘러 다음 사양으로 `Elem` 클래스를 완성합니다(채워야 할 부분은 `[...]`로 표시):

-   요소의 이름, HTML 속성 과 타입 (간단한 태그인지 더블 태그인지) (역: 꼭 닫아야하는 태그인가, 혼자 써도 되는 태그인가 구분하는 것 같음)
-   요소의 HTML 코드를 반환하는 `__str__()` 메서드
-   `add_content()` 메서드는 컨텐츠의 끝에 요소를 추가합니다.
-   관련된 `Exception` 서브클래스

작업이 잘 완료되었다면, `Elem` 클래스로 모든 HTML 요소와 그 컨텐츠를 표현할 수 있을 것입니다. 이제 마지막 단계입니다.:

-   인트라 서브젝트에 있는 `d02.tar.gz` 의 `tests.py` 가 정상 작동해야 합니다. (Assertion 오류가 없어야 하고, 테스트 출력에 성공이 명시적으로 표시되어야 합니다.)
-   물론, 이 예제에서 명시적으로 요구하지 않는 기능을 테스트할 만큼 잔인하지는 않습니다. 하하하.. 정말아닙니다.
-   또한 `Elem` 클래스를 통해 다음 구조를 복제하여 표시해야 합니다.

```html
<html>
    <head>
        <title>"Hello ground!"</title>
    </head>
    <body>
        <h1>"Oh no, not again!"</h1>
        <img src="http://i.imgur.com/pfp3T.jpg" />
    </body>
</html>
```

## Ex 05

> 예제 5: 당신 만의 요소를 만들어보세요!
>
> `ex05` 폴더 안에 `elem.py`, `elements.py` 로 제출
>
> 허용 함수 없음

축하합니다! 이제 당신은 어떠한 HTML 요소와 컨텐츠를 생성할 수 있게 되었어요. 그러나, 각 인스턴스화 마다 각 속성을 지정하는 각 요소를 생성하는 작업은 좀 지루합니다. 여기 레거시를 사용하여 더 사용하기 쉬운 작은 클래스들을 만들 기회가 있습니다. 이전 예제에서 만든 `Elem` 클래스를 상속하는 다음 클래스들을 작성합니다.:

-   html, head, body
-   title
-   meta
-   img
-   table, th, tr, td
-   ul, ol, li
-   h1
-   h2
-   p
-   div
-   span
-   hr
-   br

각 클래스의 생성자는 컨텐츠를 첫 번째 인자로 받을 수 있습니다.:
`print( Html( [Head(), Body()] ) )` 의 결과는 다음과 같습니다.

```html
<html>
    <head></head>
    <body></body>
</html>
```

현명하게, `Elem` 클래스에서 코딩한 기능을 재사용하세요.
모든 기능을 포괄하는 여러가지 테스트(당신의 선택입니다.)를 통해, 이러한 클래스들이 어떻게 작동하는지 보여주세요. 이러한 클래스를 코딩한 후에는 태그의 이름이나 유형을 지정할 필요가 없으므로 매우 편리합니다. 다시는 Elem 클래스를 직접 인스턴스화할 필요가 없습니다. 사실은, 이제부터 `Elem` 클래스의 인스턴스화는 금지됩니다.

`d'Elem`을 직접 사용할 때와 비교하여 `d'Elem` 파생 클래스의 이점을 이해하기 위해 이전 예제의 HTML 문서 구조를 가져와 보겠습니다. 새 클래스를 사용하여 이를 복제해야 합니다.

```html
<html>
    <head>
        <title>"Hello ground!"</title>
    </head>
    <body>
        <h1>"Oh no, not again!"</h1>
        <img src="http://i.imgur.com/pfp3T.jpg" />
    </body>
</html>
```

어때요, 더 간단하지 않나요? :)

## Ex 06

> 예제 6: 검증
>
> `ex06` 폴더 안에 `Page.py`, `elem.py`, `elements.py` 로 제출
>
> 허용 함수 없음

놀라운 진전을 이루었지만 작업에는 여전히 약간의 정리가 필요합니다. 조금 더 순응하세요. 여러분은 제약과 도전을 좋아합니다. 그렇다면 HTML 문서의 구조에 규범을 적용하는 것은 어떨까요? 이 연습의 폴더에 이전 두 예제의 클래스를 복사하기 시작하세요.

`Page` 클래스를 작성하세요. 생성자는 `Elem` 클래스를 상속하는 클래스의 인스턴스를 인자로 받습니다.
`Page` 클래스는 반드시 `is_valid()` 메서드를 구현해야 합니다. 다음 규칙을 만족하면 `True`, 아니면 `False` 를 반환합니다.:

-   트리 경로에서 노드에 html, head, body, title, meta, img, table, th, tr, td , ul, ol, li, h1, h2, p, div, span, hr, br 또는 Text 유형 중 하나가 없는 경우 트리가 유효하지 않습니다.
-   Html은 엄격하게 헤드와 바디를 포함해야 합니다.
-   Head에는 제목이 하나만 포함되어야 하고 유일해야 합니다.
-   Body와 Div에는 다음 유형의 요소만 포함되어야 합니다: H1, H2, Div, Table, Ul, Ol, Span 또는 Text.
-   Title, H1, H2, Li, Th, Td에는 Text 하나만 포함해야 하며 이 Text만 포함해야 합니다.
-   P는 Text만 포함해야 합니다.
-   Span은 Text 또는 일부 P만 포함해야 합니다.
-   Ul과 Ol은 하나 이상의 Li와 일부 Li만 포함해야 합니다.

당신의 `Page` 클래스는 또한:

-   인스턴스를 `print` 할 때 해당 HTML 코드를 표시합니다.
    -   주의: 표시되는 HTML 코드 앞에는 루트 요소 유형이 Html인 경우에만 doctype이 와야 합니다.
-   파일 이름을 매개변수로 사용하는 `write_to_file` 메서드를 사용하여 파일에 HTML 코드를 작성합니다.
    -   주의: 파일에 작성된 HTML 코드는 루트 요소의 유형만 Html인 경우에만 doctype이 앞에 와야 합니다.

모든 기능을 포괄하는 여러 가지 테스트를 통해, `Page` 클래스가 어떻게 동작하는지 보여주세요. (선택)
