from django.shortcuts import render, get_object_or_404, redirect

from .models import Teacher


def get_values(src_dict, *keys):
    return (src_dict[key] for key in keys)


def display_teachers(request):
    teacher_list = Teacher.objects.order_by('id')
    return render(request,
                  'school/teachers.html',
                  {'teacher_list': teacher_list})


def get_teacher_info(request, teacher_id):
    return render(request,
                  'school/teacher.html',
                  {"teacher": get_object_or_404(Teacher, pk=teacher_id)})


def add(request):
    # first_name, last_name, patronymic = (request.POST[key] for key in ['first_name', 'last_name', 'patronymic'])
    first_name, last_name, patronymic = get_values(request.POST, 'first_name', 'last_name', 'patronymic')
    if first_name and last_name and patronymic:
        new_teacher = Teacher(first_name=first_name,
                              last_name=last_name,
                              patronymic=patronymic)
        new_teacher.save()

    return redirect('school:teachers')


def delete(request, teacher_id):
    get_object_or_404(Teacher, pk=teacher_id).delete()
    return redirect('school:teachers')


def update(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    first_name, last_name, patronymic = get_values(request.GET, 'first_name', 'last_name', 'patronymic')
    if first_name and last_name and patronymic:
        teacher.last_name = last_name
        teacher.first_name = first_name
        teacher.patronymic = patronymic
        teacher.save()

    return redirect('school:teachers')
