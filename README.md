# 똑똑한 중고차

똑똑한개발자 코딩테스트로 중고차 정보를 입력받는 api입니다.


## 개발 및 실행 환경

본 API는 아래의 환경에서 개발되었습니다.
- Ubuntu 18.04.4 LTS
- python 3.6.8
- pip 20.2.4
- Django 3.1.3
- Django Rest Framework 3.12.2

1.  pip (버전 확인 방법: ``$ pip --version``)
2. 라이브러리 (설치 방법: ``$ pip install -r requirements.txt``)

## 실행 방법
- 소스코드 저장
   - ``$ git clone https://github.com/jae0077/usedcar.git``
- 변경내용 저장 및 테이블 적용
   - ``$ python manage.py makemigrations``
   - ``$ python manage.py migrate``
- 서버 실행
   - ``$ python manage.py runserver port``

## API 명세서
https://documenter.getpostman.com/view/9871305/TVeqe7Zz

## 질문
1. 임시저장 기능을 어떠한 방법으로 구현하는지 궁금합니다.
	제가 생각한 방법은 아래의 세가지입니다.

	1. 브라우저에서 로컬스토리지에 저장하는 방법
	2. 차량 정보가 등록되는 테이블에 BooleanField를 추가하여 True일때 정상등록 False일때 임시저장으로 구분 하는 방법
	3. 차량 정보가 등록되는 테이블과 임시저장 테이블을 따로 만드는 방법

	첫번째 방법의 경우 프론트부분을 요구사항에 맞게 구현 할 수 없어 적용하지 못했습니다.
	
	두번째 방법의 경우 임시저장이기 때문에 모든 필드가 null이나 blank가 허용 되어야 하는데 하나의 테이블이기 때문에 정상등록일때도 null과 blank가 허용된다는 문제점이 있었습니다.
	
	세번째 방법의 경우 임시저장 테이블에 값이 있을때 새로운 중고차를 추가할 수 있게 처리하는 방법을 찾지 못해 구현 하지 못했습니다.

2. A(id=1)와 B(id=2) 라는 계정이 존재한다는 가정하에 차량정보 등록 api에서 헤더값에 A의 토큰을 넣고 formdata 중 user를 2로 줄 경우 B의 계정으로 등록을 할 수 있었습니다.
인증에 관한 부분을 제대로 구현하지 못해 발생한 문제로 생각되는데 어떤 방법을 사용해야 하는지 궁금합니다.
	제가 생각한 방법은 로그인시 브라우저에 토큰값과 id를 저장하고 차량정보를 등록할때 id를 받아오는 방법을 떠올렸으나 프론트를 구현하지 못해 적용해 보지 못했습니다.
