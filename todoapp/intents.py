name=''
problem_name=''
problem_info=''
def get_intent(data):
    global name,problem_info,problem_name
    m = data['message'].lower()
    if data['key']=="name":
        name = m
        return "next"
    if any (x in m for x in ["diabetes","obesity","thyroid"]):
        problem_name = m
        return "problem_name"
    if any(x in m for x in ["foods_to_eat","foods_to_avoid"]):
        problem_info = m
        return "problem_info"
    if "thank" in m:
        return "end"

def handle(data):
    global name,problem_name,problem_info
    from flask import render_template
    intent = get_intent(data)
    if intent == 'problem_name':
        return render_template('messages/aboutproblem1.html',question={'key':'request','text':'Please Enter the details you want to know.'},options={'tasks':[
            {'key':'foods_to_eat','description':'to know what foods to eat'},
            {'key':'foods_to_avoid','description':'to know what foods to avoid'}

        ]})
    elif intent == "next":
        return render_template('messages/greet.html',name=name,
        question={'key' : 'request','text': 'Enter the health issue name'})
    elif intent == 'problem_info':
        from .data.info import bot
        return render_template('messages/aboutproblem2.html',problem_name=problem_name, problem_info = problem_info, data=bot ,question={'key':'request'})
    elif intent == 'end':
        return render_template('messages/botend.html',question={'key':'request'})
    else:
        return render_template('messages/echo.html',question={'key':'request'})