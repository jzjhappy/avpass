# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-25 18:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(choices=[('a-plus', 'A+ PC Technician'), ('advance java', 'Advance Java/J2EE/Weblogic/Websphere'), ('a-s master', 'Agile-Scrum Master'), ('android mobile', 'Android Mobile Development'), ('autocad', 'AutoCAD'), ('bio-info', 'Bio-info Database Training course'), ('ba', 'Business Analyst (BA)'), ('c-sharp', 'C# .Net'), ('ccna', 'CCNA Voice'), ('ceh', 'Certified Ethical Hacking'), ('checkpoint', 'Checkpoint Security Firewall Course'), ('ip_tech', 'Cisco CCIE IP Telephony'), ('routing', 'Cisco CCIE Lab - Routing & Switch'), ('security', 'Cisco CCIE Security'), ('cisco_training', 'Cisco CCIE Training Course'), ('ccna', 'Cisco CCNA'), ('ccna_and_ccnp', 'Cisco CCNA & CCNP'), ('ccnp', 'Cisco CCNP'), ('ids', 'Cisco IDS'), ('intenet_expert', 'Cisco Internet Expert'), ('telephony', 'Cisco IP Telephony'), ('pix_firewall', 'Cisco PIX Firewall Security Specialist'), ('secure', 'Cisco Secure'), ('security_and_checkpoint', 'Cisco Security & Check Point Security'), ('vpn', 'Cisco VPN'), ('cissp', 'CISSP'), ('client_server', 'Client Server Specialist'), ('clinical_sa', 'Clinical SA'), ('cna', 'CNA'), ('comptia', 'CompTIA Security+'), ('forensics', 'Computer Forensics'), ('accounting', 'Computerized Accounting Specialist'), ('medical_office', 'Computerized Medical Office Assistant'), ('warehouse_cognos', 'Data Warehouse & Cognos'), ('data_admin', 'Database Administrator Expert'), ('data_developer', 'Database Developer'), ('data_specialist', 'Database Specialist Training'), ('debate', 'Debate Team'), ('implement_data', 'Design & Implement Database'), ('desktop_app', 'Desktop Application Specialist'), ('ecommerce', 'E-Commerce Package Training Course'), ('ekg', 'EKG'), ('emc_and_san', 'EMC & SAN'), ('emr', 'EMR'), ('english_enrich', 'English Enrichment'), ('exchange_server', 'Exchange Server 5000'), ('grapich_design', 'Graphic Design'), ('design_flash', 'Graphic Design - Flash'), ('design_html', 'Graphic Design - HTML'), ('design_illust', 'Graphic Design - Illustrator'), ('indesign', 'Graphic Design - InDesign'), ('photoshop', 'Graphic Design - Photoshop'), ('quak-express', 'Graphic Design - Qwak Express'), ('hadoop', 'Hadoop'), ('db2_certificate', 'IBM DB2 Certification Program'), ('ibm_websphere', 'IBM Websphere Program'), ('image_graphic', 'Image Graphic Design'), ('internet_security', 'Internet Security Specialist'), ('it_audit', 'IT Auditing'), ('it_incubate', 'IT Incubation'), ('java_2', 'Java 2 Certificate'), ('java_develop', 'JAVA Developer Package Training'), ('job_placement', 'Job Placement'), ('linux_sa', 'Linux SA Workshop'), ('linux_sa_work', 'Linux SA Workshop'), ('olympiad', 'Math Olympiads'), ('mcitp', 'MCITP'), ('mcsa', 'MCSA Windows 2003'), ('mctsd', 'MCTSD Windows 2003'), ('med_assist', 'Medical Assistant'), ('med_bill_and_code', 'Medical Billing & Coding Specialist'), ('med_bill', 'Medical Billing Specialist'), ('med_cert_code', 'Medical Certified Coder'), ('med_lab_tech', 'Medical Lab Technician'), ('med_transcirpt', 'Medical Transcript'), ('ms_c-sharp', 'Microsoft C# & .Net Training'), ('ms_data_admin', 'Microsoft Certified Database Admin'), ('ms_office', 'Microsoft Office Specialists'), ('ms_mous', 'Microsoft User MOUS Applications'), ('mos_access', 'MOS Access'), ('mos_access_adv', 'MOS Access Advanced'), ('mos_access_beg', 'MOS Access Begginner'), ('mos_access_int', 'MOS Access Intermediate'), ('excel_adv', 'MOS Excel Advance'), ('excel_beg', 'MOS Excel Beginner'), ('excel_core', 'MOS Excel Core'), ('excel_exp', 'MOS Excel Expert'), ('excel_int', 'MOS Excel Intermediate'), ('frontpage', 'MOS FrontPage'), ('outlook', 'MOS Outlook'), ('outlook_adv', 'MOS Outlook Advanced'), ('outlook_beg', 'MOS Outlook Beginner'), ('outlook_int', 'MOS Outlook Intermediate'), ('powerpoint', 'MOS PowerPoint'), ('powerpoint_adv', 'MOS PowerPoint Advanced'), ('powerpoint_beg', 'MOS Powerpoint Beginner'), ('powerpoint_int', 'MOS Powerpoint Intermediate'), ('word_adv', 'MOS Word Advanced'), ('word_beg', 'MOS Word Beginner'), ('word_int', 'MOS Word Intermediate'), ('ms_proj', 'MS Project 2003'), ('ms_security', 'MS Security'), ('mssql', 'MS SQL Admin'), ('windows_2000', 'MS Windows 2000 MCSE'), ('windows_2003', 'MS Windows 2003 MCSE'), ('network-plus', 'Network+'), ('nurse', 'Nurse'), ('oracle_data', 'Oracle 9i Database Administrator'), ('oracle_handson', 'Oracle 9i Hands-on Project'), ('oracle_clinic', 'Oracle Clinical Data Management'), ('oracle_data_admin', 'Oracle Database Administrator'), ('oracle_develop_web', 'Oracle Developer/2000 & Web Application'), ('oracle_finance', 'Oracle Finance Application Server'), ('oracle_financial', 'Oracle Financial Application Server'), ('oracle_oca/ocp', 'Oracle OCA/OCP DBA'), ('oracle_upgrade', 'Oracle Upgrade to 9i'), ('patient_care', 'Patient Care Tech'), ('pc/lan', 'PC/LAN Help & Support Specialist'), ('pharmacy_tech', 'Pharmacy Tech'), ('proj_manage', 'Project Management Training Course'), ('sat', 'PSAT/SAT/SAT II'), ('qual_assur_auto', 'Quality Assurance - Automation'), ('qual_assur_train', 'Quality Assurance Training Package'), ('rmp', 'Risk Management Project (RMP)'), ('sap-bibo', 'SAP-BIBO'), ('sap-crm', 'SAP-CRM'), ('sap-fico', 'SAP-FICO'), ('sap-hr', 'SAP-HR'), ('sap-mm', 'SAP-MM'), ('sas', 'SAS Training'), ('siebel', 'Siebel(CRM) 6/7 Application'), ('6-sigma', 'Six Sigma'), ('sftwr_special', 'Software Specialist Training Program'), ('sftwr_test', 'Software Tester Specialist'), ('stat_analyze', 'Statistical Analyze Specialist'), ('summer', 'Summer Camp'), ('sun_unix', 'Sun Unix Hands-on Project'), ('sweepstakes', 'Sweepstakes'), ('test', 'Test'), ('unix', 'Unix System Administrator'), ('vbnet', 'VB.NET'), ('visual-basic', 'Visual Basic & SQL Server Course'), ('vmware', 'VMWare'), ('web_develop', 'Web Developer/E-Commerce Specialist')], default='a-plus', max_length=128)),
                ('location', models.CharField(choices=[('south_plainfield', 'South Plainfield'), ('hackensack', 'Hackensack'), ('fairfield', 'Fairfield'), ('eatontown', 'Eatentown')], default='south_plainfield', max_length=128)),
                ('room', models.CharField(choices=[('A', 'South Plainfield A: CNA/MCSE'), ('B', 'South Plainfield B: SAS/.Net'), ('C', 'South Plainfield C: Cisco'), ('D', 'South Plainfield D: QA/.Net/Java'), ('E', 'South Plainfield E: Weblogic/Java/MCSE'), ('F', 'South Plainfield F: Unix/Linux'), ('G', 'South Plainfield G: Oracle/Clinic/Datawarehouse')], default='A', max_length=128)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('start_time', models.CharField(choices=[('eight-thirty am', '8:30 AM'), ('nine am', '9:00 AM'), ('nine-thirty am', '9:30 AM'), ('ten am', '10:00 AM'), ('ten-thirty am', '10:30 AM'), ('eleven am', '11:00 AM'), ('eleven-thirty am', '11:30 AM'), ('twelve pm', '12:00 PM'), ('twelve-thirty pm', '12:30 PM'), ('one pm', '1:00 PM'), ('one-thirty pm', '1:30 PM'), ('two pm', '2:00 PM'), ('two-thirty pm', '2:30 PM'), ('three pm', '3:00 PM'), ('three-thirty pm', '3:30 PM'), ('four pm', '4:00 PM'), ('four-thirty pm', '4:30 PM'), ('five pm', '5:00 PM'), ('five-thirty pm', '5:30 PM'), ('six pm', '6:00 PM'), ('six-thirty pm', '6:30 PM'), ('seven pm', '7:00 PM'), ('seven-thirty pm', '7:30 PM'), ('eight pm', '8:00 PM'), ('eight-thirty pm', '8:30 PM'), ('nine pm', '9:00 PM'), ('nine-thirty pm', '9:30 PM'), ('ten pm', '10:00 PM')], default='eight-thirty am', max_length=128)),
                ('end_time', models.CharField(choices=[('eight-thirty am', '8:30 AM'), ('nine am', '9:00 AM'), ('nine-thirty am', '9:30 AM'), ('ten am', '10:00 AM'), ('ten-thirty am', '10:30 AM'), ('eleven am', '11:00 AM'), ('eleven-thirty am', '11:30 AM'), ('twelve pm', '12:00 PM'), ('twelve-thirty pm', '12:30 PM'), ('one pm', '1:00 PM'), ('one-thirty pm', '1:30 PM'), ('two pm', '2:00 PM'), ('two-thirty pm', '2:30 PM'), ('three pm', '3:00 PM'), ('three-thirty pm', '3:30 PM'), ('four pm', '4:00 PM'), ('four-thirty pm', '4:30 PM'), ('five pm', '5:00 PM'), ('five-thirty pm', '5:30 PM'), ('six pm', '6:00 PM'), ('six-thirty pm', '6:30 PM'), ('seven pm', '7:00 PM'), ('seven-thirty pm', '7:30 PM'), ('eight pm', '8:00 PM'), ('eight-thirty pm', '8:30 PM'), ('nine pm', '9:00 PM'), ('nine-thirty pm', '9:30 PM'), ('ten pm', '10:00 PM')], default='eight-thirty am', max_length=128)),
                ('instructor', models.CharField(choices=[('adewale', 'Adewale Akinokun'), ('ajay', 'Ajay Kumar'), ('ajay_kumar', 'Ajay Kumar Bansal'), ('alexis', 'Alexis Valencia'), ('ana', 'Ana Johnson'), ('anand', 'Anand Chanchlani'), ('andrew', 'Andrew Zhang'), ('anisa', 'Anisa Johnson'), ('anju', 'Anju Bhasin'), ('anna', 'Anna Johnson'), ('anthony', 'Anthony Boffice'), ('antonio', 'Antonio Terminiello'), ('archana', 'Archana Seth'), ('ariel', 'Ariel Almacen'), ('arthur', 'Arthur Shebar'), ('ashok', 'Ashok Kalakota'), ('badar', 'Badar Sid'), ('brian', 'Brian Barretto'), ('bruce', 'Bruce Cialfi'), ('camille', 'Camille Agama'), ('carla', 'Carla Fallone'), ('carol', 'Carol Ball'), ('carolyn', 'Carolyn Shelton'), ('chandra_p', 'Chandra Praba Botcha'), ('chandra_s', 'Chandra Sekhar Botcha'), ('charles_b', 'Charles Beltran'), ('charles_h', 'Charles Huang'), ('charles_p', 'Charles Paver'), ('cleo', 'Cleo Ramos'), ('cynthia_l', 'Cynthia Little'), ('cynthia_w', 'Cynthia Wang'), ('dan', 'Dan Mendoza'), ('david_pa', 'David Pascal'), ('david_pr', 'David Prowse'), ('david_s', 'David Sing'), ('demitria', 'Demitria Orgo'), ('dennis', 'Dennis Lung'), ('devang', 'Devang Patel'), ('dmitriy', 'Dmitriy A. Krymchanskiy'), ('don', 'Don Hoffman'), ('donald', 'Donald Hsu'), ('douglas', 'Dr. Douglas J. Bolton'), ('drew', 'Drew Beebe'), ('eddy', 'Eddy Li'), ('edward_m', 'Edward McCrae'), ('edward_c', 'Edward (Wonjun) Choi'), ('effie', 'Effie He'), ('elie', 'Elie Phanor'), ('emil', 'Emil EJ Smith'), ('eric', 'Eric Silverstein'), ('erica', 'Erica James'), ('eugene', 'Eugene Bai'), ('eva', 'Eva Henry'), ('fawad', 'Fawad Khan'), ('felice', 'Felice D'), ('frank_li', 'Frank Lin'), ('frank_lu', 'Frank Lu'), ('frederick', 'Frederick Miller'), ('gary_g', 'Gary Guan'), ('gary_m', 'Gary Mao'), ('gil', 'Gil Newman'), ('gurudas', 'Gurudas Patil'), ('hai', 'Hai John Pan'), ('hector', 'Hector Reyes'), ('helen', 'Helen Njau'), ('henry', 'Henry Ma'), ('homiler', 'Homiler E Phanor'), ('hongbing', 'Hongbing Ding'), ('hseng', 'Hseng Wee Ng'), ('irene_g', 'Irene Gerlovin'), ('irene_t', 'Irene Toufiles'), ('jack_w', 'Jack Wang'), ('jack_z', 'Jack Zhen'), ('james', 'James Carr'), ('jamie', 'Jamie Juarbe'), ('jay', 'Jay Shyam N. Jayakumar'), ('jayan', 'Jayan M. Joseph'), ('jennifer_g', 'Jennifer Gwo'), ('jennifer_k', 'Jennifer Kiefer'), ('john_a', 'John Ao'), ('john_k', 'John Kormos'), ('john_s', 'John Shorter'), ('jonathan_m', 'Jonathan Montgomery'), ('jonathan_y', 'Jonathan Yan'), ('joseph', 'Joseph Miao'), ('judith', 'Judith Rodgers'), ('jun_r', 'Jun Reitman'), ('jun_w', 'Jun Wang'), ('katheleen', 'Katheleen Mouhanna'), ('keith', 'Keith A. Tice'), ('kin', 'Kin Chan'), ('lakshman', 'Lakshman P'), ('larry', 'Larry Marden'), ('laszio', 'Laszio Kopeczi-Boocz'), ('leonard', 'Leonard Lu'), ('logan', 'Logan Song'), ('lookman', 'Lookman Fazal'), ('louis_d', 'Louis DiPerna'), ('louis_s', 'Louis Soto'), ('lu', 'Lu Zhang'), ('lulu', 'Lulu Hicks'), ('manpreet', 'Manpreet Singh'), ('manuel', 'Manuel Mesia'), ('marilyn', 'Marilyn Truppo'), ('mark', 'Mark Brisson'), ('marnie', 'Marnie Vyff'), ('mary', 'Mary Jean Knoepfler'), ('maryann', 'Maryann Bouco'), ('mayen', 'Mayen Shah'), ('michael_f', 'Michael Fazio'), ('michael_s', 'Michael Steirman'), ('michael_v', 'Michael Vana'), ('mike_p', 'Mike Peters'), ('mike_c', 'Mike Chen Chen'), ('mohammed', 'Mohammed Shabber'), ('nanak', 'Nanak Sawlani'), ('naomi', 'Naomi Sauer'), ('nihal', 'Nihal S.'), ('norman', 'Norman Stern'), ('om', 'Om Maduri'), ('patricia', 'Patricia Coccaro'), ('paul_c', 'Paul Cirillo'), ('paul_k', 'Paul Krinzman'), ('peruma', 'Peruma Lakshman'), ('phil', 'Phil Crocker'), ('pratibha', 'Pratibha Bhat'), ('pravin', 'Pravin Ghandhi'), ('rachanee', 'Rachanee Singprasong'), ('raghav', 'Raghav Seth'), ('raj_g', 'Raj Guttha'), ('raj_p', 'Raj Patel'), ('rajiv', 'Rajiv'), ('ralph', 'Ralph Walker'), ('ramesh', 'Ramesh Chilukuri'), ('ramon', 'Ramon Toalombo'), ('randall', 'Randall Bratton'), ('rasheim', 'Rasheim Myers'), ('reeves', 'Reeves Alex'), ('regina', 'Regina Haber'), ('richard', 'Richard Xue'), ('rick', 'Rick Chen'), ('rikesh', 'Rikesh Modi'), ('robert_b', 'Robert Bolmer'), ('robert_w', 'Robert William'), ('roberto', 'Roberto Lopez'), ('rohit', 'Rohit Parti'), ('ron', 'Ron Carnicelli'), ('ruthie', 'Ruthie Yu'), ('sadia', 'Sadia Bhatti'), ('sairam', 'Sairam Nedunuri'), ('sajid', 'Sajid Abbasi'), ('sakthi', 'Sakthi Pichaimani'), ('samira', 'Samira Bagh'), ('sandra', 'Sandra Anojulu'), ('sarah', 'Sarah Diroff'), ('scott', 'Scott Zhu'), ('sean', 'Sean Kim'), ('sekhar', 'Sekhar Pandit'), ('shabbir', 'Shabbir Jariwala'), ('shabuddin', 'Shabuddin Sheik'), ('shyam', 'Shyam Jay Kumar'), ('sid', 'Sid Badar'), ('stela', 'Stela Anguelova'), ('steve_a', 'Steve Ajmeri'), ('steve_h', 'Steve Hill'), ('steve_y', 'Steve Yang'), ('steven', 'Steven Schilling'), ('subarau', 'Subarau 0'), ('subramaniam', 'Subramaniam Tangiral'), ('sue', 'Sue Chung'), ('surva', 'Surva Datta'), ('sushma', 'Sushma Chopra'), ('syed_a', 'Syed Ali'), ('syed_f', 'Syed Fouad Hussaim'), ('theresa', 'Theresa Desauliniers'), ('thomas', 'Thomas Gan'), ('thushyanthy', 'Thushyanthy Balasingham'), ('tom', 'Tom Qu'), ('vanessa', 'Vanessa Brownfield-Bynum'), ('venkat_n', 'Venkat Navaneethakrishnan'), ('venkat_r', 'Venkat Radhakrishnan'), ('verona', 'Verona Bassaragh-McKay'), ('vickie', 'Vickie Eaton'), ('vijaykumar', 'Vijaykumar Allampalli'), ('vikas', 'Vikas Seth'), ('wally', 'Wally Ero-Phillips'), ('wei', 'Wei Gao'), ('yu', 'Yu Shen Sean Wang'), ('zhenda', 'Zhenda Xing')], default='adewale', max_length=128)),
                ('total_hours', models.CharField(choices=[('six', '6'), ('ten', '10'), ('twelve', '12'), ('twenty', '20'), ('twenty-four', '24'), ('twenty-five', '25'), ('twenty-eight', '28'), ('thirty', '30'), ('thirty-two', '32'), ('thirty-five', '35'), ('forty', '40'), ('forty-five', '45'), ('fifty', '50'), ('sixty', '60'), ('seventy', '70'), ('seventy-five', '75'), ('eighty', '80'), ('ninety', '90'), ('ninety-six', '96'), ('hundred', '100'), ('one-twenty', '120'), ('one-fifty', '150'), ('one-sixty', '160'), ('one-eighty', '180'), ('two-hundred', '200'), ('two-forty', '240'), ('two-fifty', '250'), ('two-eighty', '280'), ('three-hundred', '300'), ('three-twenty', '320'), ('three-sixty', '360'), ('four-hundred', '400'), ('four-twenty', '420'), ('four-eighty', '480'), ('seven-hundred', '700'), ('nine-eighty', '980'), ('fourteen-forty', '1440')], default='six', max_length=128)),
                ('hours_per_class', models.CharField(choices=[('two_and_half', '2.5'), ('three', '3'), ('four', '4'), ('four_and_half', '4.5'), ('five', '5'), ('six', '6'), ('seven', '7'), ('seven_and_half', '7'), ('eight', '8'), ('nine', '9'), ('ten', '10')], default='four_and_half', max_length=128)),
                ('frequency', models.CharField(max_length=128)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('expired', 'Expired'), ('pending', 'Pending')], max_length=128)),
                ('interval', models.CharField(choices=[('1 day', '1 Day'), ('2 days', '2 Days'), ('3 days', '3 Days'), ('4 days', '4 Days'), ('5 days', '5 Days'), ('6 days', '6 Days'), ('1 week', '1 Week'), ('2 weeks', '2 Weeks'), ('3 weeks', '3 Weeks'), ('4 weeks', '4 Weeks'), ('5 weeks', '5 Weeks'), ('6 weeks', '6 Weeks'), ('8 weeks', '8 Weeks'), ('12 weeks', '12 Weeks')], default='1 day', max_length=128)),
            ],
        ),
    ]