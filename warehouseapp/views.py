from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cell, User  # Используем вашу модель User

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Проверяем, существует ли пользователь с данным email и паролем
        try:
            user = User.objects.get(email=email)
            if user.password == password:  # Простая проверка пароля (рекомендуется использовать хеширование)
                request.session['user_id'] = user.id  # Сохраняем ID пользователя в сессии
                return redirect('profile')
            else:
                messages.error(request, 'Неверный логин или пароль.')
        except User.DoesNotExist:
            messages.error(request, 'Неверный логин или пароль.')
    
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        
        # Создаем нового пользователя
        User.objects.create(name=name, email=email, password=password)
        messages.success(request, 'Регистрация прошла успешно. Теперь вы можете войти в систему.')
        return redirect('login')
    
    return render(request, 'register.html')

def profile_view(request):
    if 'user_id' not in request.session:
        return redirect('login')

    user = User.objects.get(id=request.session['user_id'])
    cells = user.cells.all()  # Получаем все ячейки пользователя

    # Создаем список для передачи в шаблон
    cells_with_items = []
    for cell in cells:
        items = cell.cell_items.all()  # Получаем все предметы в ячейке
        cells_with_items.append({'cell': cell, 'items': items})

    return render(request, 'profile.html', {'cells_with_items': cells_with_items})

def logout_view(request):
    try:
        del request.session['user_id']  # Удаляем ID пользователя из сессии
    except KeyError:
        pass
    return redirect('login')

def home(request):
    return render(request, 'home.html')