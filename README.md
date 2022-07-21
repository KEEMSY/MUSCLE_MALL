# DRF-PROJECT: Muscle Mall
### DRF의 Serializer, Permission을 연습하고 CBV를 사용한 API 작성, TDD 및 CI & CD를 공부하는 프로젝트 입니다. 
<hr>

## 소개
`MM Project` 은 내게 맞는 운동, 식단, 영양 루틴을 구성하거나, 각 분야(운동, 식단, 영양)의 코치들의 루틴을 참고하거나 해당 코치의 지도를 받을 수 있는 서비스 입니다. 


<hr>

## 기술 스택
 <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=yellow"> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/Mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
 <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
 <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white">
  <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white">


<hr>

## 주요기능
### `userapp`
`admin`
- User 등록을 통한 User 관리
- Coach 등록을 통한 Coach 관리
<br>

`permission`
- IsAuthenticatedAndIsAprovedUser 을 통한 권한 설정
- IsAuthenticatedrIsAdmin를 통한 권한 설정
<br>

`user`
- 회원가입
- 회원 승인
- 회원정보 수정
- 회원탈퇴
- (개인)유저조회
<br>

`coach`
- 코치등록
- 코치승인
- 코치정보 수정
- (개인)코치정보 조회

<hr>

### `productapp`
`permission`
- IsAdminOrReadOnly 을 통한 권한 설정
<br>

`ProductCategory`
- 대 분류 카테고리 생성, 조회, 수정, 삭제
- ProductCategorySerializer를 통한 직렬화 

<br>

`ProductDetailCategory`
- 소 분류 카테고리 생성, 조회, 수정, 삭제
- ProductDetailCategorySerializer를 통한 직렬화

<br>

`Product`
- ProductCategory / ProductDetailCategory 에 속하는 product의 생성, 조회, 수정, 삭제
- ProductSerializer를 통한 직렬화
<br>

`Routine`
- IsAuthenticatedOrReadOnly를 통한 권한 설정
- 원하는 Product 를 담아 Routine 생성, 조회, 수정, 삭제
- RoutineSerializer를 통한 직렬화
<br>

`Challenge`
- 원하는 Product로 구성된 Routine을 통한 Challenge 생성, 조회, 수정, 삭제
- ChallengeSerializer를 통한 직렬화

<br>

<hr>

<div align=center>
    <p>
     <a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FKEEMSY%2FMUSCLE_MALL%2F&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/>
     </a>
    </p>
</div>
