# Subject 번역

> 오늘은 파이썬에서 유용하게 사용할 수 있는 몇 가지 라이브러리를 다루는 방법을 배워보겠습니다.

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

-   전역 스코프에는 코드를 적지 마세요! 함수를 만드세요!
-   각 제출 파일의 끝에는 다음과 같은 조건문 안에서의 함수 호출이 있어야 합니다.

```python
if __name__ == '__main__':
	your_function(whatever, parameter, is, required)
```

-   위 조건문에서 오류 관리를 설정할 수 있습니다.
-   예제에서 허용된 모듈을 제외하고 모든 `import`는 허용되지 않습니다.
-   `python3` 인터프리터를 사용해야 합니다.

## Ex 00

> 예제 0: 반중력
> `ex00/geohasing.py` 로 제출
> `sys`, `antigravity` 모듈 허용

오늘의 서두를 반복하는 간단한 준비 운동입니다. (역: 서브젝트의 서두에 지오해싱 위키피디아 글이 있음) 그리 복잡하지 않습니다.
일반적인 지오해시를 계산하는 데 필요한 만큼의 매개변수를 받아 표준 출력에 표시하기 전에 반드시 이 지오해시를 계산해야 하는 `geohashing.py`라는 이름의 작은 프로그램을 작성합니다.
오류가 발생하면 프로그램이 제대로 종료되기 전에 당신이 선택한 관련 메시지를 표시해야 합니다.
이 설계도가 도움이 될 수 있습니다: [지오해싱 알고리즘](http://xkcd.com/426/)

## Ex 01

> 예제 1: pip
> `ex01` 폴더 안에 `my_script.sh`, `my_program.py` 로 제출
> `path` 모듈 허용 (이전에는 `path.py` 로 불림)

[path](https://pypi.org/project/path/) 는 파이썬의 `os.path` 모듈을 중심으로 Path 객체를 구현하는 라이브러리로, 매우 직관적으로 사용할 수 있습니다.
이 예제에서는 이 라이브러리를 설치하는 bash 스크립트와 이를 사용하는 파이썬 프로그램을 만들 것입니다.
쉘 스크립트는 이 설명에 적합해야 합니다:

-   쉘 스크립트이므로 이름 확장자가 `.sh`여야 합니다.
-   사용하는 pip 버전을 표시해야 합니다.
-   GitHub 리포지토리의 `path.py` 개발 버전을 `local_lib`라는 이름의 폴더에 설치해야 합니다. 해당 폴더에 라이브러리가 이미 설치되어 있는 경우 설치 시 이를 제거해야 합니다.
-   `path` 설치 로그를 확장자가 `.log`인 파일에 작성해야 합니다.
-   라이브러리가 제대로 설치되었다면 당신이 만든 작은 프로그램을 실행해야 합니다.

당신이 만들어야 하는 파이썬 프로그램은 이러한 제약 조건을 준수해야 하지만, 원하는 대로 구성할 수 있습니다:

-   파이썬이기 때문에 확장자는 `.py`여야 합니다.
-   이전 스크립트로 설치한 라이브러리의 위치에서 `path` 모듈을 가져와야 합니다.
-   이 폴더 안에 폴더와 파일을 생성하고, 이 파일에 무언가를 작성한 다음, 그 내용을 읽고 표시해야 합니다.
-   [추가되는 규칙](#추가되는 규칙)을 준수해야 합니다.

## Ex 02

> 예제 2: API 요청하기
> `ex02` 폴더 안에 `request_wikipedia.py`와 `requirement.txt` 제출
> `requests`, `json`, `dewiki`, `sys` 모듈 허용

위키피디아는 여러분이 반드시 알아야 할 놀라운 공유 도구입니다. 즐겨 사용하는 브라우저와 모바일 애플리케이션으로 이용할 수 있습니다. 이제 필수적인 이 웹사이트를 터미널에서 바로 요청할 수 있는 도구를 만들도록 초대받았습니다.

이렇게 하려면 매개변수로 문자열을 받아 [위키피디아 API](https://www.mediawiki.org/wiki/API:Main_page)를 통해 검색한 후 결과를 파일에 기록하는 `request_wikipedia.py`라는 프로그램을 설계해야 합니다. 프랑스어 또는 영어 API를 요청할 수 있습니다.

-   요청의 스펠링이 틀린 경우에도 프로그램은 결과를 작성해야 합니다. 원본 웹사이트를 예로 들면, 특정 요청에 대한 결과를 찾으면 프로그램도 결과를 찾아야 합니다.
-   결과는 파일에 기록하기 전에 JSON 또는 위키 마크업으로 포맷되어서는 안 됩니다.
-   파일 이름은 `name_of_the_search.wiki` 형식이며, 어떠한 공백도 포함되어서는 안됩니다.
-   매개변수 부재, 잘못된 매개변수, 잘못된 요청, 정보를 찾을 수 없음, 서버 문제 또는 기타 문제가 있는 경우: 파일이 생성되지 않아야 하며 콘솔에 관련 오류 메시지가 표시되어야 합니다.
-   `requirement.txt` 파일을 레포에 포함하세요. 이 파일은 평가 중에 `VirtualEnv` 프로그램이나 시스템에 필요한 라이브러리를 설치하는 데 사용됩니다.

> dewiki 라이브러리는 완벽하지 않습니다. 최상의 결과를 찾는 것은 이 예제의 목표가 아닙니다.

> API 설명서를 주의 깊게 읽어보세요. 반환되는 구조를 주의 깊게 살펴보세요.

다음은 예상되는 사항의 예시입니다:

```bash
$>python3 request_wikipedia.py "chocolatine"
$>cat chocolatine.wiki

Une chocolatine designe :
* une viennoiserie au chocolat, aussi appelee pain au chocolat ou couque au chocolat ;
* une viennoiserie a la creme patissiere et au chocolat, aussi appelee suisse ;
* une sorte de bonbon au chocolat ;
* un ouvrage d'Anna Rozen

Malgre son usage ancien, le mot n'est entre dans le dictionnaire Petit Robert qu'en 2007 et dans 1e
Petit Larousse qu'en 2011.

L'utilisation du terme "Chocolatine" se retrouve egalement au Quebec, dont la langue a evolue a partir du vieux francais differemment du francais employe en Europe, mais cet usage ne prouve ni n' infirme aucune anteriorite, dependant du hasard de l'usage du premier comnercant l'ayant introduit au Quebec.

References

Categorie:Patisserie
Categorie: Chocolat
```

## Ex 03

> 예제 3: HTML 파서
> `ex03` 폴더 안에 `roads_to_philosophy.py`, `requirement.txt` 로 제출
> `sys`, `requests`, `BeautifulSoup` 모듈 허용

전설에 따르면, 아무 위키백과 문서에서 시작하여 이탤릭체나 괄호 사이에 있는 이 문서 소개의 첫 번째 링크를 클릭하고 이 과정을 애드리브로 반복하면 항상 `철학`에 관한 문서로 이동하게 된다고 합니다.

이건 전설이 아닙니다! (제발 놀란표정..) 이를 증명할 수 있듯... (위키피디아 아티클)
(역: 진짜 서브젝트가 이럼...)

하지만 여러분은 눈으로 보는 것만 믿기 때문에, 요청과 위키피디아 아티클 사이의 모든 아티클을 나열하고 세는 이 현상을 테스트하는 프로그램인 `roads_to_philosophy`을 만들어야 합니다.

이 프로그램의 이름은 반드시 `roads_to_philosophy.py` 여야 하며, 다음과 같이 행동합니다:

-   프로그램은 하나의 위키백과 검색과 일치하는 단어 또는 단어 그룹인 문자열을 매개변수로 사용해야 합니다.
-   프로그램은 브라우저의 표준 검색과 동일한 **영어** 위키피디아 URL을 요청해야 합니다. 즉, 사이트의 API를 사용할 수 **없습니다.**
-   `BeautifulSoup` 라이브러리를 통해 `html` 페이지를 파싱해야 합니다.
    -   최종 리디렉션을 찾아 `roads_to_philosophy`에서 이를 고려하세요. URL 리디렉션이 아니니 주의하세요.
    -   페이지의 메인 제목을 찾아 철학으로 가는 길에 추가합니다.
    -   다른 위키백과 문서로 연결되는 소개 단락의 첫 번째 링크를 찾습니다(있는 경우). 이탤릭체나 괄호 사이의 내용을 무시하지 말고, 위키백과 도움말 섹션으로 연결되는 링크와 같이 새 문서로 연결되지 않는 링크는 주의해서 무시해야 합니다.
-   이전 단계에서 획득한 링크에서 **2단계**부터 다시 시작하여 해당 항목 중 하나에 도달할 때까지 프로그램을 다시 시작해야 합니다:
    -   링크가 `철학` 페이지에 연결되는 경우, 표준 출력에 다음과 같이 출력합니다: `<number> roads from <request> to philosophy`
    -   페이지가 [어떠한 유효한 링크](https://en.wikipedia.org/wiki/Category:All_dead-end_pages)도 포함하지 않는 경우, 다음과 같이 출력합니다: `It leads to a dead end !`
    -   링크가 이미 방문했던 페이지로 연결되는 경우에는 프로그램이 무한 반복될 겁니다. 무한 반복을 막고 다음과 같이 출력합니다: `It leads to an infinite loop !`
-   이 단계에서 표준 출력에 필요한 메시지를 표시한 후 프로그램이 제대로 종료되어야 합니다.

> 프로그램 실행 중 언제라도 연결, 서버, 매개변수, 요청 오류 또는 기타 오류와 같은 오류가 발생하면 관련 오류 메시지와 함께 프로그램이 올바르게 종료되어야 합니다.

이전 연습과 마찬가지로, 라이브러리 설치를 용이하게 하려면 프로그램과 함께 `requirement.txt` 파일을 제공해야 합니다.

프로그램의 출력은 반드시 이와 같습니다.

```bash
$>python3 roads_to_philosophy.py "42 (number)"
42 (number)
Natural number
Mathematics
Ancient Greek
Greek language
Modern Greek
Colloquialism
Word
Linguistics
Science
Knowledge
Awareness
Conscious
Consciousness
Quality (philosophy)
Philosophy
17 roads from 42 (number) to philosophy !
$ python3 roads_to_philosophy-py Accuvio
It's a dead end !
$>
```

> 위키피디아 커뮤니티는 종종 아티클들을 업데이트 합니다. 이 서브젝트를 만든 날과 당신이 이걸 읽은 날 그 사이, 철학으로 가는 길이 바뀌었기에 Accuvio의 예시는 더 이상 막다른 골목이 아닙니다.

## Ex 04

> 예제 4: Virtualenv
> `ex04` 폴더 안에 `my_script.sh`, `requirement.txt` 로 제출
> 모든 함수 허용

내일, 당신은 `Django` 프레임워크 훈련을 시작할 것입니다. 따라서 간단한 설치를 구성하는 기초를 마련해야 합니다.

그러기 위해서, 두 가지 요소를 작성합니다:

-   `django`와 `psycopg2` 의 최신 안정 버전을 포함하는 `requirement.txt`
-   다음의 동작을 수행하는 스크립트
    -   `.sh` 확장자를 가짐
    -   `django_venv` 라는 이름의 `virtualenv`를 생성
    -   생성한 `django_venv` 에 `requirement.txt` 파일을 설치
    -   스크립트 종료 시 `django_venv` 활성화

## Ex 05

> 예제 5: Hello World
> `ex05` 폴더 안에 필요한 모든 파일 제출
> 모든 함수 허용

단순히 장고를 설치하는 것만으로는 답답하실 겁니다. 저희도 이해합니다.

그래서 오늘은 장고로 첫 번째 Hello World를 설계하면서 라이브러리에 대한 이야기를 마무리하겠습니다.

이 마지막 연습에서는 공식 튜토리얼을 따라 다음 주소(http://localhost:8000/helloworld)에서 브라우저에 Hello World! 라는 텍스트를 간단히 표시하는 웹 페이지를 만들어야 합니다.

저장소는 장고 프로젝트가 포함된 폴더여야 합니다.
