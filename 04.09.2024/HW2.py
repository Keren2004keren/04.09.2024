# START
# IF-ELIF-ELSE
grade: int = int(input("what grade did you get?: "))
if 0 <= grade <= 40:
    print("try harder next time")
elif 41 <= grade <= 60:
    print("you're getting there, need some more work")
elif 61 <= grade <= 80:
    print("pretty good")
elif 81 <= grade <= 95:
    print("awesome")
elif 96 <= grade <= 100:
    print("excellent!! you're a star")
else:
    print("illegal grade!")
# STOP

# START
# MATCH CASE
grade: int = int(input("what grade did you get?: "))
match grade:
    case grade if 0 <= grade <= 40:
        print("try harder next time")
    case grade if 41 <= grade <= 60:
        print("you're getting there, need some more work")
    case grade if 61 <= grade <= 80:
        print("pretty good")
    case grade if 81 <= grade <= 95:
        print("awesome")
    case grade if 96 <= grade <= 100:
        print("excellent!! you're a star")
    case _:
        print("illegal grade")

# STOP
