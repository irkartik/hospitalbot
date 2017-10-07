# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
# def binarySearch (arr, l, r, x):
 
#     if r >= l:
 
#         mid = l + (r - l)/2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binarySearch(arr, l, mid-1, x)
#         else:
#             return binarySearch(arr, mid+1, r, x)
#     else:
#         return -1

# result = binarySearch(arr, 0, len(arr)-1, x)
 
# if result != -1:
#     print("Element is present at index %d" % result)
# else:
#     print("Element is not present in array")

class Hospital():
	def __init__(self, name, address, city, county, state, pin, website, telephone, latitude, longitude, source):
		self.name = name
		self.address = address
		self.city = city
		self.county = county
		self.state = state
		self.pin = pin
		self.telephone = telephone
		self.website = website
		self.latitude = latitude
		self.longitude = longitude
		self.source = source 

def home(request):
	context = {

	}
	return render(request, 'home.html', context)

def searchbycity(request):
	file = open('hospitaldata.json').read()

	jsonfile = json.loads(file)

	city = request.POST.get('city')
	hospital_list = list()

	for item in jsonfile:
		if city.lower() == item['City'].lower():
			name = item['Name']
			address = item['Address']
			city = item['City']
			county = item['County']
			state = item['State']
			pin = item['ZIP']
			telephone = item['Telephone']
			website = item['Website']
			latitude = item['Latitude']
			longitude = item['Longitude']
			source = item['Source']

			hospital = Hospital(name, address, city, county, state, pin, telephone, website, latitude, longitude, source)
			hospital_list.append(hospital)

	context = {
		'hospital_list': hospital_list,
	}

	return render(request, 'page.html', context)

def searchbyname(request):
	file = open('hospitaldata.json').read()

	jsonfile = json.loads(file)

	name = request.POST.get('name')
	hospital_list = list()

	for item in jsonfile:
		if name.lower() == item['Name'].lower():
			name = item['Name']
			address = item['Address']
			city = item['City']
			county = item['County']
			state = item['State']
			pin = item['ZIP']
			telephone = item['Telephone']
			website = item['Website']
			latitude = item['Latitude']
			longitude = item['Longitude']
			source = item['Source']

			hospital = Hospital(name, address, city, county, state, pin, telephone, website, latitude, longitude, source)
			hospital_list.append(hospital)

	context = {
		'hospital_list': hospital_list,
	}

	return render(request, 'page.html', context)