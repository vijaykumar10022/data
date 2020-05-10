from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pickle
# Create your views here.
def predict(request):
	if request.method=='POST':
		int_features=[int(request.POST['Temperature']),int(request.POST['Oxygen']),int(request.POST['Humidity'])]
		final=[np.array(int_features)]
		print(int_features)
		print(final)
		model=pickle.load(open("C:/Users/Admin/Desktop/Django_Practice/Tot-Corona/heroku_demo/demo/myfile.pkl",'rb'))
		prediction=model.predict_proba(final)
		output='{0:.{1}f}'.format(prediction[0][1], 2)
		if output>str(0.5):
			pred='Your Forest is in Danger. Probability of fire occuring is {} % '.format(output)
			bhai="be safe peoples you have to do somthing?"
			return render(request,'demo/result.html',{'pred':pred,'bhai':bhai})
		else:
			pred='Your Forest is safe. Probability of fire occuring is {} % '.format(output)
			bhai="Your Forest is Safe for now"
			return render(request,'demo/result.html',{'pred':pred,'bhai':bhai})
	return render(request,'demo/demo.html')