## 개요

[점프투장고](https://wikidocs.net/book/4223)에서 제공하는 코드를 바탕으로 게시판을 제작했다.

언어는 Python, 웹 프레임워크는 Django, 템플릿 디자인에는 Bootstrap4를 사용했다.

완성된 사이트는 아래 링크를 통해 접속 가능하다.

http://3.38.13.240/



## App 구조

- `pybo`: 게시판 질문/답변/댓글/추천
  
- `common`: 회원가입/로그인/계정설정(비밀번호 변경, 초기화)/계정정보(프로필 이미지, 작성 목록)
  
  

## 실행 환경

로컬 및 서버에서 `pip`을 통해 다운로드 받은 패키지와 용도는 아래와 같다.

- python 3.8.12
- django 3.1.3
- mysqlclient : MySQL를 DBMS로 사용
- markdown : 질문/답변 출력에 마크다운 문법 적용
- pillow : 프로필에서 ImageField 사용



## 배포 환경

* AWS LightSail
* Amazon RDS(MySQL)
* Gunicorn
* Nginx



## 추가점

교재에서 코드를 제공하지 않고 제안하는 [추가 기능](https://wikidocs.net/75418)이나, 직접 기획하여 추가한 요소는 아래와 같다.

일부 새로운 기능의 개발 과정은 velog 글로 작성했으며 아래에 링크를 걸어두었다.

* [카테고리(질문 분류)](https://velog.io/@azzurri21/Django-%EC%A0%90%ED%94%84%ED%88%AC%EC%9E%A5%EA%B3%A0-%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC-%EA%B8%B0%EB%8A%A5-%EC%B6%94%EA%B0%80)
* [비밀번호 초기화](https://velog.io/@azzurri21/Django-%EC%A0%90%ED%94%84%ED%88%AC%EC%9E%A5%EA%B3%A0-%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EC%B4%88%EA%B8%B0%ED%99%94)
* [페이징 반영된 앵커 완성](https://velog.io/@azzurri21/Django-점프투장고-페이징-반영된-앵커-완성하기)
* [프로필 화면(사용자 작성 목록) 추가하기](https://velog.io/@azzurri21/Django-점프투장고-프로필-화면-추가하기)
* 프로필 이미지 등록 및 수정
  * 이미지 경로 암호화, 이미지 수정 시 media 파일 삭제
* MySQL 연동, settings.py에서 SECRET_KEY 분리

