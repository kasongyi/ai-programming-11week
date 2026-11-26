
import pytest
from load_scores import load_scores


# 1. 정상적인 CSV 파일을 읽는지 확인
def test_정상_파일을_읽는다():
    kept, skipped = load_scores("scores.csv")

    assert len(kept) == 5
    assert len(skipped) == 5


# 2. 같은 이름이 있어도 둘 다 남기는지 확인
def test_중복된_이름을_모두_남긴다():
    kept, skipped = load_scores("scores.csv")

    same_name = [item for item in kept if item[0] == "김하나"]

    assert len(same_name) == 2


# 3. 헤더만 있는 파일을 읽는지 확인
def test_헤더만_있으면_빈_결과를_반환한다():
    kept, skipped = load_scores("empty.csv")

    assert kept == []
    assert skipped == []


# 4. 없는 파일을 입력하면 오류가 발생하는지 확인
def test_없는_파일이면_오류가_발생한다():
    with pytest.raises(FileNotFoundError):
        load_scores("없는파일.csv")


# 5. 비정상적인 데이터가 제대로 걸러지는지 확인
def test_이상한_데이터를_걸러낸다():
    kept, skipped = load_scores("weird.csv")

    assert len(kept) == 2
    assert len(skipped) == 7


# 6. 점수의 경계값 확인
@pytest.mark.parametrize("score, expected", [
    (-1, False),
    (0, True),
    (1, True),
    (99, True),
    (100, True),
    (101, False)
])
def test_점수_경계값(score, expected, tmp_path):
    file_path = tmp_path / "test.csv"

    file_path.write_text(
        f"name,score\n학생,{score}\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(str(file_path))

    assert (len(kept) == 1) == expected


# 7. 빈 줄은 건너뛰고 기록하지 않는지 확인
def test_빈줄은_기록하지_않는다(tmp_path):
    file_path = tmp_path / "blank.csv"

    file_path.write_text(
        "name,score\n\n학생,80\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(str(file_path))

    assert kept == [("학생", 80)]
    assert skipped == []
