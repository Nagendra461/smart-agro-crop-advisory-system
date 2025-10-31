from django.shortcuts import render
from django.http import HttpResponse
from .ml_model import predict_crop

def home(request):
    return render(request, 'Home_1.html')


def index(request):
    if request.method == 'POST':
        try:
            try:
                nitrogen = int(request.POST.get('Nitrogen'))
            except ValueError:
                raise ValueError("Nitrogen must be an integer between 0 and 100.")

            try:
                phosphorus = int(request.POST.get('Phosphorus'))
            except ValueError:
                raise ValueError("Phosphorus must be an integer between 0 and 100.")

            try:
                potassium = int(request.POST.get('Potassium'))
            except ValueError:
                raise ValueError("Potassium must be an integer between 0 and 100.")

            try:
                temperature = float(request.POST.get('Temperature'))
            except ValueError:
                raise ValueError("Temperature must be a number between 0 and 60.")

            try:
                humidity = float(request.POST.get('Humidity'))
            except ValueError:
                raise ValueError("Humidity must be a number between 0 and 100.")

            try:
                ph = float(request.POST.get('ph'))
            except ValueError:
                raise ValueError("pH must be a number between 0 and 14.")

            try:
                rainfall = float(request.POST.get('Rainfall'))
            except ValueError:
                raise ValueError("Rainfall must be a number between 0 and 10000.")

            # Now do limits validation
            if not (0 <= nitrogen <= 100):
                raise ValueError("Nitrogen should be between 0 and 100.")
            if not (0 <= phosphorus <= 100):
                raise ValueError("Phosphorus should be between 0 and 100.")
            if not (0 <= potassium <= 100):
                raise ValueError("Potassium should be between 0 and 100.")
            if not (0 <= temperature <= 60):
                raise ValueError("Temperature should be between 0 and 60 °C.")
            if not (0 <= humidity <= 100):
                raise ValueError("Humidity should be between 0 and 100%.")
            if not (0 <= ph <= 14):
                raise ValueError("pH should be between 0 and 14.")
            if not (0 <= rainfall <= 10000):
                raise ValueError("Rainfall should be between 0 and 10000 mm.")

            # Prediction
            prediction = predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)

            return render(request, 'prediction.html', {'prediction': prediction})

        except (TypeError, ValueError) as e:
            error_message = str(e)
            context = {
                'error_message': error_message,
                'nitrogen': request.POST.get('Nitrogen', ''),
                'phosphorus': request.POST.get('Phosphorus', ''),
                'potassium': request.POST.get('Potassium', ''),
                'temperature': request.POST.get('Temperature', ''),
                'humidity': request.POST.get('Humidity', ''),
                'ph': request.POST.get('ph', ''),
                'rainfall': request.POST.get('Rainfall', ''),
            }
            return render(request, 'error.html', context)


    return render(request, 'Index.html')


# from django.shortcuts import render
# from .ml_model import predict_crop
# from django.http import HttpResponse

# def home(request):
#     return render(request, 'Home_1.html')


# def index(request):
#     if request.method == 'POST':
#         # Extract form data from POST request
#         try:
#             nitrogen = int(request.POST.get('nitrogen'))
#             phosphorus = int(request.POST.get('phosphorus'))
#             potassium = int(request.POST.get('potassium'))
#             temperature = float(request.POST.get('temperature'))
#             humidity = float(request.POST.get('humidity'))
#             ph = float(request.POST.get('ph'))
#             rainfall = float(request.POST.get('rainfall'))
#         except (TypeError, ValueError):
#             return HttpResponse("Invalid input. Please enter valid numbers.")

#         # Call prediction function
#         prediction = predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)

#         # Render prediction.html with result
#         return render(request, 'prediction.html', {'prediction': prediction})

#     # Render the form if GET request
#     return render(request, 'Index.html')
