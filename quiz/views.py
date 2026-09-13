from django.shortcuts import render, redirect
from django.contrib import messages
from attend.models import  Attend
from  .models import Quiz


def quiz(request):

    if request.method == 'POST':

        obj = Quiz()

        obj.question = request.POST.get('question')
        obj.option1 = request.POST.get('option1')
        obj.option2 = request.POST.get('option2')
        obj.option3 = request.POST.get('option3')
        obj.option4 = request.POST.get('option4')
        obj.correct_answer = request.POST.get('correct_answer')

        obj.save()

        messages.success(request, "Question Added Successfully")

        return redirect('/quiz/add/')

    return render(request, 'quiz/quiz.html')



def attend_quiz(request):

    questions = Quiz.objects.all()

    if request.method == "POST":

        register_id = request.session.get('u_id')

        if not register_id:
            messages.error(request, "User session not found")
            return redirect('/login/login/')

        score = 0
        total = questions.count()

        # Remove previous attempts if needed
        Attend.objects.filter(register_id=register_id).delete()

        for question in questions:

            selected_option = request.POST.get(
                f"q_{question.quiz_id}"
            )

            if selected_option:

                Attend.objects.create(
                    quiz_id=question.quiz_id,
                    register_id=register_id,
                    option=selected_option
                )

                if selected_option == question.correct_answer:
                    score += 1

        request.session['score'] = score
        request.session['total'] = total

        return redirect('/quiz/result/')

    return render(
        request,
        'quiz/attend.html',
        {
            'questions': questions
        }
    )


def quiz_result(request):

    score = request.session.get('score', 0)
    total = request.session.get('total', 0)

    percentage = 0

    if total > 0:
        percentage = round((score / total) * 100)

    wrong = total - score

    register_id = request.session.get('rid')

    results = []

    if register_id:

        attends = Attend.objects.filter(
            register_id=register_id
        )

        for attend in attends:

            try:

                question = Quiz.objects.get(
                    quiz_id=attend.quiz_id
                )

                results.append({
                    'question': question.question,
                    'user_answer': attend.option,
                    'correct_answer': question.correct_answer,
                    'is_correct':
                        attend.option == question.correct_answer
                })

            except Quiz.DoesNotExist:
                pass

    context = {
        'score': score,
        'total': total,
        'wrong': wrong,
        'percentage': percentage,
        'results': results
    }

    return render(
        request,
        'quiz/result.html',
        context
    )



from collections import defaultdict
def view_participants(request):

    participants = defaultdict(lambda: {
        'name': '',
        'score': 0,
        'total': 0
    })

    attends = Attend.objects.select_related('register')

    for a in attends:

        try:
            quiz = Quiz.objects.get(quiz_id=a.quiz_id)

            participants[a.register.register_id]['name'] = a.register.username
            participants[a.register.register_id]['total'] += 1

            if a.option == quiz.correct_answer:
                participants[a.register.register_id]['score'] += 1

        except Quiz.DoesNotExist:
            pass

    data = participants.values()

    return render(request, 'quiz/view_participants.html', {'data': data})



from django.shortcuts import render, redirect
from .models import Quiz


def view_quiz(request):
    data = Quiz.objects.all()
    return render(request, 'quiz/view_quiz.html', {'data': data})


def edit_quiz(request, id):
    obj = Quiz.objects.get(quiz_id=id)

    if request.method == 'POST':
        obj.question = request.POST.get('question')
        obj.option1 = request.POST.get('option1')
        obj.option2 = request.POST.get('option2')
        obj.option3 = request.POST.get('option3')
        obj.option4 = request.POST.get('option4')
        obj.correct_answer = request.POST.get('correct_answer')
        obj.save()

        return redirect('/quiz/view_quiz/')

    return render(request, 'quiz/edit_quiz.html', {'i': obj})