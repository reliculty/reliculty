from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import *
from . import db
import os

views = Blueprint('views', __name__)
static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

@views.route('/', methods=['GET', 'POST'])
@login_required
def interface():
    if request.method == 'POST':   

        #teaching and non teaching staff variables
        if 'teaching_staff' in request.form:
            tname = request.form.get('tname')
            tqualification = request.form.get('tqualification')
            acadrank = request.form.get('acadrank')
            dept = request.form.get('dept')
            phno1 = request.form.get('phno1')
            teaching_staff = Teaching_Staff(name=tname, qualification=tqualification, academic_rank=acadrank, department=dept, phone=phno1)
            db.session.add(teaching_staff)
        
        elif 'non_teaching_staff' in request.form:
            sname = request.form.get('sname')
            squalification = request.form.get('squalification')
            duty = request.form.get('duty')
            phno2 = request.form.get('phno2')
            non_teaching_staff = Non_Teaching_Staff(name=sname, qualification=squalification, assigned_duty=duty, phone=phno2)
            db.session.add(non_teaching_staff)

        #news & events variables
        elif 'events' in request.form:
            image_file = request.files.get('event-image')
            event_title = request.form.get('event-title')
            event_description = request.form.get('event-description')
            if image_file and allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(static_path, 'img', 'events', filename))
                flash('Image added Succefully', category='success')
            else:
                filename = None
            events = Events(event_title=event_title, event_description=event_description, image_filename=filename)
            db.session.add(events)
        
        #programmes & fees variables
        elif 'programmes_fees' in request.form:
            programme = request.form.get('programme')
            fees = request.form.get('fees')
            graduation = request.form.get('graduation')
            programmes_fees = Programmes_Fees(programme=programme, fees=fees, graduation=graduation)
            db.session.add(programmes_fees)

        #downloads variables
        elif 'downloads' in request.form:
            image_name = request.files.get('image')
            file_name = request.files.get('file')
            #title = request.form.get('title')
            if image_name and allowed_file(image_name.filename):
                imgname = secure_filename(image_name.filename)
                filename = secure_filename(file_name.filename)
                image_name.save(os.path.join(static_path, 'img', 'downloads', imgname))
                file_name.save(os.path.join(static_path, 'img', 'downloads', filename))
                flash('Image added Succefully', category='success')
            else:
                imgname = None
                filename = None
            downloads = Downloads(image_name=imgname, file_name=filename)
            db.session.add(downloads)

        #IQAC variables
        elif 'iqac' in request.form:
            name = request.form.get('name')
            category = request.form.get('category')
            designation = request.form.get('designation')
            iqac = IQAC(name=name, category=category, designation=designation)
            db.session.add(iqac)

        db.session.commit()
        flash('Added Succefully', category='success')

    #ug_programmes = UG_Programmes.query.all()
    pg_programmes = PG_Programmes.query.all()
    iqac = IQAC.query.all()
    downloads = Downloads.query.all()
    programmes_fees = Programmes_Fees.query.all()
    events = Events.query.all()
    teaching_staff = Teaching_Staff.query.all()
    non_teaching_staff = Non_Teaching_Staff.query.all()
    contact = Contact.query.all()
    return render_template("interface.html"
                           , teaching_staff=teaching_staff
                           , non_teaching_staff=non_teaching_staff
                           , events=events
                           , programmes_fees=programmes_fees
                           , downloads=downloads
                           , iqac=iqac
                           , contact=contact
                           #, ug_programmes=ug_programmes
                           , pg_programmes=pg_programmes)

@views.route('/delete_record/<string:table_name>/<int:id>', methods=['GET', 'POST'])
def delete_record(table_name, id):
    if table_name == 'teaching_staff':
        table = Teaching_Staff
    elif table_name == 'non_teaching_staff':
        table = Non_Teaching_Staff
    elif table_name == 'events':
        table = Events
    elif table_name == 'programmes':
        table = Programmes_Fees
    elif table_name == 'downloads':
        table = Downloads
    elif table_name == 'iqac':
        table = IQAC
    else:
        return "Table not found"
    record = table.query.filter_by(id=id).first()
    db.session.delete(record)
    db.session.commit()
    flash(f'{table_name} record deleted successfully!', 'success')
    return redirect(url_for('views.interface'))

