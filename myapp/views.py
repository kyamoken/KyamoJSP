from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'myapp/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'myapp/student_create.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'myapp/student_update.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'myapp/student_delete.html', {'student': student})

def student_update_page(request):
    students = Student.objects.all()
    return render(request, 'myapp/student_update_page.html', {'students': students})

def student_delete_page(request):
    students = Student.objects.all()
    return render(request, 'myapp/student_delete_page.html', {'students': students})

def redirect_to_students(request):
    return redirect('student_list')
