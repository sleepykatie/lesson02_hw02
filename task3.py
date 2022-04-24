tutors = ['Иван', 'Анастасия', 'Петр',
          'Сергей', 'Дмитрий', 'Борис', 'Елена',
          #'Алиса', 'Анна', 'Антон', 'Глеб'
          ]
school_classes = ['9А', '7В', '9Б', '9В',
                  '8Б', '10А', '10Б', '9А']


def class_teacher(names_of_tutors, classes_names):

    # print(len(names_of_tutors), len(classes_names))
    for i in range(len(names_of_tutors)):
        if i < len(classes_names):
            #print(f'{i} <= {len(classes_names)}')
            yield names_of_tutors[i], classes_names[i]
        else:
            #print(f'{i} > {len(classes_names)-1}')
            yield names_of_tutors[i], None


if __name__ == '__main__':

    teachers_gen = class_teacher(tutors, school_classes)
    for i in range(len(tutors)):
        print(next(teachers_gen))
