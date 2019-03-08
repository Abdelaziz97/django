from django.shortcuts import render

projects = [
    {
        'name': 'Apollo11',
        'duration': '3 years',
        'startDate': '2019/05/01',
        'endDate': '2022/05/01',
        'client': [
            {
                'lastName': 'Omari',
                'firstName': 'Abdelaziz',
                'phoneNumber': '0661603019',
                'firm': 'Aelo'
            }
        ],
        'task': [
            {
                'abstract': 'Create class position',
                'duration': '5 hours',
                'startTime': '14:15',
                'endTime': '19:15'
            }
        ]
    }
]

def home(request):
    context = {
        'projects': projects
    }
    return render(request, 'blog/home.html', context)

def client(request):
    return render(request, 'blog/client.html')

def user(request):
    return render(request, 'blog/user.html')
