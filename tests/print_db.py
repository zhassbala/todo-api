import api.scripts
from api.api_app.models import Task

if __name__ == '__main__':
    print("Hello. This is a script for checking database objects of Task model")
    count = 1
    for i in Task.objects.all():
        print(f'{count}.{i}')
        count += 1
