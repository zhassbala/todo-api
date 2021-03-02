import api.scripts
from api.api_app.models import Task
import random, string


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


if __name__ == '__main__':
    for i in range(random.randint(1000, 10000)):
        model = Task(title=randomword(100), completed=bool(random.randint(0, 1)))
        model.save()
    print("everything is done successfully!")
