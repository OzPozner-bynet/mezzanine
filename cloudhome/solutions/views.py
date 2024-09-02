from django.shortcuts import render, get_object_or_404
from .models import Solution


def solution_list(request):
    solutions = Solution.objects.all()
    return render(request, 'solutions/solution_list.html', {'solutions': solutions})

def solution_detail(request, slug):
    try:
        # Try to find the solution by slug
        solution = Solution.objects.get(slug=slug)
    except Solution.DoesNotExist:
        # If not found by slug, try to find by ID
        solution = get_object_or_404(Solution, pk=slug)
    return render(request, 'solutions/solution_detail.html', {'solution': solution})
    return render(request, 'solutions/solution_detail.html', {'solution': solution})