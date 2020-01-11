# sparmeter_customer_registration_wizard

* copy these files into one folder.
* .env file will store the url and api keys for the site you're handling.
* Make sure that the file with customer information is within the same folder.
* The file MUST be CSV.
* Have the csv headers as  serial, meter_tariff_name ,  name ,  code ,  phone_number ,  address  etc as it appears in the documentations     
* Run cmd inside the folder
* On the cmd, type `python register.py`
* It will prompt you to enter the name of the file. Please do so without the .csv ext.
* Press enter and watch the magic happen.
* The wizard will keep a record of the registered customers and if it finds an error in the middle, it will let you know how many of them have been successfully pushed to the portal.
* If it fails, note the number then have them removed from the file.
