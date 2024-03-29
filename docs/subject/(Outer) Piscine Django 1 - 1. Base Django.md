# Subject 번역

> 파이썬 이후, 장고!

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

-   애플리케이션과 관련된 모든 경로는 이 애플리케이션의 폴더에 있는 `urls.py` 파일에 정의되어야 합니다.
-   모든 폼(`django.forms.Form`의 파생 클래스)은 관련된 `forms.py` 애플리케이션의 파일에 위치해야 합니다.
-   표시되는 각 페이지는 형식이 올바르게 지정되어야 하며(doctype, 몇 개의 `html` 태그, `body`, `head`가 포함되어야 함), 특수 문자를 적절히 관리하고, 이상한 표시가 없어야 합니다.
-   오늘은 `manage.py` 유틸리티와 함께 제공되는 장고의 기본 개발 서버를 사용하겠습니다.
-   특별히 요청된 URL만 오류 없이 페이지를 반환해야 합니다. 따라서 `/ex00`만 요청된 경우 `/ex00foo`는 404 오류를 반환해야 합니다.
-   요청된 URL은 슬래시를 포함하거나 포함하지 않고 작동해야 합니다. 따라서 `/ex00`이 요청된 경우 `/ex00`과 `/ex00/`가 모두 작동해야 합니다.

## Ex 00

> 예제 0: 첫 정적 페이지
>
> `ex00` 폴더 안에 `requirements.txt`, 프로젝트와 애플리케이션의 파일과 폴더들
>
> 장고의 모든 기능 허용

이 예제에서는, 장고로 첫 번째 정적 페이지를 만들게 될 것입니다.

`python3`로 `virtualenv`를 생성하고, `Django`를 설치하고, 프로젝트의 의존성이 담긴 `requirements.txt` 를 레포의 루트에 생성하세요.

`d05` 프로젝트를 시작하세요.

`ex00` 애플리케이션을 시작하세요.

`/ex00` URL에서 찾을 수 있는 페이지를 만듭니다. 이 페이지에서 전체 마크다운 구문에 대한 모든 정보를 수집하고 이 페이지의 제목을 "Ex00: Markdown Cheatsheet."로 지정합니다.

사용되는 템플릿의 이름은 `index.html` 입니다.

## Ex 01

> 예제 1: 조금 더 많은 페이지
>
> `ex01` 폴더 안에 `requirements.txt`, 프로젝트와 애플리케이션의 파일과 폴더들
>
> 장고의 모든 기능 허용

두 번째 애플리케이션 `ex01`에 아래의 페이지들을 만드세요:

-   제목: "Ex01: Django, framework web."
    URL: `/ex01/django`
    설명: 이 페이지에서는 장고와 그 역사에 대해 간략하게 설명합니다.
-   제목: "Ex01: Display process of a static page."
    URL: `/ex01/display`
    설명: 이 페이지에서는 간단한 템플릿에서 뷰를 거쳐 요청으로 부터 응답까지, 정적 웹페이지가 표시되는 과정을 설명합니다.
-   제목: "Ex01: Template engine."
    URL: `/ex01/templates`
    설명: 이 페이지에서는 장고의 기본 템플릿 엔진에 대한 기능을 설명합니다. (블록, `for ... in` 루프, `if` 제어 구문, 전달되는 컨텍스트 변수 표시)

**_don't repeat yourself_** 원칙은 장고의 설계 철학 중 일부입니다. 이 원칙을 존중하기 위해서, `base.html`이라는 기본 템플릿을 사용하여 필요한 페이지를 만듭니다.

`base.html`은 반드시 다음을 포함합니다:

-   `body` 안 `content` 블록
-   `head` 안 `style` 블록
-   `head` 안 `title` 블록

또한 각 연습 페이지의 링크를 나열하는 내비게이션 바가 포함된 `nav.html` 템플릿을 생성합니다.

이 연습의 모든 페이지는 `base.html` 템플릿을 기반으로 해야 합니다. `nav.html` 템플릿은 각 페이지에 포함되어야 합니다.

