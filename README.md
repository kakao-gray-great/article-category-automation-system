# :newspaper: 기사 카테고리 자동화 시스템

## :pushpin: 프로젝트 소개
카테고리 별 기사를 크롤링하여 학습 한 뒤, 이후 새로운 기사 데이터가 어떤 카테고리인지 판별하는 프로그램이다.


Docker, Postman, Rabbitmq와 같은 기술을 공부하고 다양한 기술을 접목해보기 위해 시작하였다.

## :clipboard: 프로젝트 시나리오
1. NodeJS를 사용하여 기사를 id, category, content, title로 크롤링 한 후 Docker위에 띄워진 RabbitMQ에 넣는다.
2. RabbitMQ에 있는 기사 message Queue를 Spring Boot를 사용하여 PostgreSQL 데이터베이스에 넣는다.
3. PostgreSQL에서 데이터를 .csv 파일 형태로 저장한다.
4. content와 encodeing된 category를 TfidfVectorizer, MultinomialNB를 사용하여 전처리한다.
5. 전처리 된 모델을 학습한다.
6. API를 만들고 기사가 요청될 때 카테고리를 출력해준다.

## :books: 기술 스택
- <b>CRAWLING</b>: NodeJs
- <b>DATA-PROCESSING</b>: Spring-Boot
- <b>DATABASE</b>: PostgreSQL
- <b>MACHIN-LEARNING</b>: Python(Scikitlearn)
- <b>ETC</b>: Postman, Docker, RabbitMQ, Github 

## :computer: 시나리오 VIEW

### 기사 크롤링
![](https://i.imgur.com/7X9u9HP.png)

![](https://i.imgur.com/xWO5UHl.png)

### DB에 데이터 삽입
![](https://i.imgur.com/2kAYzUY.png)

![](https://i.imgur.com/CEGW1OC.png)

### 카테고리 자동화 확인
![](https://i.imgur.com/Tk8U23I.png)

![](https://i.imgur.com/w5KIBSf.png)