@views.route('/update_record/<string:table>/<int:id>', methods=['GET', 'POST'])
def update_record(table, id):
    if table == 'teaching_staff':
        table = Teaching_Staff
        template_name = 'update_teaching_staff.html'
    elif table == 'non_teaching_staff':
        table = Non_Teaching_Staff
        template_name = 'update_non_teaching_staff.html'
    elif table == 'programmes':
        table = Programmes_Fees
        template_name = 'update_programmes.html'
    elif table == 'iqac':
        table = IQAC
        template_name = 'update_iqac.html'
    else:
        flash('Table not found', category='error')
    record = table.query.filter_by(id=id).first()
    if request.method == 'POST':
        if 'teaching_staff' in request.form:
            record.name = request.form.get('tname')
            record.qualification = request.form.get('tqualification')
            record.academic_rank = request.form.get('acadrank')
            record.department = request.form.get('dept')
            record.phone = request.form.get('phno1')
            db.session.commit()
            flash('Teaching staff record updated successfully!', 'success')
            return redirect(url_for('views.interface'))
        
        elif 'non_teaching_staff' in request.form:
            record.name = request.form.get('sname')
            record.qualification = request.form.get('squalification')
            record.assigned_duty = request.form.get('duty')
            record.phone = request.form.get('phno2')
            db.session.commit()
            flash('Non Teaching staff record updated successfully!', 'success')
            return redirect(url_for('views.interface'))
            
        elif 'programmes' in request.form:
            record.programme = request.form.get('programme')
            record.fees = request.form.get('fees')
            record.graduation = request.form.get('graduation')
            db.session.commit()
            flash('Programmes record updated successfully!', 'success')
            return redirect(url_for('views.interface'))
        
        elif 'iqac' in request.form:
            record.name = request.form.get('name')
            record.category = request.form.get('category')
            record.designation = request.form.get('designation')
            db.session.commit()
            flash('IQAC record updated successfully!', 'success')
            return redirect(url_for('views.interface'))

    return render_template(template_name, record=record)


@views.route('/administration')
def administration():
    teaching_staff = Teaching_Staff.query.all()
    non_teaching_staff = Non_Teaching_Staff.query.all()
    return render_template("administration.html"
                           , teaching_staff=teaching_staff
                           , non_teaching_staff=non_teaching_staff)

@views.route('/news')
def news():
    events = Events.query.all()
    return render_template("news.html", events=events)

def upload_file():
    file = request.files['image']
    if file:
        filename = file.filename
        file.save(os.path.join('website/static/img/events', filename))
        flash('File Uploaded Succefully', category='success')
    else:
        flash('File Upload Failed', category='error')

@views.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename = 'img/events/' + filename), code = 301)

@views.route('/programmes')
def programmes():
    ug_programmes_fees = Programmes_Fees.query.filter_by(graduation="UG").all()
    pg_programmes_fees = Programmes_Fees.query.filter_by(graduation="PG").all()
    return render_template("programmes.html"
                           , ug_programmes_fees=ug_programmes_fees
                           , pg_programmes_fees=pg_programmes_fees)

@views.route('/departments')
def departments():
    return render_template("departments.html")

@views.route('/dept-english')
def english():
    teaching_staff = Teaching_Staff.query.filter_by(department='English & Journalism').all()
    return render_template("dept-english.html", teaching_staff=teaching_staff)

@views.route('/dept-commerce')
def commerce():
    teaching_staff = Teaching_Staff.query.filter_by(department='Commerce').all()
    return render_template("dept-commerce.html", teaching_staff=teaching_staff)

@views.route('/dept-social')
def social():
    teaching_staff = Teaching_Staff.query.filter_by(department='Social Work').all()
    return render_template("dept-social.html", teaching_staff=teaching_staff)

