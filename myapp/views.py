from django.shortcuts import render, redirect
from .models import Food, Consume

# add selected food items to the user
def index(request):
    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed') 
        if food_consumed:  
            try:
                consume = Food.objects.get(name=food_consumed)
                user = request.user
                consume = Consume(user=user, food_consumed=consume)
                consume.save()
            except Food.DoesNotExist:
                # handle empty error
                pass

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user.id)

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})


# delete the selcted food item
def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('/')
    # use GET to show delete comfirm first
    else: 
        return render(request,'myapp/delete.html')