# algorithm-study

2021 알고리즘 스터디

## 출결표

[여기](https://docs.google.com/document/d/1aNvfxmfV1EfTn5taj55e0NNJAZxRZSOedg5M4Rh2S7s/edit?usp=sharing)
에서 확인할 수 있습니다.

## Guideline

- 각자 PC에서 git을 설치한 후에, 리모트 -> 로컬 저장소 생성  
  맥은 터미널에서 진행하면 되고, 윈도우는 아마 git bash에서 진행하면 되는 걸로 알고 있습니다.

```bash
git clone https://github.com/AMYMEME/algorithm-study.git
```

- 각자 브랜치 생성  
  위에서 생성한 로컬 저장소 위치에서 명령어를 이용해 브랜치를 설정할 수 있습니다.  
  초기 브랜치는 `main`으로 설정되어 있을텐데, 브랜치 새로 생성 및 교체 명령어는 `git checkout -b {브랜치명}`입니다.
  이후에 `main`에서 자기가 설정한 브랜치명으로 바뀌었는지 확인하시고 진행해주세요.

- 모든 문제는 빌드가 꼬이지 않는 경우에 에디터에서 Open으로 열어서 수정 후
  터미널에서 git push 해도 되고, 단순히 터미널에서 vi로 붙여넣어도 됩니다.  
  에디터를 사용하실 경우 자동으로 생성되는 `.idea/`등 필요없는 파일들은 `.gitignore`에 추가해주세요.  
  공통 문제와 개인 문제를 모두 올려주신 이후 다른 사람이 쉽게 볼 수 있게 [깃허브 사이트](https://github.com/AMYMEME/algorithm-study/pulls)에서
  `Pull requests`이용해서 PR 띄워주세요!(`자기 브랜치` -> `main`)  
  *자바 등 빌드가 꼬이기 쉬울 경우는 프로젝트를 따로 만들어서 빌드/테스팅 하시고, 코드만 복붙하시는 걸 추천드립니다!*  
  한 주 스터디가 끝날 때마다 **각자** 브랜치를 `merge` 해주시고, `git push`가 되지 않으면 `git pull`진행 후 해보시거나,
  카톡방에 공유해주세요!

- 공통 문제는 `/common/스터디 날짜`에 올려주시면 됩니다.  
  문제를 모두 풀든 못 풀든 마감시간 전에 깃 리모트 저장소에 올려주시면 됩니다.  
  파일명은 **깃헙 닉네임**으로 해주세요! (ex: `/common/2020.01.06/amymeme.py`)  
  `git status`로 생성/수정된 파일 확인 후, `git add 파일명`, `git commit -m "{커밋 메시지}"`를 모두 진행하신 후에,
  `git push origin {자기 브랜치명}`으로 올려주시면 됩니다.

- 개인(선택) 문제는 루트 하위에 폴더를 새로 생성후 올려주시면 됩니다.(ex : `/amymeme`)  
  위 처럼 `git push` 진행하시면 됩니다.  
  폴더명은 자유이고, 날짜별 폴더를 만들거나 파일 이름을 날짜별로 해주시면 감사하겠습니다. (ex : `20210106.java`, `20200106.py`...)  
  코드 뿐만 아니라 관련 개념 정리나 푸는 과정에서 든 생각들을 기록하셔도 상관없습니다 :)

## 문제목록

날짜|문제
---|-------
`2021.01.06`| [백준 #9012](https://www.acmicpc.net/problem/9012)
`2021.01.14`| [백준 #15686](https://www.acmicpc.net/problem/15686), [백준 #17225](https://www.acmicpc.net/problem/17225)
`2021.01.21`| [백준 #14502](https://www.acmicpc.net/problem/14502), [백준 #11286](https://www.acmicpc.net/problem/11286)
`2021.01.28`| [백준 #16236](https://www.acmicpc.net/problem/16236), [백준 #14891](https://www.acmicpc.net/problem/14891)
`2021.02.04`| [백준 #15684](https://www.acmicpc.net./problem/15684), [백준 #17144](https://www.acmicpc.net./problem/17144)
`2021.02.17`| [백준 #2638](https://www.acmicpc.net./problem/2638), [백준 #11047](https://www.acmicpc.net./problem/11047), [백준 #14500](https://www.acmicpc.net./problem/14500)
`2021.02.24`| [백준 #11000](https://www.acmicpc.net./problem/11000), [백준 #12865](https://www.acmicpc.net./problem/12865)
`2021.03.02`| [백준 #9251](https://www.acmicpc.net./problem/9251)
`2021.03.09`| [백준 자료구조 알고리즘](https://www.acmicpc.net/problemset?sort=ac_desc&algo=175)
`2021.03.16`| [백준 #4256](https://www.acmicpc.net/problem/4256), [백준 #1916](https://www.acmicpc.net/problem/1916)
`2021.03.23`| [백준 #1339](https://www.acmicpc.net/problem/1339), [백준 #1939](https://www.acmicpc.net/problem/1939)
`2021.03.30`| [백준 #16234](https://www.acmicpc.net/problem/16234), [백준 #17822](https://www.acmicpc.net/problem/17822)
`2021.04.06`| [백준 #1030](https://www.acmicpc.net/problem/1030), [백준 #10830](https://www.acmicpc.net/problem/10830)
`2021.04.27`| [백준 #9466](https://www.acmicpc.net/problem/9466), [백준 #3055](https://www.acmicpc.net/problem/3055)
`2021.05.04`| [백준 #11559](https://www.acmicpc.net/problem/11559), [백준 #14002](https://www.acmicpc.net/problem/14002)
`2021.05.11`| [백준 #2661](https://www.acmicpc.net/problem/2661), [백준 #1806](https://www.acmicpc.net/problem/1806)
`2021.05.18`| [프로그래머스 #가장 먼 노드](https://programmers.co.kr/learn/courses/30/lessons/49189), [프로그래머스 #네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162)
`2021.05.25`| [백준 #13913](https://www.acmicpc.net/problem/13913), [백준 #17281](https://www.acmicpc.net/problem/17281)
`2021.06.29`| [백준 #2239](https://www.acmicpc.net/problem/2239), [백준 #1956](https://www.acmicpc.net/problem/1956)
