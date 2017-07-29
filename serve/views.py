# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from ntw import Number2Words as ntw
from .models import database
from django.contrib.auth import authenticate,logout,login
from django.template.loader import render_to_string
from django.utils.encoding import smart_str
from django.http import HttpResponse
from os import remove
from pywkher import generate_pdf


source  = ""

def login_x(request):
    if request.method == "POST":
        user = request.POST.get('username')
        pas = request.POST.get('pass')
        user = authenticate(username=user,password=pas)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('/generate')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout_x(request):
    logout(request)
    return redirect('/login')

def main(request):
    global source
    if request.user.is_authenticated:
        if request.method == "POST":
            c_dic={}
            c_dic['firm'] = request.POST.get('firm')
            c_dic['bill_type'] = request.POST.get('bill_type')
            is_Firm1 = c_dic['firm']=="Firm 1"
            c_dic['PD']=request.POST.get('PD')
            c_dic['PT']=request.POST.get('PT')
            c_dic['IN']=request.POST.get('IN')
            c_dic['DATE']=request.POST.get('DATE')
            c_dic['TP']=request.POST.get('TP')
            c_dic['VN']=request.POST.get('VN')
            c_dic['ST']=request.POST.get('ST')
            name = request.POST.getlist('DG')
            qty = request.POST.getlist('QTY')
            unit = request.POST.getlist('UNIT')
            price = request.POST.getlist('PRICE')
            amount =[int(i.strip(' '))*int(j.strip(' ')) for i,j in zip(qty,price)]
            gst = request.POST.get('GST')
            gst_val = round(float(gst)/2.0,2)
            sno = range(1,len(name)+1)
            br_extra = range(15-len(sno))
            val = zip(sno,name,qty,unit,price,amount)
            total = sum(amount)
            gtotal = total+total*(float(gst)/100)

            #convert number to words
            words =  ntw().convertNumberToWords(gtotal)[4:]+' Only';

            # Saving all to database
            try:
                database(
                    firm = c_dic['firm'],
                    bill_type = c_dic['bill_type'],
                    invoice_no=c_dic['IN'],
                    dated = c_dic['DATE'],
                    party_details=c_dic['PD'],
                    party_tin = c_dic['PT'],
                    transport=c_dic['TP'],
                    station=c_dic['ST'],
                    vehicle_no=c_dic['VN'],
                    desc='~'.join(name),
                    qty = '~'.join([str(i) for i in qty]),
                    unit = '~'.join(unit),
                    price = '~'.join([str(i) for i in price]),
                    gst = str(gst)
                ).save()
            except:
                return HttpResponse("Data could not be saved to database")
            source = render_to_string("bill.html",{'info':c_dic,'val':val,'brs':br_extra,'last':br_extra[len(br_extra)-1],'total':total
            ,'gst':gst_val,'csgst':float(total*float(gst_val))/100,'gtotal':gtotal,'inwords':words,'is_Firm1':is_Firm1})
            pdf = generate_pdf(html=source)
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('out.pdf')
            return response

            #return render(request,"bill.html",{'info':c_dic,'val':val,'brs':br_extra,'last':br_extra[len(br_extra)-1],'total':total
            #,'gst':gst_val,'csgst':float(total*float(gst_val))/100,'gtotal':gtotal,'inwords':words})
        else:
            return render(request,"form.html")
    else:
        return redirect('/login')
        #Random comment
def regenerate(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            to_search = request.POST.get('INV')
            try:
                data = database.objects.filter(invoice_no=str(to_search))
                try:
                    data = data[0]
                except:
                    return HttpResponse("Invoice not found!")
            except:
                return HttpResponse("Unable to access database!")
            c_dic={}
            c_dic['firm'] = data.firm
            is_Firm1 = c['firm'] =="Firm 1"
            c_dic['bill_type'] = data.bill_type
            c_dic['PD']=data.party_details
            c_dic['PT']=data.party_tin
            c_dic['IN']=data.invoice_no
            c_dic['DATE']=data.dated
            c_dic['TP']=data.transport
            c_dic['VN']=data.vehicle_no
            c_dic['ST']=data.station
            name = data.desc.split('~')
            qty = data.qty.split('~')
            unit = data.unit.split('~')
            price = data.price.split('~')
            amount =[int(i.strip(' '))*int(j.strip(' ')) for i,j in zip(qty,price)]
            gst = data.gst
            gst_val = round(float(gst)/2.0,2)
            sno = range(1,len(name)+1)
            br_extra = range(15-len(sno))
            val = zip(sno,name,qty,unit,price,amount)
            total = sum(amount)
            gtotal = total+total*(float(gst)/100)

            #convert number to words
            words =  ntw().convertNumberToWords(gtotal)[3:]+' Only'
            source = render_to_string("bill.html",{'info':c_dic,'val':val,'brs':br_extra,'last':br_extra[len(br_extra)-1],'total':total
            ,'gst':gst_val,'csgst':float(total*float(gst_val))/100,'gtotal':gtotal,'inwords':words,'is_Firm1':is_Firm1})
            pdf =generate_pdf(html=source)
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('out.pdf')
            return response
        else:
            return render(request,"formx.html")
    else:
        return redirect('/login')
