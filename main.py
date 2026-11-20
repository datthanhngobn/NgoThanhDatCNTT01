def normalize_name(text: str) -> str:
    return " ".join(text.strip().split())

def average_score(scores: list) -> float:
    avg = 0
    for i in scores:
        avg += i / len(scores)
    return avg

def count_passed(scores: list, threshold: float = 5) -> int:
    passed = 0
    for i in scores:
        if i >= threshold:
            passed += 1
    return passed

def rank_students(score_by_name: dict) -> dict:
    return dict(sorted(score_by_name.items(), key=lambda student: (-student[1], student[0])))


print(f"{normalize_name("  Nguyễn   An  ")} \n{normalize_name("minh")} \n{normalize_name("   ")}")

scores = [8, 4, 9, 5]
print(average_score(scores), count_passed(scores), count_passed(scores, 8))
scores = [5]
print(average_score(scores), count_passed(scores), count_passed(scores, 8))
scores = []
print(average_score(scores), count_passed(scores), count_passed(scores, 8))


score_by_name = {"Minh": 9, "Lan": 7, "An": 9, "Vy": 5}
print(rank_students(score_by_name))
score_by_name = {}
print(rank_students(score_by_name))