# load_scores — 성적 CSV 읽기 프로그램

## ① 무엇을 하나요 (What)

성적 CSV를 읽어 유효한 점수는 `kept`로, 건너뛴 줄은 이유와 함께 `skipped`로 나누어 돌려줍니다.

## ② 왜 만들었나요 (Why)

실제 성적 파일에는 빈 칸, 범위 밖 점수, 중복 이름이 섞여 있어 그냥 읽으면 프로그램이 죽거나 틀린 값이 섞입니다. 그래서 유효한 줄과 건너뛴 줄을 나누어 기록하는 함수가 필요했습니다.

## ③ 어떻게 쓰나요 (How)

```bash
# 설치 (Python 3.8 이상, 별도 설치 없음)

# 실행
python load_scores.py scores.csv
```

## ④ 어떻게 테스트하나요

```bash
pip install pytest pytest-cov
pytest
```

```
test_load_scores.py ............                                         [100%]
12 passed in 0.65s
```

## ⑤ 파일 구성

| 파일 | 하는 일 |
| --- | --- |
| `load_scores.py` | 성적 CSV를 읽어 `(kept, skipped)`를 돌려주는 함수 |
| `test_load_scores.py` | 정상 · 예외 · 경계값을 확인하는 pytest 테스트 |
| `scores.csv` · `weird.csv` · `empty.csv` | 실행과 확인에 쓰는 예시 데이터 |

## ⑥ 만든 사람 · AI를 어디에 썼는지

- 만든 사람 : 가송이 (2026101073)
- AI를 쓴 곳 : 테스트 코드 초안 작성, README 정리
- 내가 직접 판단한 것 : 어떤 경우를 시험할지(정상 · 예외 · 경계값) 정하고, 실행해서 결과를 확인함

## 라이선스

MIT License (LICENSE 파일 참고)
