from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template.context_processors import csrf
from registration.models import Disease, Doctor, Hospital, Pharmacy, SearchDiseaseResult, SearchSymptomRecord, UserDetails
import requests
from django.db.models import Q
from django.core import serializers
from geopy.distance import geodesic
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
# from geopy.distance import geodesic 
# from geopy.geocoders import Nominatim
# import geocoder

# from newsapi import NewsApiClient
# Create your views here.
symp=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze','itchy skin','hunger','snore','vomiting','disequilibrium','numbness','high_pressure_chest','shortness_of_breath','drowsiness','weight_gain','fatigue']

def index(request):
    return render(request,'index.html')

def doctorhome(request):
    if(request.session.get('doctor')):
        return render(request,'doctor_home.html')
    else:
        return HttpResponseRedirect('/logintosite/login/?msg=doctor login is required')

def adminhome(request):
    if(request.session.get('admin')):
        return render(request,'admin_home.html')
    else:
        if(request.session.get('doctor')):
            return render(request,'doctor_home.html',{'msg':'you can not access admin home as you are not an admin'})
        else:
            return HttpResponseRedirect('/logintosite/login/?msg=admin login is required')


def news(request):
    url = ('http://newsapi.org/v2/top-headlines?'
        'q=medical&'
        'apiKey=81606bad15824906a328e56705cc8f52')
    response = requests.get(url)
    results=response.json()['articles']
    news=[]#title
    image=[]#url for image
    desc=[]#description
    content=[]
    urls=[]
    for l in range(len(results)):
        t=results[l]
        news.append(t['title'])
        image.append(t['urlToImage'])
        desc.append(t['description'])
        content.append(t['content'])
        urls.append(t['url'])
    mylist=zip(news,desc,content,image,urls)
    return render(request,'news.html',{'mylist':mylist})
    # https://www.medicalnewstoday.com/
    # newsapi = NewsApiClient(api_key='81606bad15824906a328e56705cc8f52')
    # top_headlines = newsapi.get_top_headlines(q='bitcoin',
    #                                       sources='bbc-news,the-verge',
    #                                       category='business',
    #                                       language='en',
    #                                       country='us')
    # print(top_headlines)
    # return render(request,'home.html')
def viewdoctorprofiles(request):
    profiles=[]
    dname=request.session['doctor']
    users=UserDetails.objects.filter(IsDoctor=True)
    docs=Doctor.objects.all()
    for u in users:
        if(u.name==dname):
            print("cancel",u.name)
            continue
        else:
            print(u.name)
            for d in docs:
                if d.userID==u:
                    profiles.append(Doctor.objects.get(userID=u))
                    break
    print(profiles)
    return render(request,'viewalldoctors.html',{'profiles':profiles})
        
def getprofile(request):
    name=request.session['doctor']
    d=UserDetails.objects.get(name=name)
    docs=Doctor.objects.all()
    c={}
    c.update(csrf(request))
    found=False
    for doct in docs:
        if doct.userID==d:
            found=True
            doc=doct
            break
    hospitals=Hospital.objects.all()
    if(found):
        return render(request,'profile.html',{'doc':doc,'d':d,'c':c,'hospitals':hospitals})
    return render(request,'profile.html',{'d':d,'c':c,'notfound':True,'hospitals':hospitals})

def updateprofile(request):
    name=request.POST['name']
    email=request.POST['email']
    contactno=request.POST['contactno']
    education=request.POST['education']
    speciality=request.POST['speciality']
    changehospital=request.POST['hospital']
    hospital=request.POST['associatehospital']
    UserDetails.objects.filter(name=name).update(emailID=email)
    u=UserDetails.objects.get(name=name)
    if(changehospital=="select hospiatl"):
        h=Hospital.objects.get(name=hospital)
    else:
        h=Hospital.objects.get(name=changehospital)
    d=Doctor.objects.all()
    found=False
    for doct in d:
        if doct.userID==u:
            found=True
            doc=doct
            break
    if(found):
        Doctor.objects.filter(userID=u).update(contactno=contactno,education=education,speciality=speciality,associate_hospital=h)
    else:
        d=Doctor(contactno=contactno,education=education,speciality=speciality,userID=u,associate_hospital=h)
        d.save()
    return HttpResponseRedirect('/home/doctorhome/')

