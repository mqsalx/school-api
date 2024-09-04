from django.http import JsonResponse


def students(request):
    if request.method == "GET":
        student = {"name": "John Doe", "age": 20, "course": "Computer Science"}
        return JsonResponse(student)
