# Subject 번역

> 오늘은 파이썬의 구문론과 의미론의 기초를 알아보는 여정을 시작하겠습니다.

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

-   위 조건문에서 오류 관리를 설정할 수 있습니다.
-   예제에서 허용된 모듈을 제외하고 모든 `import`는 허용되지 않습니다.
-   `open` 함수로 인해 발생할 수 있는 예외는 처리하지 않아도 됩니다.
-   `python3` 인터프리터를 사용해야 합니다.

## Ex 00

> 예제 0: 내 첫 변수
>
> `ex00/var.py`로 제출.
>
> 허용 함수 없음

`my_var` 함수를 정의하는 `var.py` 스크립트를 작성하세요. 이 함수는 9개의 각기 다른 타입의 변수를 선언하고 `stdout`에 출력합니다. 출력은 정확하게 다음과 같습니다.:

```bash
$> python3 var.py
42 has a type <class 'int'>
42 has a type <class 'str'>
quarante-deux has a type <class 'str'>
42.0 has a type <class 'float'>
True has a type <class 'bool'>
[42] has a type <class 'list'>
{42: 42} has a type <class 'dict'>
(42,) has a type <class 'tuple'>
set() has a type <class 'set'>
$>
```

당연하게도, 변수 타입을 명시적으로 작성하여 그대로 출력하는 것은 엄격하게 금지되어 있습니다.
스크립트 끝에 함수 호출 하는 것을 잊지마세요!:

```python
if __name__ == '__main__':
	my_var()
```

## Ex 01

> 예제 1: 숫자
>
> `ex01/numbers.py`로 제출.
>
> 허용 함수 없음

이 예제에서는 원하는 만큼 함수를 만들고, 마음대로 이름을 지을 수 있습니다.
인트라 첨부파일에 있는 `d01.tar.gz` 에는 `ex01` 서브 폴더가 있고, 그 안에는 `numbers.txt` 라는 1부터 100까지의 숫자가 쉼표로 구분된 문자열이 적힌 파일이 있습니다.
`numbers.py`라는 파이썬 스크립트를 설계하세요. `numbers.txt` 파일을 열어 숫자를 읽고, 한 줄에 하나씩 쉼표 없이 `stdout`에 출력합니다.

## Ex 02

> 예제 2: 내 첫 딕셔너리
>
> `ex02/var_to_dict.py`로 제출.
>
> 허용 함수 없음

다시 한 번, 원하는 만큼 함수를 만들고, 마음대로 이름을 지을 수 있습니다. 명시적으로 모순되는 경우를 제외하고는 이 지침을 반복하지 않겠습니다.

쌍으로 된 다음 리스트 `d` 를 딕셔너리로 바꾸는 스크립트인 `var_to_dict.py`를 작성하세요.

```python
d = [
	('Hendrix' , '1942'),
	('Allman' , '1946'),
	('King' , '1925'),
	('Clapton' , '1945'),
	('Johnson' , '1911'),
	('Berry' , '1926'),
	('Vaughan' , '1954'),
	('Cooder' , '1947'),
	('Page' , '1944'),
	('Richards' , '1943'),
	('Hammett' , '1962'),
	('Cobain' , '1967'),
	('Garcia' , '1942'),
	('Beck' , '1944'),
	('Santana' , '1947'),
	('Ramone' , '1948'),
	('White' , '1975'),
	('Frusciante', '1970'),
	('Thompson' , '1949'),
	('Burton' , '1939')
]
```

스크립트는 이 변수를 딕셔너리로 바꿔야 합니다. 연도는 키가 되고 뮤지션의 이름은 값이 됩니다. 그런 다음 이 딕셔너리를 명확한 형식에 따라 `stdout`에 표시해야 합니다:

```bash
1970 : Frusicante
1954 : Vaughan
1948 : Ramone
...
```

> 최종 순서는 예제와 다를 수 있습니다. 이것은 일반적인 행동입니다. 왜그런지 아시나요?

## Ex 03

> 예제 3: 키(Key) 탐색
>
> `ex03/capital_city.py`로 제출.
>
> `import sys` 허용

다음은 스크립트의 함수 중 하나에서 변경하지 않고 복사해야 하는 사전입니다:

```python
states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
}

capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
}
```

`state`를 인자로 받아서 `capital_city`를 `stdout`에 출력하는 프로그램을 작성하세요. 알 수 없는 `state`가 인자로 들어온다면, `Unknown state`를 출력하세요. 인자가 주어지지 않거나, 너무 많이 주어지면 아무것도 하지 않고 종료되어야 합니다.

```bash
$> python3 capital_city.py Oregon
Salem
$> python3 capital_city.py Ile-De-France
Unknown state
$> python3 capital_city.py
$> python3 capital_city.py Oregon Alabama
$> python3 capital_city.py Oregon Alabama Ile-De-France
$>
```

## Ex 04

> 예제 4: 값으로 찾기
>
> `ex04/state.py`로 제출.
>
> `import sys` 허용

이전 예제와 똑같은 딕셔너리들이 주어집니다. 스크립트의 함수 중 하나에서 변경하지 않고 복사하세요.