def hospitalsearch(request):
    query= request.GET.get('search','')
    print(query)
    if query != '':
        lookups = Q(location__icontains=query)
        object_list=Hospital.objects.filter(lookups)
        if (object_list):
            return render(request,'hospitalsearch.html',{'objectlist':object_list,'found':True})
        else:
            return render(request,'hospitalsearch.html',{'errmsg':"SORRY: No search result found."})
    else:
        return render(request,'hospitalsearch.html',{'errmsg':"Enter appropriate search value"})
        
def pharmacysearch(request):
    query= request.GET.get('search','')
    print(query)
    if query != '':
        lookups = Q(location__icontains=query)
        object_list=Pharmacy.objects.filter(lookups)
        if (object_list):
            return render(request,'pharmacysearch.html',{'objectlist':object_list,'found':True})
        else:
            return render(request,'pharmacysearch.html',{'errmsg':"SORRY: No search result found."})
    else:
        return render(request,'pharmacysearch.html',{'errmsg':"Enter appropriate search value"})

def gotosearch(request):
    c={}
    c.update(csrf(request))
    return render(request,'search.html',{'c':c,'l1':symp}) 

def search(request):
    c={}
    c.update(csrf(request))
    sym1=(int)(request.POST['sym1'])
    sym2=(int)(request.POST['sym2'])
    if(sym1==0 or sym2==0):
        return render(request,'search.html',{'c':c,'found':False,'l1':symp,'errmsg':'please enter atleast 2 symptoms details'})
    s1=SearchSymptomRecord.objects.filter(symptom=symp[sym1-1])
    s2=SearchSymptomRecord.objects.filter(symptom=symp[sym2-1])
    if(not s1):
        sym=SearchSymptomRecord(symptom=symp[sym1-1],searchcount=1)
        sym.save()
    else:
        sym=SearchSymptomRecord.objects.get(symptom=symp[sym1-1])
        sym.searchcount=sym.searchcount+1
        sym.save()
    if(not s2):
        sym=SearchSymptomRecord(symptom=symp[sym2-1],searchcount=1)
        sym.save()
    else:
        sym=SearchSymptomRecord.objects.get(symptom=symp[sym2-1])
        sym.searchcount=sym.searchcount+1
        sym.save()
    ds1=Disease.objects.filter(Q(Symptoms__icontains=symp[sym1-1]))
    ds2=Disease.objects.filter(Q(Symptoms__icontains=symp[sym2-1]))
    sym3=(int)(request.POST['sym3'])
    if(sym3==0):
        if(ds1 or ds2):
            q1=set(ds1)
            q2=set(ds2)
            q=set(ds1).intersection(set(ds2))
            
            if(q):
                for d in q:
                    d1=SearchDiseaseResult.objects.filter(diseasename=d)
                    if(not d1):
                        d1=SearchDiseaseResult(diseasename=d,searchcount=1)
                        d1.save()
                    else:
                        d1=SearchDiseaseResult.objects.get(diseasename=d)
                        d1.searchcount=d1.searchcount+1
                        d1.save()
                return render(request,'search.html',{'q':q,'found':True,'c':c,'l1':symp})
            else:
                for d in q1:
                    d1=SearchDiseaseResult.objects.filter(diseasename=d)
                    if(not d1):
                        d1=SearchDiseaseResult(diseasename=d,searchcount=1)
                        d1.save()
                    else:
                        d1=SearchDiseaseResult.objects.get(diseasename=d)
                        d1.searchcount=d1.searchcount+1
                        d1.save()

                for d in q2:
                    d1=SearchDiseaseResult.objects.filter(diseasename=d)
                    if(not d1):
                        d1=SearchDiseaseResult(diseasename=d,searchcount=1)
                        d1.save()
                    else:
                        d1=SearchDiseaseResult.objects.get(diseasename=d)
                        d1.searchcount=d1.searchcount+1
                        d1.save()

                return render(request,'search.html',{'q1':q1,'found':True,'c':c,'q2':q2,'l1':symp,'sug':'provide more symptoms to get perfect results if possible'})
        else:
            return render(request,'search.html',{'msg':'Sorry!!!not found any matching results..kindly request you to provide this details in FAQ. our team will give you satisfiable answer there..','found':False,'c':c,'l1':symp})
    else:
        ds3=Disease.objects.filter(Q(Symptoms__icontains=symp[sym3-1]))
        if(ds3 or ds2 or ds1):
            q3=set(ds3)
            q1=set(ds1)
            q2=set(ds2)
            q=q1.intersection(q2.intersection(q3))
            if(q):
                return render(request,'search.html',{'q':q,'found':True,'c':c,'l1':symp})
            q12=q1.intersection(q2)
            q13=q1.intersection(q3)
            q23=q2.intersection(q3)
            if(q12 or q13 or q23):
                return render(request,'search.html',{'q12':q12,'q13':q13,'q23':q23,'found':True,'c':c,'l1':symp})
            else:
                return render(request,'search.html',{'q1':q1,'found':True,'c':c,'q2':q2,'q3':q3,'l1':symp,'sug':'provide matching symptoms to get suitable results if possible'})
        else:
            if(ds1 or ds2):
                q1=set(ds1)
                q2=set(ds2)
                q=set(ds1).intersection(set(ds2))
        
                if(q):
                    return render(request,'search.html',{'q':q,'found':True,'c':c,'l1':symp})
                else:
                    return render(request,'search.html',{'q1':q1,'found':True,'c':c,'q2':q2,'l1':symp,'sug':'provide more symptoms to get perfect results if possible'})
            else:
                return render(request,'search.html',{'msg':'Sorry!!!not found any matching results..kindly request you to provide this details in FAQ. our team will give you satisfiable answer there..','found':False,'c':c,'l1':symp})
    return render(request,'search.html')

