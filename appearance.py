
tests = [
   {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
    'answer': 3117
    },
   {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
   {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

def appearance(intervals):
    for item in intervals:

        answer_id = item['answer']
        lesson_list = item['data']['lesson']
        pupil_list = item['data']['pupil']
        tutor_list = item['data']['tutor']

        lesson_diff_list = []
        pupil_diff_list = []
        tutor_diff_list = []

        for x, y in zip(lesson_list[0::2], lesson_list[1::2]):
            lesson_diff_list.append(y-x)

        for x, y in zip(pupil_list[0::2], pupil_list[1::2]):
            pupil_diff_list.append(y-x)

        for x, y in zip(tutor_list[0::2], tutor_list[1::2]):
            tutor_diff_list.append(y-x)
        
        sum_time_lesson = 0
        for i in lesson_diff_list:
            sum_time_lesson += i

        sum_time_pupil = 0
        for i in pupil_diff_list:
            sum_time_pupil += i
        
        sum_time_tutor = 0
        for i in tutor_diff_list:
            sum_time_tutor += i

        print('ID: ', answer_id)
        print('Продолжительность урока: ', sum_time_lesson, 'секунд.')
        print('Ученик провел времени на уроке: ', sum_time_pupil, 'секунд.')
        print('Учитель провел времени на уроке: ', sum_time_tutor, 'секунд.\n')

appearance(tests)