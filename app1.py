

from flask import Flask,render_template,redirect,request



app=Flask(__name__)


login_user=[]


source=['chennai','madurai','coimbatore']
destinations=['kanyakumari','bangalore','ooty']

list_of_booking=['None']
user_booking_detail=['None']

buses_and_route=[
    {
        'id':1,'bus_name':'KPN bus','source':'chennai','destination':'kanyakumari','price':200
    },
    {
        'id':2,'bus_name':'MARK bus','source':'chennai','destination':'kanyakumari','price':250
    }, 
    {
        'id':3,'bus_name':'RDK bus','source':'chennai','destination':'bangalore','price':350
    }, 
    {
        'id':4,'bus_name':'FAST bus','source':'madurai','destination':'bangalore','price':300
    }, 
    {
        'id':5,'bus_name':'NICK bus','source':'coimbatore','destination':'ooty','price':200
    }, 
    {
        'id':6,'bus_name':'RICK bus','source':'coimbatore','destination':'ooty','price':200
    }
]


bus_list=[]

@app.route('/',methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        data={'username':username,'password':password}
        login_user.append(data)
        if login_user:
            print(username)
            return render_template('booking_page.html',datas=data,name=username,login_user=login_user)
    return render_template('login.html')

@app.route('/logout',methods=['GET','POST'])
def logout():
    return render_template('login.html')


@app.route('/booking_page',methods=['GET','POST'])
def booking_page():
     return render_template('booking_page.html')


#------------------bus------------------------------
@app.route('/search_bus',methods=['GET','POST'])
def Search_bus():
    if request.method=='POST':
        Source=request.form.get('from_')
        destination=request.form.get('to_')
        new=[]
        for i in buses_and_route:
            if i['source']==Source and i['destination']==destination:
                n1={'id':i['id'],'from':Source,'to':destination,'buses':i['bus_name'],'price':i['price']}
                new.insert(0,n1)    
                bus_list.insert(0,n1)              
        return render_template('bus/avail_bus.html',buses=new,count=len(new))          
    return render_template('bus/searching_bus.html',start_point=source,end_point=destinations)

@app.route('/avail_detail',methods=['GET','POST'])
def avail_bus():
    return render_template('bus/avail_bus.html')


@app.route('/bus_detail/<int:id>',methods=['GET','POST'])
def bus_detail(id):
    booking_form=['None']
    for i in bus_list:
        if id==i['id']:
            booking_form[0]=i
    if request.method=='POST':
        name=request.form.get('name')
        age=request.form.get('age')
        gender=request.form.get('gender')
        from_=request.form.get('from_')
        to_=request.form.get('to_')
        phone=request.form.get('phone')
        ticket=request.form.get('ticket')
        bus_name=request.form.get('bus_name')

        total_price=booking_form[0]['price']*int(ticket)  

        p={'id':id,'name':name,'age':age,'gender':gender,'from_':from_,'to_':to_,'phone':phone,'ticket':ticket,'bus_name':bus_name,'total_price':total_price}   
        list_of_booking.insert(0,p)
        
        return render_template('bus/booking_detail.html',lists=list_of_booking)         
    return render_template('bus/booking_bus.html',booking_form=booking_form)


@app.route('/booking_detail',methods=['GET','POST'])
def details():
    return render_template('bus/booking_detail.html',lists=list_of_booking)

@app.route('/payment',methods=['GET','POST'])
def payment():
    if request.method=='POST':
        card_no=request.form.get('card_no')
        expire=request.form.get('expire')
        cvv=request.form.get('cvv')
        user_booking_detail[0]=list_of_booking 
        return render_template('booking_page.html',message="payment successfull")
    return render_template('bus/payment.html')       




#---------------------------------flight------------------------------

source1=['chennai','madurai','bangalore']
destinations1=['delhi','hydrabat','kochi']

list_of_flight_booking=['None']
user_flight_booking_detail=['None']

flight_and_route=[
    {
        'id':1,'flight_name':'A1 Flight','source':'chennai','destination':'delhi','price':200
    },
    {
        'id':2,'flight_name':'B1 Flight','source':'chennai','destination':'hydrabat','price':250
    }, 
    {
        'id':3,'flight_name':'A2 Flight','source':'chennai','destination':'mumbai','price':350
    }, 
    {
        'id':4,'flight_name':'B2 Flight','source':'madurai','destination':'mumbai','price':300
    }, 
    {
        'id':5,'flight_name':'B2 Flight','source':'bangalore','destination':'kochi','price':200
    }, 
    {
        'id':6,'flight_name':'C1 Flight','source':'bangalore','destination':'kochi','price':200
    }
]


flight_list=[]


@app.route('/flight/search_flight',methods=['GET','POST'])
def Search_flight():
    if request.method=='POST':
        Sources=request.form.get('from_')
        destination=request.form.get('to_')
        new=[]
        for i in flight_and_route:
            if i['source']==Sources and i['destination']==destination:
                n1={'id':i['id'],'from':Sources,'to':destination,'flight':i['flight_name'],'price':i['price']}
                new.insert(0,n1)    
                flight_list.insert(0,n1)              
        return render_template('flight/flight_avail.html',flight=new,count=len(new))          
    return render_template('flight/searching_flight.html',start_point=source1,end_point=destinations1)

@app.route('/flight/avail_detail',methods=['GET','POST'])
def avail_flight():
    return render_template('flight/flight_avail.html')


@app.route('/flight/flight_detail/<int:id>',methods=['GET','POST'])
def flight_detail(id):
    booking_form=['None']
    for i in flight_list:
        if id==i['id']:
            booking_form[0]=i
    if request.method=='POST':
        name=request.form.get('name')
        age=request.form.get('age')
        gender=request.form.get('gender')
        from_=request.form.get('from_')
        to_=request.form.get('to_')
        phone=request.form.get('phone')
        ticket=request.form.get('ticket')
        flight_name=request.form.get('flight_name')

        total_price=booking_form[0]['price']*int(ticket)  

        p={'id':id,'name':name,'age':age,'gender':gender,'from_':from_,'to_':to_,'phone':phone,'ticket':ticket,'flight_name':flight_name,'total_price':total_price}   
        list_of_flight_booking.insert(0,p)   

        return render_template('flight/booking_detail.html',lists=list_of_flight_booking)         
    return render_template('flight/booking_flight.html',booking_form=booking_form)


@app.route('/flight/booking_detail',methods=['GET','POST'])
def flight_details():
    return render_template('flight/booking_detail.html',lists=list_of_flight_booking)

@app.route('/flight/payment',methods=['GET','POST'])
def flight_payment():
    if request.method=='POST':
        card_no=request.form.get('card_no1')
        expire=request.form.get('expire')
        cvv=request.form.get('cvv1')
        user_flight_booking_detail[0]=list_of_flight_booking 
        return render_template('booking_page.html',message="payment successfull")
    
    return render_template('flight/payments.html')     

#----------------------------train------------------------

source2=['chennai','madurai','bangalore']
destinations2=['delhi','hydrabat','kochi']

list_of_train_booking=[]
user_train_booking_detail=['none']

train_and_route=[
    {
        'id':1,'train_name':'india_express train','source':'chennai','destination':'delhi','price':200
    },
    {
        'id':2,'train_name':'A2 train','source':'chennai','destination':'mumbai','price':350
    }, 
    {
        'id':3,'train_name':'B2 train','source':'madurai','destination':'mumbai','price':300
    }, 
    {
        'id':4,'train_name':'C1 train','source':'bangalore','destination':'kochi','price':200
    }
]


train_list=[]


@app.route('/train/search_bus',methods=['GET','POST'])
def Search_train():
    if request.method=='POST':
        Sources2=request.form.get('from_')
        destinationss2=request.form.get('to_')
        new=[]
        for i in train_and_route:
            if i['source']==Sources2 and i['destination']==destinationss2:
                n1={'id':i['id'],'from':Sources2,'to':destinationss2,'train':i['train_name'],'price':i['price']}
                new.insert(0,n1)    
                train_list.insert(0,n1)              
        return render_template('train/train_avail.html',train=new,count=len(new))          
    return render_template('train/searching_train.html',start_point=source2,end_point=destinations2)

@app.route('/train/avail_detail',methods=['GET','POST'])
def avail_train():
    return render_template('train/train_avail.html')


@app.route('/train/train_detail/<int:id>',methods=['GET','POST'])
def train_detail(id):
    booking_form=['None']
    for i in train_list:
        if id==i['id']:
            booking_form[0]=i
    if request.method=='POST':
        name=request.form.get('name')
        age=request.form.get('age')
        gender=request.form.get('gender')
        from_=request.form.get('from_')
        to_=request.form.get('to_')
        phone=request.form.get('phone')
        ticket=request.form.get('ticket')
        train_name=request.form.get('train_name')

        total_price=booking_form[0]['price']*int(ticket)  

        p={'id':id,'name':name,'age':age,'gender':gender,'from_':from_,'to_':to_,'phone':phone,'ticket':ticket,'train_name':train_name,'total_price':total_price}   
        list_of_train_booking.insert(0,p)   

        return render_template('train/booking_detail.html',lists=list_of_train_booking)         
    return render_template('train/booking_train.html',booking_form=booking_form)


@app.route('/train/booking_detail',methods=['GET','POST'])
def train_details():
    return render_template('train/booking_detail.html',lists=list_of_train_booking)

@app.route('/train/payment',methods=['GET','POST'])
def train_payment():
    if request.method=='POST':
        card_no=request.form.get('card_no1')
        expire=request.form.get('expire')
        cvv=request.form.get('cvv1')
        user_train_booking_detail[0]=list_of_train_booking 
        return render_template('booking_page.html',message="payment successfull")
    return render_template('train/paymentss.html')     






@app.route('/result',methods=['GET','POST'])
def result():    
    return render_template('result.html',bookings=user_booking_detail,booking1=user_flight_booking_detail,booking2=user_train_booking_detail)


if __name__=='__main__':
    app.run(debug=True)