또한 `style1.css` 및 `style2.css` 파일 2개를 생성합니다. 첫 번째 파일은 텍스트 색상을 파란색으로 정의하고 다른 하나는 루즈색으로 정의합니다. `style2.css`를 사용하는 "템플릿 엔진" 페이지를 제외한 모든 페이지에서 `style1.css`를 사용해야 합니다.

> 이 예제를 위해 모든 템플릿에서 각 스타일 시트를 한 번만 사용해야 합니다.

> 평가 중에 `collectstatic` 을 사용할 것입니다.

## Ex 02

> 예제 2: 첫 폼
>
> `ex02` 폴더 안에 `requirements.txt`, 프로젝트와 애플리케이션의 파일과 폴더들
>
> 장고의 모든 기능 허용

`ex02` 애플리케이션 안에 `/ex02` URL을 통해 접근 가능한 페이지를 만드세요.

이 페이지는 2개의 파트를 포함합니다:

-   텍스트 필드와 `Submit` 버튼이 있는 폼
-   입력 기록을 포함하는 파트

폼과 관련된 규칙은 다음과 같습니다:

-   폼의 필드를 하드 코딩해서는 안 됩니다. 장고에서 제공하는 `django.forms.Form` 클래스를 사용하여 폼을 만듭니다. 템플릿의 렌더 함수에 컨텍스트로 전달합니다.

입력 기록을 위한 규칙은 다음과 같습니다:

-   입력 기록은 빈 상태로 시작합니다.
-   폼에서의 각 텍스트 제출마다
    -   로그 파일 끝에 입력 내용과 해당 타임스탬프를 나열합니다. 파일이 없는 경우 자동으로 만들어야 합니다. 이 파일은 폴더 또는 `ex02` 애플리케이션에 만들어야 합니다.
    -   제출 시간 및 날짜와 함께 페이지의 기록에 입력을 추가합니다.
-   로그 파일의 경로(파일 이름 포함)는 프로젝트의 `settings.py` 에 정의되어 있어야 합니다. 따라서 제출된 각 항목은 `log` 파일에, 타임스탬프와 페이지의 기록이 포함될 것입니다.
-   데이터는 반드시 영구적이여야 합니다. 만약 개발 서버가 재시작되는 경우에도, 데이터를 잃어서는 안됩니다. 일반적으로 페이지를 다시 표시하면, 데이터가 저장되어 있는 한 데이터가 다시 표시됩니다.

## Ex 03

> 예제 3: bic 의 50가지 그림자
>
> `ex03` 폴더 안에 `requirements.txt`, 프로젝트와 애플리케이션의 파일과 폴더들
>
> 장고의 모든 기능 허용

마지막 애플리케이션인 `ex03`을 생성하세요.

4열 x 51줄 표가 포함된 페이지를 표시합니다(한 줄은 열 이름 전용으로 사용됨).

이 페이지를 `/ex03` URL로 접근하게 될 것 입니다.

각 표의 열은 각기 다른 색을 가집니다: 느와르, 루즈, 블루, 버트

표 상자 (역: 한 칸 말하는 듯?)는 다음 스펙을 만족해야 합니다.

-   높이: 40픽셀
-   너비: 80픽셀
-   배경 색: 열과 일치하는 색조
    표는 50줄 음영을 얻기 위해 각 색상의 음영을 표시해야 합니다.

다음 지침을 준수해야 합니다:

-   템플릿에 하드 색상이 포함되어서는 안 됩니다. 뷰에서 서로 다른 음영을 생성해야 하며 모두 달라야 합니다.
-   템플릿에는 총 4개의 태그 커플 `<td></td>`이 허용됩니다.
-   템플릿에서 총 4개의 태그 커플 `<th></th>`이 허용됩니다.
-   테이블의 형식은 다음과 같이 지정해야 합니다:
    -   열 이름에 대해 상자당 `<th></th>` 태그 커플.
    -   색상 음영선마다 태그 커플 `<tr></tr>`.
    -   색상 음영 상자당 `<td></td>` 태그 커플.
