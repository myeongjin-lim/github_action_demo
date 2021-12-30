# Github Actions 다루기
## Github Actions이란?
Github 에서 제공하는 워크플로우(workflow)를 자동화하도록 도와주는 도구(테스트, 빌드, 배포 등)

## 요금과 제한
public 저장소 : 무료로 사용 가능
private 저장소 : 무료 계정 기준으로 매월 500MB의 스토리지와 2,000분의 실행시간이 제공

## Github Actions 생성
repository를 생성한 후 `.github/workflows` 폴더를 생성 후 `.yml`를 추가할 수 있고 Github에서 제공되는 workflow 템플릿을 제공받아 생성할 수 있다.

## Github Actions 구성
### 1.워크플로우
1.1 저장소에 추가하는 자동화된 프로세스<br>
1.2 하나 이상의 `job`으로 이루어져 있으며 이벤트에 의해 실행
      
### 2.이벤트
2.1 워크 플로우를 실행하는 특정 활동이나 규칙<br>
2.2 내부에서 발생되는 활동으로 인한 동작: push, pull request, 이외 [다양한 이벤트 참고](https://meetup.toast.com/posts/286)
```
# push나 pull  request가 발생할 때 워크 플로우 실행
on: [push, pull_request]
```   

2.3 외부에서 발생되는 활동으로 인한 동작: [저장소 dispatch event](https://docs.github.com/en/rest/reference/repos#create-a-repository-dispatch-event)
2.4 schedule을 활용한 동작
```
on:
  schedule:
    - cron : '* * * * *'
```
### cron 생성 참고 사이트
- [Cronttab Maker](http://www.cronmaker.com/?1)
- [Crontab Guru](https://crontab.guru/)

### 3.runners
3.1 Github Action Runner Application이 설치된 서버로 Github에서 호스팅하는 runner를 사용하거나 직접 호스팅할 수 있음<br>
3.2 호스팅 runner 종류: Ubuntu Linux, Windows, macOS

### 4.jobs
4.1 워크 플로우의 기본 실행 단위<br>
4.2 기본적으로 여러 작업을 병렬적으로 실행하며 순차적으로 실행하도록 설정할 수 있음<br>
ex) 빌드와 테스트 코드의 수행인 두 작업을 순차적으로 실행할 수 있으며 이런 경우는 선행작업이 실패하면 이후 작업도 실행되지 않음

### 5.steps
5.1 jobs에서 커맨드를 실행하는 독립적인 단위<br>
5.2 한 jobs의 각 steps는 동일한 runner에서 실행되므로 해당 작업의 actions는 서로 데이터를 공유한다.

### 6.actions
워크 플로우의 가장 작은 요소로 직접 만들어 사용할 수 있고 마켓에 등록된 요소를 가져와 사용할 수 있다.

## ○ 참고문서
[Github Actions으로 배포 자동화하기](https://meetup.toast.com/posts/286)<br>
[Github profile 예쁘게 꾸미기](https://velog.io/@woo0_hooo/Github-github-profile-%EA%B0%84%EC%A7%80%EB%82%98%EA%B2%8C-%EA%BE%B8%EB%AF%B8%EA%B8%B0)