@views.route('/dept-malayalam')
def malayalam():
    teaching_staff = Teaching_Staff.query.filter_by(department='Malayalam').all()
    return render_template("dept-malayalam.html", teaching_staff=teaching_staff)

@views.route('/dept-management')
def management():
    teaching_staff = Teaching_Staff.query.filter_by(department='Management').all()
    return render_template("dept-management.html", teaching_staff=teaching_staff)

@views.route('/dept-computer')
def computer():
    teaching_staff = Teaching_Staff.query.filter_by(department='Computer Science').all()
    return render_template("dept-computer.html", teaching_staff=teaching_staff)

@views.route('/fees')
def fees():
    ugfees = Programmes_Fees.query.filter_by(graduation="UG").all()
    pgfees = Programmes_Fees.query.filter_by(graduation="PG").all()
    return render_template("fees.html", ugfees=ugfees, pgfees=pgfees)

@views.route('/downloads')
def downloads():
    downloads = Downloads.query.all()
    return render_template("downloads.html", downloads=downloads)

@views.route('/iqac')
def iqac():
    iqac = IQAC.query.all()
    return render_template("iqac.html", iqac=iqac)

@views.route('/ugadmission', methods=['GET', 'POST'])
def ugadmission():
    if request.method == 'POST':
        programme = request.form.get('programme')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        age = request.form.get('age')
        dob = request.form.get('dob')
        gender = request.form.get('gender')
        marital_status = request.form.get('marital_status')
        parent_name = request.form.get('parent_name')
        parent_relation = request.form.get('parent_relation')
        parent_occupation = request.form.get('parent_occupation')
        parent_income = request.form.get('parent_income')
        permanent_address = request.form.get('phno1')
        p_pinode = request.form.get('p_pinode')
        p_contact = request.form.get('p_contact')
        residential_address = request.form.get('residential_address')
        r_pincode = request.form.get('r_pincode')
        r_contact = request.form.get('r_contact')
        ug_programmes = UG_Programmes(programme=programme, name=name,email=email, phone=phone
                                      , age=age, dob=dob, gender=gender,marital_status=marital_status
                                      , parent_name=parent_name, parent_relation=parent_relation
                                      , parent_occupation=parent_occupation, parent_income=parent_income
                                      , permanent_address=permanent_address, p_pinode=p_pinode, p_contact=p_contact
                                      , residential_address=residential_address, r_pincode=r_pincode, r_contact=r_contact)
        db.session.add(ug_programmes)
        db.session.commit()
        flash('Details Added Succefully', category='success')
    return render_template("ugadmission.html")

@views.route('/pgadmission', methods=['GET', 'POST'])
def pgadmission():
    if request.method == 'POST':
        programme = request.form.get('programme')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        age = request.form.get('age')
        dob = request.form.get('dob')
        gender = request.form.get('gender')
        marital_status = request.form.get('marital_status')
        parent_name = request.form.get('parent_name')
        parent_relation = request.form.get('parent_relation')
        parent_occupation = request.form.get('parent_occupation')
        parent_income = request.form.get('parent_income')
        permanent_address = request.form.get('phno1')
        p_pinode = request.form.get('p_pinode')
        p_contact = request.form.get('p_contact')
        residential_address = request.form.get('residential_address')
        r_pincode = request.form.get('r_pincode')
        r_contact = request.form.get('r_contact')
        pg_programmes = PG_Programmes(programme=programme, name=name,email=email, phone=phone
                                      , age=age, dob=dob, gender=gender,marital_status=marital_status
                                      , parent_name=parent_name, parent_relation=parent_relation
                                      , parent_occupation=parent_occupation, parent_income=parent_income
                                      , permanent_address=permanent_address, p_pinode=p_pinode, p_contact=p_contact
                                      , residential_address=residential_address, r_pincode=r_pincode, r_contact=r_contact)
        db.session.add(pg_programmes)
        db.session.commit()
        flash('Details Added Succefully', category='success')
    return render_template("pgadmission.html")

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        db.session.add(contact)
        db.session.commit()
        flash('Your message has been sent. Thank you!', category='success')
    return render_template("contact.html")