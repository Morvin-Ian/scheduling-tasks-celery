from celery import shared_task


@shared_task(bind=True)
def func_test(self):
    for x in range(10):
        print(x)
    return "Task Complete !!"