def hospitalsearchnearest(request):
    object_list=Hospital.objects.all()
    sorted_list=[]
    for hosp in object_list:
        g=geocoder.ip('me')
        geolocator=Nominatim(user_agent='WeCare')
        location=geolocator.geocode(hosp.location)
        print(location)
        location2=(location.latitude,location.longitude)
        location3=(g.lat,g.lng)
        print(location.address)
        print(g.address)
        print((location.latitude,location.longitude))
        print((g.lat,g.lng))
        hosp.distance=geodesic(location2,location3).km
        print(hosp.distance)
        # hosp.distance=int(great_circle(location2,location3).km)

    for hosp in object_list:
        if hosp.distance<=10:
            info={
                    "name":hosp.name,
                    "address":hosp.address,
                    "location":hosp.location,
                    "pincode":hosp.pincode,
                    "speciality":hosp.speciality,
                    "timings":hosp.timings,
                    "distance":hosp.distance
            }
            sorted_list.append(info)
    s_list=sorted(sorted_list,key=lambda i:i['distance'])
    print(s_list)
    return render(request,'nearesthospital.html',{'objectlist':s_list,'found':True})

def pharmacysearchnearest(request):
    object_list=Pharmacy.objects.all()
    sorted_list=[]
    for pharm in object_list:
        g=geocoder.ip('me')
        geolocator=Nominatim(user_agent='WeCare')
        location=geolocator.geocode(pharm.location)
        print(pharm.location)
        location2=(location.latitude,location.longitude)
        location3=(g.lat,g.lng)
        print(location.address)
        print(g.address)
        print((location.latitude,location.longitude))
        print((g.lat,g.lng))
        pharm.distance=geodesic(location2,location3).km

    for pharm in object_list:
        if pharm.distance<=5:
            info={
                "name":pharm.name,
                "location":pharm.location,
                "distance":pharm.distance
            }
            sorted_list.append(info)
    s_list=sorted(sorted_list,key=lambda i:i['distance'])
    print(s_list)
    return render(request,'nearestpharmacy.html',{'objectlist':s_list,'found':True})

# def api(request):
#     user_long=None
#     user_lat=None
#     km=3
#     hospitals=Hospital.objects.all()
#     pincode=request.GET.get('pincode','')
#     if pincode:
#         geolocator=Nominatim(user_agent="WeCare")
#         location=geolocator.geocode(int(pincode))
#         user_lat=location.latitude
#         user_long=location.longitude

#     payload=[]
#     for hosp in hospitals:
#         result={
#            "name":hosp.name,
#             "address":hosp.address,
#             "location":hosp.location,
#             "speciality":hosp.speciality,
#             "timings":hosp.timings,
#         }
#         if pincode:
#             first=(float(user_lat),float(user_long))
#             second=(float(hosp.lat),float(hosp.long))
#             hosp.distance=int(great_circle(first,second).km)
#             result['distance']=hosp.distance
#         if result['distance']<=5:
#             payload.append(result)
#     s_list=sorted(payload,key=lambda i:i['distance'])
#     return render(request,'nearesthospital.html',{'objectlist':s_list,'found':True})

    