이번에는 `capital_city`를 인자로 받아서 `state`를 출력하는 프로그램을 작성하세요. 프로그램의 나머지 동작은 이전 예제와 동일해야 합니다.

```bash
$> python3 state.py Salem
Oregon
$> python3 state.py Paris
Unknown capital city
$> python3 state.py
$>
```

## Ex 05

> 예제 5: 키나 값으로 찾기
>
> `ex05/all_in.py`로 제출.
>
> `import sys` 허용

이전 예제와 똑같은 딕셔너리에서 시작하여 스크립트의 함수 중 하나에 변경하지 않고 복사한 다음, 다음과 같이 동작하는 프로그램을 작성하세요.

-   프로그램은 검색할 만큼의 표현식이 포함된 문자열을 쉼표로 구분하여 인자로 받아야 합니다.
-   이 문자열의 각 표현식에 대해 프로그램은 `state`인지 `capital_city`인지 감지해야 합니다.
-   프로그램은 대소문자를 구분하지 않아야 합니다. 또한 여러 개의 공백을 고려하지 않습니다.
-   매개변수가 없거나 너무 많으면, 프로그램은 아무 동작도 하지 않고 종료됩니다.
-   문자열에 연속된 쉼표가 2개 있는 경우, 프로그램은 아무 동작도 하지 않고 종료됩니다.
-   프로그램은 결과를 캐리지 리턴으로 구분하여 표시해야 하며, 엄격하게 다음의 형식을 따라야 합니다.

```bash
$> python3 all_in.py "New jersey, Tren ton, NewJersey, Trenton, toto, , sAlem"
Trenton is the capital of New Jersey
Tren ton is neither a capital city nor a state
NewJersey is neither a capital city nor a state
Trenton is the capital of New Jersey
toto is neither a capital city nor a state
Salem is the capital of Oregon
$>
```

## Ex 06

> 예제 6: 딕셔너리 정렬
>
> `ex06/my_sort.py`로 제출.
>
> 허용 함수 없음

이 딕셔너리를 당신의 함수에 포함시키세요.:

```python
d = {
	'Hendrix' : '1942',
	'Allman' : '1946',
	'King' : '1925',
	'Clapton' : '1945',
	'Johnson' : '1911',
	'Berry' : '1926',
	'Vaughan' : '1954',
	'Cooder' : '1947',
	'Page' : '1944',
	'Richards' : '1943',
	'Hammett' : '1962',
	'Cobain' : '1967',
	'Garcia' : '1942',
	'Beck' : '1944',
	'Santana' : '1947',
	'Ramone' : '1948',
	'White' : '1975',
	'Frusciante': '1970',
	'Thompson' : '1949',
	'Burton' : '1939',
}
```

연도별로 오름차순 정렬된 뮤지션들의 이름을 출력하는 프로그램을 작성하세요. 년도가 같을 경우 알파벳 순으로 정렬합니다. 한 줄에 한 명씩, 연도 없이 이름만 출력합니다.

## Ex 07

> 예제 7: 원소 주기율표
>
> `ex07/periodic_table.py`로 제출.
>
> `import sys` 허용

인트라 첨부파일에 있는 `d01.tar.gz` 에는 `ex07` 서브 폴더가 있고, 그 안에서 프로그래머들을 위한 형식으로 적힌 원소 주기율표 파일인 `periodic_table.txt`를 찾을 수 있을겁니다.

파일을 사용하여 적절한 형식으로 원소 주기율표를 표시할 수 있는 HTML 페이지를 작성하는 프로그램을 만드세요.

-   각 원소는 HTML 표의 `bot` 안에 있어야 합니다.
-   각 원소의 이름은 `<h4>` 태그 안에 있어야 합니다.
-   각 원소의 속성은 리스트로 표시되어야 합니다. 리스트에는 최소한 원소 번호, 기호 및 원자 질량이 명시되어야 합니다.
-   최소한 Google에 표시되는 멘델레예프 표의 레이아웃을 준수해야 합니다. 빈 상자가 있어야 할 곳에 빈 상자가 있어야 하고, 캐리지 리턴이 있어야 할 곳에 캐리지 리턴이 있어야 합니다.

프로그램에서 결과 파일 `periodic_table.html`을 생성해야 합니다. 물론 이 HTML 파일은 모든 브라우저에서 읽을 수 있어야 하며 `W3C`에 유효한 파일이어야 합니다.

프로그램을 원하는 대로 자유롭게 디자인할 수 있습니다. 재사용할 수 있는 특정 기능으로 코드를 쪼개는 것을 주저하지 마세요. CSS "인라인" 스타일로 태그를 사용자 정의하여 턴인을 더 예쁘게 만들 수 있습니다(표의 테두리 색상을 생각해보세요). 원하는 경우 `periodic_table.css` 파일을 생성할 수도 있습니다.

다음은 아이디어를 얻을 수 있는 출력 예제 발췌문입니다:

```html
[...]
<table>
    <tr>
        <td style="border: 1ps solid black; padding:10px">
            <h4>Hydrogen</h4>
            <ul>
                <li>No 42</li>
                <li>H</li>
                <li>1.00794</li>
                <li>1 electron</li>
            </ul>
        </td>
        [...]
    </tr>
</table>
```
