from django.shortcuts import render, redirect
from credential.models import Credential

def add_credential(request):

    if request.method == "POST":

        email = request.POST.get('email')
        breach_source = request.POST.get('breach_source')
        breach_date = request.POST.get('breach_date')

        Credential.objects.create(
            email=email,
            breach_source=breach_source,
            breach_date=breach_date
        )

        # return redirect('/credential/view/')

    return render(request, 'datasource/datasource.html')



def check_credential(request):

    leak_status = None
    breaches = None

    if request.method == "POST":

        email = request.POST.get('email')

        breaches = Credential.objects.filter(email=email)

        if breaches.exists():
            leak_status = "Leaked"
        else:
            leak_status = "Safe"

    return render(
        request,
        'datasource/view data source.html',
        {
            'leak_status': leak_status,
            'breaches': breaches
        }
    )

from credential.models import EmailScan

from django.shortcuts import render
from credential.models import EmailScan, Credential

def organization_dashboard(request):

    # Threat Monitoring
    total_scans = EmailScan.objects.count()

    high_risk = EmailScan.objects.filter(risk="High").count()

    medium_risk = EmailScan.objects.filter(risk="Medium").count()

    low_risk = EmailScan.objects.filter(risk="Low").count()

    # Breach Statistics
    total_breaches = Credential.objects.count()

    recent_breaches = Credential.objects.order_by(
        '-breach_date'
    )[:10]

    # Preventive Actions
    actions = []

    if high_risk > 10:
        actions.append(
            "Conduct phishing awareness training."
        )

    if total_breaches > 10:
        actions.append(
            "Force password reset for affected users."
        )

    actions.append(
        "Enable Multi-Factor Authentication (MFA)."
    )

    actions.append(
        "Monitor suspicious email activity."
    )

    context = {
        "total_scans": total_scans,
        "high_risk": high_risk,
        "medium_risk": medium_risk,
        "low_risk": low_risk,
        "total_breaches": total_breaches,
        "recent_breaches": recent_breaches,
        "actions": actions,
    }

    return render(
        request,
        "datasource/threat_monitor.html",
        context
    )