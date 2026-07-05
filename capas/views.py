from django.shortcuts import render

def capa_dashboard(request):
    active_capas = CapaAction.objects.filter(is_active=True).count()
    context = {'active_capas': active_capas}
    return render(request, 'capas/dashboard.html', context)